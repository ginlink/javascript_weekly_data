import scrapy
from scrapy.http import TextResponse


class WeekSpider(scrapy.Spider):
    name = "week"
    allowed_domains = ["javascriptweekly.com"]
    # start_urls = ["https://javascriptweekly.com"]

    def start_requests(self):
        week = 645
        yield scrapy.Request(url=f'https://javascriptweekly.com/issues/{week}')

    def parse(self, response: scrapy.http.response.Response):
        item = response.css('.el-item.item').getall()
        print(f'item: {item}')

        # print('打印数据：')
        # print(response)
        yield None
