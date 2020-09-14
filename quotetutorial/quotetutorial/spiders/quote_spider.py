# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote_spider'
    start_urls = ["http://quotes.toscrape.com/"]
    
    
    def parse(self, response):
        title = response.css('title').extract()
        yield {'title_text':title}