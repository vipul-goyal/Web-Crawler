from scrapy.spiders import Spider
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from pathlib import Path
import os
import json
import scrapy


class MySpider1(Spider):
    name = "spider1"
    allowed_domains = ["http://www.rigzone.com"]
    start_urls = ["http://www.rigzone.com"]
    urls=[]
    output=[]
    i=0
    
    def parse(self, response):
        #parse any elements you need from the start_urls and, optionally, store them as Items.
        
        s = Selector(response)
        MySpider1.urls = s.css('div.rz-fts-section>a::attr(href)').extract()
        for url in MySpider1.urls:
            url=response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_following_urls,dont_filter=True)
            


    def parse_following_urls(self, response):
        url=MySpider1.urls[MySpider1.i]
        url=response.urljoin(url)
        All_text=response.css("div>p::text").extract()
        MySpider1.output.append({'url':url,'All_text': All_text})
        yield{
            'url' :url,         
             'All_text':All_text 
        }
        MySpider1.i+=1
    
class MySpider2(Spider):
    name = "spider2"
    allowed_domains = ["http://www.offshoreenergytoday.com"]
    start_urls = ["http://www.offshoreenergytoday.com"]
    urls=[]
    i=0
    
    def parse(self, response):
        #parse any elements you need from the start_urls and, optionally, store them as Items.
      
        s = Selector(response)
        MySpider2.urls = s.css('#newscarousel a::attr(href) , .block-news a::attr(href)').extract()
        for url in MySpider2.urls:
            url=response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_following_urls,dont_filter=True)    



    def parse_following_urls(self, response):
        url=MySpider2.urls[MySpider2.i]
        url=response.urljoin(url)
        All_text=response.css("l.content p::text,strong::text").extract()
        MySpider1.output.append({'url':url,'All_text': All_text})
        yield{
             'url' :url,         
             'All_text':All_text             
        }
        MySpider2.i+=1
        
        
class MySpider3(Spider):
    name = "spider3"
    allowed_domains = ["http://www.worldoil.com"]
    start_urls = ["http://www.worldoil.com"]
    urls=[]
    i=0
    
    def parse(self, response):
        #parse any elements you need from the start_urls and, optionally, store them as Items.
      
        s = Selector(response)
        MySpider3.urls = s.css('div.col-sm-6>ul>li>a::attr(href)').extract()
        for url in MySpider3.urls:
            url=response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_following_urls,dont_filter=True)
            



    def parse_following_urls(self, response):
        url=MySpider3.urls[MySpider3.i]
        url=response.urljoin(url)
        All_text=response.css("div>p::text").extract()
        MySpider1.output.append({'url':url,'All_text': All_text})
        yield{
             'url' :url,         
             'All_text':All_text            
        }
        MySpider3.i+=1
        
class MySpider4(Spider):
    name = "spider4"
    allowed_domains = ["http://www.pennenergy.com"]
    start_urls = ["http://www.pennenergy.com"]
    urls=[]
    i=0
    
    def parse(self, response):
        #parse any elements you need from the start_urls and, optionally, store them as Items.
      
        s = Selector(response)
        MySpider4.urls = s.css('a::attr(href)').extract()
        for url in MySpider4.urls:
            url=response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_following_urls,dont_filter=True)
            


    def parse_following_urls(self, response):
        url=MySpider4.urls[MySpider4.i]
        url=response.urljoin(url)
        All_text=response.css("p::text").extract()
        MySpider1.output.append({'url':url,'All_text': All_text})
        yield{
             'url' :url,         
             'All_text':All_text            
        }
        MySpider4.i+=1        
        
class MySpider5(Spider):
    name = "spider5"
    allowed_domains = ["http://www.gasprocessingnews.com"]
    start_urls = ["http://www.gasprocessingnews.com"]
    urls=[]
    i=0
    
    def parse(self, response):
        #parse any elements you need from the start_urls and, optionally, store them as Items.
      
        s = Selector(response)
        MySpider5.urls = s.css('a::attr(href)').extract()
        for url in MySpider5.urls:
            url=response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_following_urls,dont_filter=True)
            


    def parse_following_urls(self, response):
        url=MySpider5.urls[MySpider5.i]
        url=response.urljoin(url)
        All_text=response.css("#content-left p::text").extract()
        MySpider1.output.append({'url':url,'All_text': All_text})
        yield{
             'url' :url,         
             'All_text':All_text            
        }
        MySpider5.i+=1        
        
        
configure_logging()
runner = CrawlerRunner()
runner.crawl(MySpider1)
runner.crawl(MySpider2)
runner.crawl(MySpider3)
runner.crawl(MySpider4)
runner.crawl(MySpider5)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
my_file = Path("news.json")
if my_file.exists():
    os.remove('news.json')
with open('news.json', 'a') as outfile:
    json.dump(MySpider1.output, outfile)