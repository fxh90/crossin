# coding = UTF-8
def load_file():
    global list
    f = open('blocklist.txt')
    list = f.readlines()
def block(a):
    for n in range(list.index(list[-1])+1):
        for i in [' ','\n','\r']:
            list[n] = list[n].replace(i,'')
    for m in list:
        b = ['']
        for c in m:
            for d in range(b.index(b[-1])+1):
                b.append(b[d] + c.upper())
                b[d] += c
        for e in b:
            a = a.replace(e,'*' * len(m.decode('utf-8')))
    return a
load_file()
while True:
    inp = raw_input('Please enter your text. Press "ENTER" to exit.\n')
    if not inp:
        break
    print block(inp)