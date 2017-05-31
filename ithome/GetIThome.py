import requests
from bs4 import BeautifulSoup

url = "http://www.ithome.com/ithome/getajaxdata.aspx?page=1&type=indexpage"
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3107.4 Safari/537.36' ,
            'Host':'www.ithome.com',
            'Referer': 'http://www.ithome.com/blog.htm'}

html = requests.get(url, headers = headers).content
soup = BeautifulSoup(html, "html.parser")

tags = soup.find_all("div",class_="block")

for tag in tags:
    article_title = tag.a.text
    article_url = tag.a['href']
    article_time0 = tag.span.text
    article_memo = tag.find('div',class_='memo').p.text
    print(article_title+"----"+article_url)

    #博客详情页
    bloghtml = requests.get(article_url, headers = headers).content
    blogsoup = BeautifulSoup(bloghtml, "html.parser")
    #print(blogsoup)

    article_time = blogsoup.find('span',id='pubtime_baidu').text
    print(article_time)
