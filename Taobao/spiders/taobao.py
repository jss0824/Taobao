# -*- coding: utf-8 -*-
import scrapy
from Taobao.get_cookie import LoginTaoBao
from scrapy.http import Request,FormRequest
import time
import re
import json
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    # allowed_domains = ['www.taobao.com']
    # start_urls = ['https://dell.tmall.com/search.htm?spm=a1z10.3-b-s.w4011-14717277032.260.32cc2670XP1svZ&search=y&orderType=hotsell_desc&viewType=grid&lowPrice=10&scene=taobao_shop&pageNo=1&tsearch=y#anchor']
    def start_requests(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print(ts)
        url = 'https://s.taobao.com/search?q=%E6%88%B4%E5%B0%94&initiative_id=staobaoz_20200323&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=0'
        # url = 'https://s.taobao.com/search?data-key=s&data-value=44&ajax=true&_ksTS={}_2023&callback=jsonp2024&q=%E6%88%B4%E5%B0%94&initiative_id=staobaoz_20200323&ie=utf8&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&s=0'.format(ts)
        print(url)
        # cookie = LoginTaoBao().log()
        # print(cookie)
        cookie = {'x': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0', 'thw': 'cn', 'hng': 'CN%7Czh-CN%7CCNY%7C156', 'UM_distinctid': '16dedb6e4315bf-0570a50a09a925-e343166-1fa400-16dedb6e43279a', 't': 'ddfbf9e1821a599beab74786b4fadb05', '_m_h5_tk': 'c861ed63ba4becf367d785a9882c03fb_1584612398381', '_m_h5_tk_enc': 'ea51611fc8f47d0503f7ceb17d1094f5', 'cna': '4BJsFi1P7RUCAXvEC6I3DD9I', 'enc': 'T8ih5DzVwwXiRQv1qhIsQdc0y1q5emWWdTYqTeoDNSKNpxY53t12yJHaQgqu749i8rwo9Fpvu2ZcC6513beVlQ%3D%3D', 'sgcookie': 'E%2F1%2B6HAwzWHydHwwvF7b1', 'uc3': 'nk2=1rQRXbulApU%3D&lg2=W5iHLLyFOGW7aA%3D%3D&vt3=F8dBxd9kq6J6iW07g6A%3D&id2=VAKMd4fpjh7G', 'lgc': '%5Cu8776%5Cu821E%5Cu98CE%5Cu6F47', 'uc4': 'id4=0%40VhvAhRvxDXGpsHeKm3kEayz0iAs%3D&nk4=0%401AVyc9eZ0fHE6xQ72%2BBqNijEZA%3D%3D', 'tracknick': '%5Cu8776%5Cu821E%5Cu98CE%5Cu6F47', '_cc_': 'U%2BGCWk%2F7og%3D%3D', 'tg': '0', 'tfstk': 'coZCBAAw1BAQKJDB8z6Z4h7T00i5ZnpjFwG3dPMmfaHHKxwCimKqGDX4rQKtkA1..', 'mt': 'ci=20_1', 'v': '0', 'cookie2': '5b42156697d899cb8530db62a9ff132e', '_tb_token_': 'e31137be68653', 'uc1': 'cookie14=UoTUPvnayHSLWw%3D%3D', 'JSESSIONID': '2FB64F3C4BC83BFA1E57407D59138044', 'l': 'dBxtlIEVQ1891CB6BOfi5JmH9kQtnKRf5sPr-0SSMIB1tTWKIdkvoHwE4ZqW63QQEtfAbetPgrrGARhH5fzLRxgKqelyRs5mp9p6y', 'isg': 'BI6ORGlpXIGq3-iuzPIsFKmX32RQD1IJmyNOZ7jffBX-Gyd1IJ3SGdidU0d3A0oh'}



        headers = {
        'authority': 's.taobao.com',
        'method': 'GET',
        'path': '/search?data-key=s&data-value=44&ajax=true&_ksTS=1584938652417_2023&callback=jsonp2024&q=%E6%88%B4%E5%B0%94&initiative_id=staobaoz_20200323&ie=utf8&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48&s=0',
        'scheme': 'https',
        # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cache-control': 'no-cache',
        # 'pragma': 'no-cache',
        # 'cookie':cookie,
        # 'referer': 'https://s.taobao.com/search?q=%E6%88%B4%E5%B0%94&initiative_id=staobaoz_20200323&ie=utf8&bcoffset=-1&ntoffset=-1&p4ppushleft=1%2C48&s=176',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
        print(headers)
        yield Request(url, callback=self.parse, meta={
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]}, cookies=cookie)
    def parse(self, response):
        content = str(response.text)
        print(content)
        g_page = ('').join(re.findall('g_page_config = (.*);', content))
        content_json = json.loads(g_page)
        print(content_json)
