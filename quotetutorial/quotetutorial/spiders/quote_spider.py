# -*- coding: utf-8 -*-
import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote_spider'
    start_urls = ["http://quotes.toscrape.com/"]
    
    
    def parse(self, response):
        all_divs = response.css('div.quote')
        for div in all_divs:
            title = div.css("span.text::text").extract()
            author =div.css(".author::text").extract()
            tags = div.css(".tag::text").extract()
            yield {'title': title, 'author': author, 'tags': tags }