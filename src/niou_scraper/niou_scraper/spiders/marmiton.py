# -*- coding: utf-8 -*-
import scrapy


class MarmitonSpider(scrapy.Spider):
    name = "marmiton"
    allowed_domains = ["http://www.marmiton.org/"]
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
