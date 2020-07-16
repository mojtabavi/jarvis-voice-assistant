import subprocess
from playsound import playsound
import config 







def play(audio):
    file_path = f'{config.AUDIOS_DIR}/{audio}'
    playsound(file_path)


