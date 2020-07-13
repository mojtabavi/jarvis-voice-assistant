from assets.snowboy.snowboydecoder import HotwordDetector,play_audio_file
from vosk import Model, KaldiRecognizer
import pyaudio

class Jarvis(object):
    def __init__(self, hotword_models: list, sensitivity: float = 0.5):
        self.interrupted = False
        self.hotword_detector = HotwordDetector(hotword_models, sensitivity=sensitivity)
        self.hotword_said = False

    def hotword_interrupt_check(self):
        return self.hotword_said or self.interrupted

    def on_hotword(self):
        self.hotword_said = True
        play_audio_file() 


    def hotword_check(self):
        self.hotword_said = False
        self.hotword_detector.start(detected_callback=self.on_hotword,
                                    interrupt_check=self.hotword_interrupt_check,
                                    sleep_time=0.03)
        self.hotword_detector.terminate()
        return True

    def run(self):
        while(True):
            print(self.hotword_check())

jarvis = Jarvis(hotword_models=["assets/models/JARVIS.pmdl"])
jarvis.run()