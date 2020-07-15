from assistant import assistant
from filters import regexp

#this is not work and program paused!!! chake it later
@assistant.register_handler(regexp(r'say'))
def handle(cmd, regexp):
    print(cmd, regexp)


# @assistant.register_handler()
# def handle(cmd):
#     print(cmd)