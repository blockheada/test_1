import re
import pymongo
import pandas as pd
# 上映（1）
# client = pymongo.MongoClient()
# db = client['douban_top250']
# table = db['Top250']
# data = pd.DataFrame(list(table.find()))
# date = data.movie_date
# date_list = date.values.tolist()
# dates = list(set(date_list))
# dates.sort()
# numbers = []
# for item in dates:
#     numbers.append(date_list.count(str(format(item))))
# print(numbers)



# 国家（1）
client = pymongo.MongoClient()
db = client['bishe4']
table = db['top250']
data = pd.DataFrame(list(table.find()))
country = data.movie_country
country_list = country.values.tolist()
countrys = list(set(country_list))
new_list = []
numbers = []
country_name = []
country_name1 = []
numbers1 = []
for elm in countrys:
    new_list.extend(elm.split(" / "))
new_list = list(set(new_list))
number_sum = 0
for item in new_list:
    number = db['top250'].count({'movie_country': re.compile(item)})
    if number>=10:
        country_name.append(item)
        numbers.append(number)
    elif number > 5:
        country_name1.append(item)
        numbers1.append(number)
    else:
        number_sum = number_sum + number
country_name1.append("其他")
numbers1.append(number_sum)
datas = []
for i,j in zip(numbers,country_name):
    mydict = {}
    mydict["value"] = int(i)
    mydict["name"] = str(j)
    datas.append(mydict)
datas1 = []
for a,b in zip(numbers1,country_name1):
    mydict1 = {}
    mydict1["value"] = int(a)
    mydict1["name"] = str(b)
    datas1.append(mydict1)
country_name = country_name+country_name1
print(datas)
print(datas1)
print(country_name)










# 转换成字符串计算数量
# str1 = str(country_list)
# print(str1.count('美国'))

# 列表元素拆分
# .split()主要是用于对一个字符串进行分割成多个字符串数组
# my_list = ['my_label2 new_label2 my_label', 'label_test1 label_test2 label_test3', 'my_label2 new_label2 my_label']
# new_list=[]
# for elm in my_list:
#     new_list.extend(elm.split("/"))
# print(new_list)

# 列表选择符合长度的字符串
# countrys=[]
# ln = list(filter(lambda s:isinstance(s,str) and len(s) == 2,countrys))
# print(ln)

# 国家（2）
# client = pymongo.MongoClient()
# db = client['bishe4']
# country = ['中国', '日本', '印度', '法国', '韩国', '德国', '美国', '英国','意大利']
# numbers= []
# for item in country:
#     result = db['top250'].count({'movie_country':re.compile(item)})
#     numbers.append(result)
# print(numbers)


# 类型(1)
# client = pymongo.MongoClient()
# db = client['bishe4']
# type = ['剧情', '爱情', '喜剧', '冒险', '犯罪', '奇幻', '动画', '惊悚', '动作',
#         '悬疑','家庭','战争','传记','古装','音乐','历史','同性','歌舞','儿童','武侠',
#         '纪录片','恐怖','灾难','情色','运动']
# type = [type[len(type)-i-1] for i in range(len(type))]
# print(type)
# numbers= []
# for item in type:
#     result = db['top250'].count({'movie_type':re.compile(item)})
#     numbers.append(result)
# print(numbers)

# 类型2(1)
# client = pymongo.MongoClient()
# db = client['bishe4']
# table = db['top250']
# data = pd.DataFrame(list(table.find()))
# type = data.movie_type
# type_list = type.values.tolist()
# types = list(set(type_list))
# new_list=[]
# numbers = []
# for elm in types:
#     new_list.extend(elm.split("/"))
# new_list = list(set(new_list))
# for item in new_list:
#     number = db['top250'].count({'movie_type': re.compile(item)})
#     numbers.append(number)
# print(new_list)
# print(numbers)

