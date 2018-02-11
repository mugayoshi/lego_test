# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'brickset'
    allowed_domains = ['brickset.com']
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        pass
