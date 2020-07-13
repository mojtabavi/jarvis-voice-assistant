from assets.snowboy.snowboydecoder import HotwordDetector,play_audio_file
from vosk import Model, KaldiRecognizer
import pyaudio
import time
import signal

class Jarvis(object):
    def __init__(self, 
                vosk_model: str, 
                hotword_models: list,  
                sensitivity: float = 0.5, 
                command_mode_time: int = 20):

        self.interrupted = False
        self.hotword_detector = HotwordDetector(hotword_models, sensitivity=sensitivity)
        self.hotword_said = False
        vosk_model = Model(vosk_model)
        self.speech_recofnizer = KaldiRecognizer(vosk_model, 16000)
        self.command_mode_time = command_mode_time
        signal.signal(signal.SIGINT, self.on_signal)

    def hotword_interrupt_check(self):
        return self.hotword_said or self.interrupted

    def on_hotword(self):
        self.hotword_said = True
        play_audio_file() 

    def on_signal(self, signal, frame):
        self.interrupted = True

    def hotword_check(self):
        self.hotword_said = False
        self.hotword_detector.start(detected_callback=self.on_hotword,
                                    interrupt_check=self.hotword_interrupt_check,
                                    sleep_time=0.03)
        self.hotword_detector.terminate()
        return True

    def command_check(self):
        self._cmd_start_t = time.time()
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()

        while not self.command_interrupt_check():
            data = stream.read(4000)
            if len(data) == 0:
                break
            if self.speech_recofnizer.AcceptWaveform(data):
                res = self.speech_recofnizer.Result()
                print(res)
            #else:
                #print(rec.PartialResult())
        res = self.speech_recofnizer.PartialResult()
        print(res)
        stream.stop_stream()

    def command_interrupt_check(self):
        return time.time() - self._cmd_start_t > self.command_mode_time

    def run(self):
        while(self.hotword_check() and not self.interrupted):
            self.command_check()

jarvis = Jarvis(vosk_model="assets/models/vosk-api",
                hotword_models=["assets/models/JARVIS.pmdl"])
jarvis.run()