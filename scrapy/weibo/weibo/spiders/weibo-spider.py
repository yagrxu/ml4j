#encoding=utf-8
import scrapy
import weibo.items as items
import json
import time 
from scrapy import log

class TouTiaoSpider(scrapy.Spider):

    name = 'toutiao'
    allowed_domains = ["toutiao.com"]
    start_urls = [
    'http://toutiao.com/articles_news_society/p1'
    ]
    base_class_url = 'http://toutiao.com/articles_news_society'
    base_url = 'http://toutiao.com'
#maxpage = 501;#允许爬的最大的页数
    maxpage = 5;#允许爬的最大的页数
    category = ['articles_news_society','articles_news_entertainment',
    'articles_movie','articles_news_tech','articles_digital',
    'articels_news_sports','articles_news_finance','articles_news_military',
    'articles_news_culture','articles_science_all'
    ]

#请求每一个分类,按页数来
    def parse(self,response):
        log.msg("Yagr In", log.INFO)
        for ctg in self.category:
            log.msg(ctg, log.INFO)
            for page in range(0,self.maxpage):
                url = self.base_url+'/'+ctg+'/p'+str(page)
                yield scrapy.Request(url,self.parseNewsHref)

#解析每页新闻列表的地址
    def parseNewsHref(self,response):
        urls = response.xpath("//div[@class='info']//a/@href").extract()
        log.msg("Yagr In 2", log.INFO)
        for url in urls:
            log.msg(url, log.INFO)
            news_url = self.base_url+url
            yield scrapy.Request(news_url,self.parseNews)

#解析具体新闻内容 
    def parseNews(self,response):
        articles = response.xpath("//div[@id='pagelet-article']")
        item = items.WeiboItem()
        title = articles.xpath("//div[@class='article-header']/h1/text()").extract()[0]
        log.msg(title, log.INFO)
        tm = articles.xpath("//div[@id='pagelet-article']//span[@class='time']/text()").extract()[0]
        log.msg(tm, log.INFO)
        content = articles.xpath("//div[@class='article-content']//p/text()").extract()
        log.msg(content, log.INFO)

        if(len(title)!=0 and len(tm)!=0 and len(content)!=0):
            item['title'] = title
            item['time'] = int(time.mktime(time.strptime(tm,'%Y-%m-%d %H:%M')))
            item['url'] = response.url
            cc=''
            if(len(content) != 0):
                for c in content:
                    cc = cc+c+'\n'
                item['content'] = cc
                yield item
