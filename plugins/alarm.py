from assistant import assistant,filters



@assistant.register_handler(filters.regexp(r'say'))
def handle(cmd, regexp):
    print(cmd, regexp)


@assistant.register_handler(filters.contains('alarm'))
def handle2(cmd):
    print(cmd)


# assistant.add_handler(handle2, contains('set'))