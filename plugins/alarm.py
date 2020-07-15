from assistant import assistant,filters
from filters import regexp, contains


@assistant.register_handler(filters.regexp(r'say'))
def handle(cmd, regexp):
    print(cmd, regexp)


@assistant.register_handler(filters.contains('alarm'))
def handle2(cmd):
    print(cmd)


# assistant.add_handler(handle2, contains('set'))