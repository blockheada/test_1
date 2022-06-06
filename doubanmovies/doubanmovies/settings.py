
BOT_NAME = 'doubanmovies'

SPIDER_MODULES = ['doubanmovies.spiders']
NEWSPIDER_MODULE = 'doubanmovies.spiders'
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}


ITEM_PIPELINES = {
   'doubanmovies.pipelines.DoubanmoviesPipeline': 300,
}


