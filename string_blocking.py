# coding = UTF-8
def load_file():
    global b
    g = open('blocklist.txt')
    list = g.readlines()
    for n in range(len(list)):
        for i in [' ', '\n', '\r']:
            list[n] = list[n].replace(i, '')
    b = []
    for m in list:
        if m.isalpha() == 1:
            f = ['']
            for c in m:
                for d in range(len(f)):
                    f.append(f[d] + c.upper())
                    f[d] += c
            b += f
        else:
            b.append(m)


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
