import requests, json, webbrowser


def get_wechat(keyword, num=10, page=1):
    api_key = {'apikey': '6c063d5c2170cf42e59f46ca9d59ece7'}
    url = 'http://apis.baidu.com/txapi/weixin/wxhot?num=' + str(num) + '&word=' + keyword + '&page=' + str(page)
    a = requests.get(url, headers=api_key)
    data = a.json()
    return data


keyword = raw_input('Please enter the keyword for which you would like to search.\n')
print 'Please wait...'
p = 1
while True:
    result = get_wechat(keyword, page=p)
    for n in range(10):
        try:
            a = result['newslist'][n]
        except:
            continue
        print
        print n + 1
        print 'Title:' + a['title']
        print 'Source:' + a['description']
    while True:
        choice = raw_input(
            '\nEnter number to view article in browser.\nEnter M to search for more articles.\nPress Enter to exit\n')
        if choice == 'm' or choice == 'M':
            p += 1
            break
        elif choice == '':
            break
        else:
            try:
                choice = int(choice)
                if choice in range(1, 11):
                    print result['newslist'][choice - 1]['url']
                    webbrowser.open(result['newslist'][choice - 1]['url'])
                else:
                    print 'Instruction not defined.'
            except:
                print 'Instruction not defined.'
    if bool(choice) == 0:
        break
