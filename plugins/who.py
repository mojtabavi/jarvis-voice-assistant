from assistant import assistant,filters,utils


"""
Command              Description

who are you?          jarvis introduce


"""


@assistant.register_handler(filters.equals("what's your name"))
@assistant.register_handler(filters.contains('name'))
@assistant.register_handler(filters.regexp(r'name'))
def intro_cmd_mode(cmd):
    utils.play('jarvis-intro.wav')
    