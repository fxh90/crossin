import string
def string_blocking(a):
    f = open('blocklist.txt')
    list = f.readlines()
    for n in range(list.index(list[-1])+1):
        for i in [' ','\n','\r']:
            list[n] = string.replace(list[n],i,'')
    print list
    for m in list:
        a = string.replace(a,m,'**')
    return a
inp = raw_input()
print string_blocking(inp)