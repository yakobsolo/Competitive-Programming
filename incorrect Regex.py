import re
for _ in range(int(input())):
    _bolean = True
    try:
        regx = re.compile(input())
    except re.error:
        _bolean = False
    print(_bolean)
