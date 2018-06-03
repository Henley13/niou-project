# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["http://www.marmiton.org/"]
    start_urls = ['http://www.marmiton.org/recettes/recherche.aspx?aqt=plat']

    def parse(self, response):
        filename = 'example.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        return
