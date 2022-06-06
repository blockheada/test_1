# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from doubanmovies.items import DoubanmoviesItem
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ["https://movie.douban.com/top250"]
    # step_time = 5
    page_number = 0

    def parse(self, response):
        node_list = response.xpath('//ol[@class="grid_view"]/li/div[@class="item"]')
        for msg in node_list:
            # 排名
            movie_rank = msg.xpath('./div[@class="pic"]/em/text()').extract()
            movie_rank = ''.join(movie_rank)

            # 详情链接
            details_url = msg.xpath('./div[@class="info"]/div[@class="hd"]/a/@href').extract()

            # 链接部分
            url = msg.xpath('./div[@class="info"]/div[@class="hd"]/a/@href').extract()
            url = ''.join(url)

            # 名称
            movie_name = msg.xpath('./div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract()
            movie_name = ''.join(movie_name)

            # 评论人数
            movie_num = msg.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()
            movie_num = str(movie_num)[2:-5]
            movie_num = ''.join(movie_num)

            # 评分
            movie_score = msg.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@property="v:average"]/text()').extract()
            movie_score = ''.join(movie_score)

            # 中心主题
            movie_purpose = msg.xpath('./div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            movie_purpose = ''.join(movie_purpose)

            # 使用管道保存，管道可以对键值自动去重
            item = DoubanmoviesItem()
            item['movie_rank'] = movie_rank
            item["movie_url"] = details_url
            item["movie_name"] = movie_name
            item["movie_num"] = movie_num
            item["movie_score"] = movie_score
            item["movie_purpose"] = movie_purpose
            item["url"] = url

            # time.sleep(self.step_time)
            yield Request(details_url[0], callback=self.get_details, meta={"info": item})

        # 有序内容获取方法
        self.page_number += 1
        print(self.page_number)
        # 爬取其他页面
        if (self.page_number < 10):
            # time.sleep(3)
            page_url = 'https://movie.douban.com/top250?start={}&filter='.format(self.page_number * 25)
            yield scrapy.Request(page_url, callback=self.parse)

    # 获取详情页数据
    def get_details(self, response):
        item = DoubanmoviesItem()
        info = response.meta["info"]
        item.update(info)

        # 上映年份
        movie_data = response.xpath('//h1/span[@class="year"]/text()').extract()
        movie_data = ''.join(movie_data)
        movie_data = movie_data.replace('(', ' ').replace(')', '')

        response = response.xpath('//div[@id="info"]')

        # 导演列表
        movie_director = response.xpath('./span[1]/span[@class="attrs"]/a/text()').extract()
        movie_director = ''.join(movie_director)

        # 主演列表
        movie_actor = response.xpath('string(./span[@class="actor"]/span[@class="attrs"])').extract()
        movie_actor = '/'.join(movie_actor)

        # 上映时间
        # movie_data = response.xpath('./span[@property="v:initialReleaseDate"]/text()').extract_first()
        # movie_data = ''.join(movie_data)

        # 制片国
        movie_country = str(response.extract())
        movie_country = movie_country[movie_country.index("制片国"):movie_country.index("语言")].strip()
        movie_country = movie_country[movie_country.index("</span>") + 7:movie_country.index("<br>")].strip()

        # 语言
        movie_languages = str(response.extract())
        movie_languages = movie_languages[movie_languages.index("语言"):movie_languages.index("上映")].strip()
        movie_languages = movie_languages[movie_languages.index("</span>") + 7:movie_languages.index("<br>")].strip()

        # 片长
        movie_times = response.xpath('./span[@property="v:runtime"]/text()').extract()
        movie_times = ''.join(movie_times)

        # 类型
        movie_type = response.xpath('./span[@property="v:genre"]/text()').extract()
        movie_type = '/'.join(movie_type)

        item["movie_director"] = movie_director
        item["movie_actor"] = movie_actor
        item["movie_data"] = movie_data
        item["movie_country"] = movie_country
        item["movie_languages"] = movie_languages
        item["movie_times"] = movie_times
        item["movie_type"] = movie_type

        yield item




