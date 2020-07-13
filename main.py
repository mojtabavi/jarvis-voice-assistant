from assistant import assistant
import config
import importlib
import traceback

for plug in config.PLUGINS:
    try:
        print(f"Loading {plug} plugin ...")
        importlib.import_module(f'{config.PLUGINS_DIR}.{plug}')
    except Exception:
        traceback.print_exc()
