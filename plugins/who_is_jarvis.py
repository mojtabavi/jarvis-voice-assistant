from assistant import assistant,filters,utils


"""
Command              Description

who are you?          jarvis introduce


"""


@assistant.register_handler(filters.equals('who are you'))
@assistant.register_handler(filters.contains('who'))
def intro_cmd_mode(cmd):
    utils.play('jarvis-intro.wav')
    