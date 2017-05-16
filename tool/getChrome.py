'''
    爬取Chrome下载地址
'''

import urllib.request
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

'''
from tool import proxy

def getProxy():
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    ip_list = proxy.get_ip_list(url, headers=headers)
    proxies = proxy.get_random_ip(ip_list)
    return proxies
'''
class getUrl():
    # 网址
    url = "https://api.shuax.com/tools/getchrome"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


    #获取代理IP
    #proxies = getProxy()
    #print(proxies)

    #proxy_handler = urllib.request.ProxyHandler(proxies)
    #opener = urllib.request.build_opener(proxy_handler)
    #urllib.request.install_opener(opener)



    # 请求
    request = urllib.request.Request(url=url, headers=headers)

    # 爬取结果
    response = urllib.request.urlopen(request, timeout=5)

    data = response.read()

    # 设置解码方式
    data = data.decode('utf-8')

    # 打印结果
    # print(data)

    # 打印爬取网页的各类信息
    # print(type(response))
    # print(response.geturl())
    # print(response.info())
    # print(response.getcode())

    # 分析网页
    soup = BeautifulSoup(data, "html.parser")

    # print(soup.prettify())
    # print(soup.find_all('a'))
    # print(soup.find_all('a')[10]['href'])

    def __init__(self,verChosen, bitChosen, v_ver,v_size,v_time,text_url):
        self.releaseversion = verChosen
        self.bitnum = bitChosen
        self.v_ver = v_ver
        self.v_size = v_size
        self.v_time = v_time
        self.texturl = text_url

    def getinfo(self):

        #'稳定版','测试版','开发版','金丝雀版'
        if self.releaseversion == '稳定版':
            classname = "bs-callout bs-callout-success"
        elif self.releaseversion == '测试版':
            classname = "bs-callout bs-callout-info"
        elif self.releaseversion == '开发版':
            classname = "bs-callout bs-callout-warning"
        elif self.releaseversion == '金丝雀版':
            classname = "bs-callout bs-callout-danger"
        else:
            classname = "bs-callout bs-callout-success"

        #'32位','64位'
        if self.bitnum == '32位':
            verbit = 0
        elif self.bitnum == '64位':
            verbit = 1
        else:
            verbit = 0

        content = self.soup.find_all("div", {"class", classname})[verbit]
        #print(content)
        #print(content.h4.text+"：")
        #print(content.p.text)
        #print(content.find_all('p')[2].text)

        #获取版本信息
        #verinfo = content.p.text
        verinfo = content.find_all('p')[0].text
        ver = verinfo.split('，')[0].replace('最新版本：','')
        #print('最新版本：' + ver)
        self.v_ver['text'] = ver
        size = verinfo.split('，')[1].replace('文件大小：','')
        #print('文件大小：' + size)
        self.v_size['text'] = size
        time = verinfo.split('，')[2].replace('查询时间：','')
        #print('查询时间：' + time)
        self.v_time['text'] = time

        #获取下载地址
        downlink = content.find('blockquote').find_all('a')
        #print(downlink)
        #print(len(downlink))

        #清除文本框
        self.texturl.delete(1.0,END)

        for i in range(0,len(downlink)):
            #print(downlink[i]['href'])
            self.texturl.insert(END,downlink[i]['href']+"\n")


def view():
    root = Tk()
    #root.withdraw()
    root.title('Chrome浏览器下载链接提取工具')
    width = 650
    height = 280
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)
    root.resizable(width=False, height=False)

    l_note = Label(root,text='在线查询Chrome版本')
    l_note.grid(row=0,sticky=W)

    l_release = Label(root,text='查询版本：')
    l_release.grid(row=1,sticky=W)

    rversion = StringVar()
    verChosen = ttk.Combobox(root,textvariable=rversion,width=10,state='readonly')
    verChosen['values'] = ('稳定版','测试版','开发版','金丝雀版')
    verChosen.grid(row=1,column=1,sticky=W)
    verChosen.current(0)

    rbit = StringVar()
    bitChosen = ttk.Combobox(root, textvariable=rbit, width=10,state='readonly')
    bitChosen['values'] = ('32位','64位')
    bitChosen.grid(row=1, column=2, sticky=W)
    bitChosen.current(0)

    l_ver = Label(root, text='最新版本：')
    l_ver.grid(row=2, sticky=W)
    v_ver = Label(root, text='')
    v_ver.grid(row=2,column=1,sticky=W)

    l_size = Label(root, text='文件大小：')
    l_size.grid(row=3, sticky=W)
    v_size = Label(root, text='')
    v_size.grid(row=3, column=1, sticky=W)

    l_time = Label(root, text='更新时间：')
    l_time.grid(row=4, sticky=W)
    v_time = Label(root, text='')
    v_time.grid(row=4, column=1, sticky=W)

    l_url = Label(root, text="下载地址：")
    l_url.grid(row=5,sticky=W)

    text_url = Text(root,width=90,height=6)
    text_url.grid(row=6, rowspan=5, columnspan=5, sticky=W, padx=10, pady=10)

    def query():
        getUrl(verChosen.get(), bitChosen.get(), v_ver, v_size, v_time, text_url).getinfo()

    b_query = Button(root, text="立刻查询", command=query)
    b_query.grid(row=1, column=3, sticky=W, padx=30)



    l_msg = Label(root, text='')
    #l_msg.grid(row=6)


    root.mainloop()

if __name__ == "__main__":
    #geturl = geturl(4,1)
    #geturl.getinfo()
    view()





