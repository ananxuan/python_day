# -*- coding:utf-8 -*-
"""
多线程抓取网页
"""
# import mul
import gzip
from urllib import request as urllib2

import threading

from pyquery import PyQuery as pq

threads = []
web_site_url = "http://www.oschina.net/question/tag/python"  # OS CHINA 下python标签

def work(url):
    """
    callback function
    """
    # 出现urllib2.HTTPError: HTTP Error 403: Forbidden错误是由于网站禁止爬虫，可以在请求加上头信息，伪装成浏览器访问
    # 伪装浏览器头
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    if not url:
        url = web_site_url
    req = urllib2.Request(url=url, headers = headers)
    feed_data = urllib2.urlopen(req).read()
    feed_data = gzip_decode_content(feed_data)
    data = pq(feed_data)
    get_next_page(data)
    if data :
        data("ul li.question").each(parse_html)


def parse_html(i, element ):
    pq_element = pq(element)
    user_img = pq_element("a.ShowUserOutline img").attr("src")
    # user_name = pq_element("a.ShowUserOutline img").attr("title")
    question = pq_element("div.qbody h2 a").text()
    date_str = pq_element("div.qbody div.Date").text()
    date_str = date_str.split("，")[0].strip()
    print("%s\t%s\t%s" % (question, date_str, user_img))

def get_next_page(data):
    if data :
        page_li = data("ul.pager").eq(1).find("li.next")
        if page_li :
            page_params = page_li.find("a").attr("href")
            next_page_url = web_site_url + page_params
            threading.Thread(target=work, args=(next_page_url, )).start()


def gzip_decode_content(doc=""):
    """
    根据URL返回内容，有些页面可能需要 gzip 解压缩
    """

    try:
        html = gzip.decompress(doc).decode("utf-8") #解码
    except:
        html=doc.decode("utf-8")
    return html


def main():
    work(())

if __name__ == "__main__":
    main()


# import urllib.request
#
# url = "http://www.oschina.net/"
# headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
#
# opener = urllib.request.build_opener()
# opener.addheaders = [headers]
# data = opener.open(url).read()
#
# print(data)