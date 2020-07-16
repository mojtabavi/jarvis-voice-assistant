from assistant import assistant,filters,utils


"""
Command              Description

stop this            stops the command mode
go to sleep          stops the command mode


"""


@assistant.register_handler(filters.equals('stop this'))
@assistant.register_handler(filters.contains('go to sleep'))
def stop_cmd_mode(cmd):
    print("bye")
    