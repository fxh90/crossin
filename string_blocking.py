import string
def string_blocking(a):
    f = open('blocklist.txt')
    list = f.readlines()
    for i in [' ','\n','\r']:
        a = string.replace(a,i,'')
    for i in list:
        a = string.replace(a,i,'**')
    return a
inp = raw_input()
print string_blocking(inp)