# coding = UTF-8
def load_file():
    global b
    g = open('blocklist.txt')
    list = g.readlines()
    for n in range(list.index(list[-1]) + 1):
        for i in [' ', '\n', '\r']:
            list[n] = list[n].replace(i, '')
    b = []
    print list
    for m in list:
        print m.isalpha()
        if m.isalpha() == 1:
            f = ['']
            for c in m:
                for d in range(f.index(f[-1]) + 1):
                    f.append(f[d] + c.upper())
                    f[d] += c
            b += f
        else:
            b += m.isalpha()
    print b


def block(a):
    for e in b:
        a = a.replace(e, '*' * len(e.decode('utf-8')))
    return a


load_file()
while True:
    inp = raw_input('Please enter your text. Press "ENTER" to exit.\n')
    if not inp:
        break
    print block(inp)
