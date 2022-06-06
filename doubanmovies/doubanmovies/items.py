

import scrapy


class DoubanmoviesItem(scrapy.Item):
    movie_rank = scrapy.Field()
    movie_url = scrapy.Field()
    movie_name = scrapy.Field()
    movie_num = scrapy.Field()
    movie_score = scrapy.Field()
    movie_purpose = scrapy.Field()
    movie_director = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_data = scrapy.Field()
    movie_country = scrapy.Field()
    movie_languages = scrapy.Field()
    movie_times = scrapy.Field()
    movie_type = scrapy.Field()
    url = scrapy.Field()



