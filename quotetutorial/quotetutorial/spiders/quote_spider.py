# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote_spider'
    start_urls = ["http://quotes.toscrape.com/"]
    
    
    def parse(self, response):
        all_divs = response.css('div.quote')
        title = all_divs.css("span.text::text").extract()
        author =all_divs.css(".author::text").extract()
        tags = all_divs.css(".tag::text").extract()
        yield {'title': title, 'author': author, 'tags': tags }