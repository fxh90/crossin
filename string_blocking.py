# coding = UTF-8
import jieba


def load_file():
    global list_1
    f = open('blocklist.txt')
    list_1 = f.readlines()
    for n in range(len(list_1)):
        for i in [' ', '\n', '\r']:
            list_1[n] = list_1[n].replace(i, '')


def block(a):
    a_cut = list(jieba.cut(a, cut_all=False))
    for b in list_1:
        for i in range(len(a_cut)):
            if b.decode('utf-8') == a_cut[i].lower():
                a_cut[i] = '*' * len(b.decode('utf-8'))
    a = ''.join(a_cut)
    return a


jieba.setLogLevel(60)
load_file()
while True:
    inp = raw_input('Please enter your text. Press "ENTER" to exit.\n')
    if not inp:
        break
    print block(inp)
