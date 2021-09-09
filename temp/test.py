

def test():
    slist = ["tt", "Sdsfd", "AA", "xx", "SZ"]
    g = filter(lambda x: x.startswith("S"), slist)
    alt = [s for s in slist if s.startswith("S")]
    print(alt, g)
    for i in g:
        print(i)


test()

print(__name__)
