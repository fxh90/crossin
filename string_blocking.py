import string
def string_blocking(a):
    f = open('blocklist.txt')
    data = f.read()
    list = data.split('\n')
    print list
    for i in list:
        a = string.replace(a,i,'**')
    return a
inp = raw_input()
print string_blocking(inp)