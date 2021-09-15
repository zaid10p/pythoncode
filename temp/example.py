import re


def is_filename_safe(filename):
    # ^ means start of string and $ means end of string
    # regex = '^[0-9]+com$'
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    # ^[a-zA-Z0-9]      start with a-zA-Z0-9
    # [a-zA-Z0-9_()-]*      then only contains a-zA-Z0-9_()- for any number of times
    # (\.jpg|\.jpeg|\.png|\.gif)$  at last, it must end with one of the four extensions,
    # since we check from start to end, it can either match the whole string or none
    return re.match(regex, filename) is not None

print(is_filename_safe('as2.jpg'))

def test():
    slist = ["tt", "Sdsfd", "AA", "xx", "SZ"]
    g = filter(lambda x: x.startswith("S"), slist)
    alt = [s for s in slist if s.startswith("S")]
    print(alt, g)
    for i in g:
        print(i)


#print(__name__)
