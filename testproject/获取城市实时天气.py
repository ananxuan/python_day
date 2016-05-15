import urllib
import urllib.request as urllib2
import urllib.parse
import json



def post_curl_keystone():
    url = 'http://service.envicloud.cn:8082/api/getWeatherCurrent'
    values = {"citycode":"B3DHC3AXNDYZMTK4MDGZMDE5","accessId":"101280601"}
    # params = json.dumps(values)
    params = urllib.parse.urlencode(values).encode(encoding='utf-8')
    print(params)
    # headers = {"Content-type":"application/json","Accept": "application/json"}
    headers = {"Accept": "application/json"}
    req = urllib2.Request(url, params, headers)
    response = urllib2.urlopen(req)
    print(response.read())
# post_curl_keystone()

def get_curl_keystone():
    header_dict={'User-Agent':\
           'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}


    # url = 'http://service.envicloud.cn:8082/api/getWeatherCurrent'
    url  ="http://service.envicloud.cn:8082/api/getWeatherCurrent?citycode=101280601&ak=B3DHC3AXNDYZMTK4MDGZMDE5"
    values = urllib.parse.urlencode({"ak":"B3DHC3AXNDYZMTK4MDGZMDE5","citycode":"101280601"}).encode(encoding='utf-8')
    print(values)
    # params = json.dumps(values)
    # headers = {"Content-type":"application/json","Accept": "application/json"}
    # req = urllib2.Request(url)
    response = urllib2.urlopen(url,data=values)
    print(response.read())
get_curl_keystone()