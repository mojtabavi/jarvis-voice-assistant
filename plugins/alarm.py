from assistant import assistant

@assistant.register_handler()
def handle(cmd):
    print(cmd)