import scrapy
from scrapy.spiders import Spider
class QuotesSpider(scrapy.Spider):
    spider_name = "quotes"
    
    def start_request(self):
        
        url = ["https://quotes.toscrape.com/page/1/",
              "https://quotes.toscrape.com/page/2/",
              ]
        #Generate Function
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
            
    def parse(self,response):
        page_id = response.url.split("/")[-2]
        filename = "quotes-%s"%page_id
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)    