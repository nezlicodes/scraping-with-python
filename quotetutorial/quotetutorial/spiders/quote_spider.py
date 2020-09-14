# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quote_spider'
    start_urls = ["http://quotes.toscrape.com/"]
    
    
    def parse(self, response):
        items = QuotetutorialItem()
        all_divs = response.css('div.quote')
        for div in all_divs:
            title = div.css("span.text::text").extract()
            author =div.css(".author::text").extract()
            tags = div.css(".tag::text").extract()
            
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items
            
        next_url = response.css("li.next a::attr(href)").get()
        if next_url is not None:
            yield response.follow(next_url, callback = self.parse)