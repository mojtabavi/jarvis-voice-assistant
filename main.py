from assistant import assistant
from assistant.utils import play
import config
import importlib
import traceback


for plug in config.PLUGINS:
    try:
        print(f"Loading {plug} plugin ...")
        importlib.import_module(f'{config.PLUGINS_DIR}.{plug}')
    except Exception:
        traceback.print_exc()


assistant.run()