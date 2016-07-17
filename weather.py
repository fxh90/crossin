# coding=UTF-8
city = raw_input('Which city would you like to search for?\n')
import urllib2

try:
    web = urllib2.urlopen('http://wthrcdn.etouch.cn/weather_mini?city=%s' % (city))
    content = web.read()
except:
    print '查询失败'
try:
    from StringIO import StringIO
    import gzip

    buf = StringIO(content)
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
except:
    data = content
if data == '{"desc":"invilad-citykey","status":1002}':
    print 'Your city is invilad.'
import json

dic = json.loads(data)
try:
    print '\n' + city
    print str(dic['data']['wendu']) + '     ' + dic['data']['forecast'][0]['type']
    print dic['data']['forecast'][0]['high']
    print dic['data']['forecast'][0]['low']
    print '\n\n未来三日天气预报'
    for i in range(1, 4):
        print
        print dic['data']['forecast'][i]['date'] + '\t' + dic['data']['forecast'][i]['type']
        print dic['data']['forecast'][i]['high']
        print dic['data']['forecast'][i]['low']
except:
    print '查询失败'
