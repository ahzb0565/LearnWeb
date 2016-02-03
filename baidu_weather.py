# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Use baidu API to get weather

import sys, urllib, urllib2, json
"""
url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname=%E6%9C%9D%E9%98%B3'

req = urllib2.Request(url)

req.add_header("apikey", "your apikey")

resp = urllib2.urlopen(req)
content = resp.read()
if(content):
    print(content)
"""

class Weather(object):
    API_CITYLIST_URL = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname='
    API_CITYINFO_URL = ' http://apis.baidu.com/apistore/weatherservice/cityinfo'
    API_CITYID_URL = 'http://apis.baidu.com/apistore/weatherservice/cityid?cityid='
    API_KEY = '5ab7ee113dea3a1ee5c865e4d2378cb1'
    def __init__(self):
        self.__api_citylist_url = self.API_CITYLIST_URL
        self.__api_cityinfo_url = self.API_CITYINFO_URL
        self.__api_key = self.API_KEY

    def __build_request(self, url, *args, **kws):
        req = urllib2.Request(url, *args, **kws)
        req.add_header('apikey', self.__api_key)
        return req

    def __do_open(self, req, *args, **kws):
        resp = urllib2.urlopen(req, *args, **kws)
        content = json.loads(resp.read().decode('utf8'))
        return self.__handler_response(content)

    def __handler_response(self, resp):
        if resp['errNum'] != 0:
            print resp['errMsg']
            raise Exception("Get city info failed.")
        else:
            return resp['retData']

    def get_city_list(self, city):
        city = urllib.quote(city)
        url = "%s%s"%(self.__api_citylist_url,city)
        req = self.__build_request(url)
        return self.__do_open(req)

    def get_weather_by_id(self, id):
        url = '%s%d'%(self.API_CITYID_URL,id)
        req = self.__build_request(url)
        return self.__do_open(req)

    def get_weather(self, city):
        city_list = self.get_city_list(city)
        for city in city_list:
            province_cn = city['province_cn'].encode('utf8')
            district_cn = city['district_cn'].encode('utf8')
            name_cn = city['name_cn'].encode('utf8')
            print '%s-%s-%s'%(str(province_cn), str(district_cn), str(name_cn))
            id = int(city['area_id'])
            weather = self.get_weather_by_id(id)
            print weather

def main():
    city = '郎溪'
    w = Weather()
    print w.get_weather(city)
main()