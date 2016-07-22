import requests, BeautifulSoup, thread, time, os, random


def get_totalpage():
    global headers
    url = 'http://jandan.net/ooxx'
    a = requests.get(url, headers=headers)
    counter = 0
    while a.status_code != 200 and counter < 10:
        print a
        a.requests.get(url, headers=headers)
        counter += 1
    if counter == 10:
        thread.exit()
    data = a.content
    soup = BeautifulSoup.BeautifulSoup(data)
    totalpage = int((soup.find('span', {'class': "current-comment-page"}).string)[1:-1])
    return totalpage


def load_page(pagenum):
    global finished, headers, active, failed
    time3 = time.time()
    url = 'http://jandan.net/ooxx/page-%d' % pagenum
    a = requests.get(url, headers=headers)
    counter = 0
    while a.status_code != 200 and counter < 50:
        print pagenum, a
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.%d.90 Safari/537.36" % (
                2300 + random.randint(1, 100))}
        a = requests.get(url, headers=headers)
        counter += 1
    if counter == 50:
        failed.append(pagenum)
        thread.exit()
    data = a.content
    soup = BeautifulSoup.BeautifulSoup(data)
    lst = [i.get('href') for i in soup.findAll('a', {'class': 'view_img_link'})]
    if not os.path.exists('jianbing'):
        os.mkdir('jianbing')
    for i in range(len(lst)):
        get_img(pagenum, i, lst[i])
    print 'Page %d finished' % pagenum, time.time() - time3
    finished += 1
    active -= 1
    thread.exit()


def get_img(pagenum, i, url):
    f = open('jianbing/%d_%d.jpg' % (pagenum, i + 1), 'w')
    data = requests.get(url).content
    f.write(data)
    f.close()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.%d.90 Safari/537.36" % (
        random.randint(2300, 2400))}
time1 = time.time()
time2 = time.time()
start_page = raw_input('Start page(optional):')
end_page = raw_input('End page(optional):')
if not start_page:
    start_page = 1
else:
    start_page = int(start_page)
if not end_page:
    end_page = get_totalpage()
    print 'total page = %d' % end_page, time2 - time1
else:
    end_page = int(end_page)
finished = 0
active = 0
failed = []
for i in xrange(start_page, end_page + 1):
    print '\nGetting Page %d' % i
    if i != start_page:
        time_left = float(time.time() - time2) / (i - start_page) * (end_page - i + 1)
        print 'Expected finished time:' + time.strftime('%H:%M:%S', time.localtime(time.time() + time_left))
    active += 1
    thread.start_new_thread(load_page, (i,))
    print 'active', active
    while active > 5:
        pass
while active != 0:
    pass
raw_input('All finished! Press ENTER to exit\n')
