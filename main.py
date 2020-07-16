from assistant import assistant,utils
from assistant.utils import play
import config
import importlib
import traceback
import random


for plug in config.PLUGINS:
    try:
        print(f"Loading {plug} plugin ...")
        importlib.import_module(f'{config.PLUGINS_DIR}.{plug}')
    except Exception:
        traceback.print_exc()




@assistant.on_command_mode_start
def on_cmd_start():
    aus = "jarvis.wav"
    utils.play(aus)


@assistant.on_command_mode_stop
def on_cmd_stop():
    # aus = "jarvis.wav"
    # utils.play(aus)
    print("command off")



assistant.run()