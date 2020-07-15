from assistant import assistant
from filters import regexp, contains


@assistant.register_handler(regexp(r'say'))
def handle(cmd, regexp):
    print(cmd, regexp)


@assistant.register_handler(contains('alarm'))
def handle2(cmd):
    print(cmd)