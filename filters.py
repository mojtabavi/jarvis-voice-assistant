import re

def regexp(pattern):
    patt = re.compile(pattern)

    def inner(cmd):
        r = patt.match(cmd)
        if r is None:
            return False
        return {"regexp": r}
    return inner