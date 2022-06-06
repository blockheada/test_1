
import pymongo
class DoubanmoviesPipeline:
    # 初始化mongodb
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.col = self.client['bishe4']
        self.top250 = self.col.top250


    def process_item(self, item, spider):
        res = dict(item)
        self.top250.insert_one(res)
        return item


    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.client.close()



