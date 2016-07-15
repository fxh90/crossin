# coding = UTF-8
def load_file():
    global list
    f = open('blocklist.txt')
    list = f.readlines()
    for n in range(len(list)):
        for i in [' ', '\n', '\r']:
            list[n] = list[n].replace(i, '')


def block(a):
    for b in list:
        place = a.lower().find(b)
        while place != -1:
            a = a[0:place] + '*' * len(b.decode('utf-8')) + a[(place + len(b.decode('utf-8'))):]
            place = a.lower().find(b)
    return a


load_file()
while True:
    inp = raw_input('Please enter your text. Press "ENTER" to exit.\n')
    if not inp:
        break
    print block(inp)
