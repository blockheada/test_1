import re

from flask import Flask,render_template


import pymongo
app = Flask(__name__)

import pandas as pd

@app.route('/')
def hello_world():
    return render_template("temp.html")

# 首页
@app.route("/index")
def index():
    # return render_template("temp.html")
    return hello_world()

@app.route('/movie')
def movie():
    datalist = []
    client = pymongo.MongoClient()
    db = client['bishe4']
    result = db['top250'].find()
    for i in result:
        datalist.append(list(i.values()))
    return render_template("movie.html",movies = datalist)

@app.route('/score')
def score():
    client = pymongo.MongoClient()
    db = client['bishe4']
    table = db['top250']
    data = pd.DataFrame(list(table.find()))
    score = data.movie_score
    score_list = score.values.tolist()
    scores = ['8.3', '8.4', '8.5', '8.6', '8.7', '8.8','8.9', '9.0', '9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '9.7']
    numbers = []
    for i in range(0, 15):
        scores = 8.3 + i * 0.1
        numbers.append(score_list.count(str(format(scores, '.1f'))))
    return render_template("scroe.html",scores =scores,numbers =numbers)

@app.route('/top9')
def top():
    client = pymongo.MongoClient()
    db = client['bishe4']
    result = db['top250'].find({'movie_score': {'$gte': '9.5'}})
    name = []
    score = []
    for i in result:
        name.append(i['movie_name'])
        score.append((i['movie_score']))
    return render_template("top8.html",name = name,score = score)

@app.route('/type')
def type():
    # client = pymongo.MongoClient()
    # db = client['bishe4']
    # table = db['top250']
    # data = pd.DataFrame(list(table.find()))
    # type = data.movie_type
    # type_list = type.values.tolist()
    # types = list(set(type_list))
    # new_list = []
    # numbers = []
    # for elm in types:
    #     new_list.extend(elm.split("/"))
    # new_list = list(set(new_list))
    # for item in new_list:
    #     number = db['top250'].count({'movie_type': re.compile(item)})
    #     numbers.append(number)
    # return render_template("type.html",new_list = new_list,numbers = numbers)
    client = pymongo.MongoClient()
    db = client['bishe4']
    type = ['剧情', '爱情', '喜剧', '冒险', '犯罪', '奇幻', '动画', '惊悚', '动作',
            '悬疑', '家庭', '战争', '传记', '古装', '音乐', '历史', '同性', '歌舞', '儿童', '武侠',
            '纪录片', '恐怖', '灾难', '情色', '运动']
    type = [type[len(type) - i - 1] for i in range(len(type))]
    numbers = []
    for item in type:
        result = db['top250'].count({'movie_type': re.compile(item)})
        numbers.append(result)
    return render_template("type.html",numbers = numbers)


@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/country')
def country():
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
        if number >= 10:
            country_name.append(item)
            numbers.append(number)
        elif number > 3:
            country_name1.append(item)
            numbers1.append(number)
        else:
            number_sum = number_sum + number
    country_name1.append("其他")
    numbers1.append(number_sum)
    datas = []
    for i, j in zip(numbers, country_name):
        mydict = {}
        mydict["value"] = int(i)
        mydict["name"] = str(j)
        datas.append(mydict)
    datas1 = []
    for a, b in zip(numbers1, country_name1):
        mydict1 = {}
        mydict1["value"] = int(a)
        mydict1["name"] = str(b)
        datas1.append(mydict1)
    country_name = country_name + country_name1
    return render_template("country.html" ,country_name = country_name,datas1 = datas1,datas = datas)

@app.route('/date')
def date():
    client = pymongo.MongoClient()
    db = client['bishe4']
    table = db['top250']
    data = pd.DataFrame(list(table.find()))
    date = data.movie_data
    date_list = date.values.tolist()
    dates = list(set(date_list))
    dates.sort()
    numbers = []
    for item in dates:
        numbers.append(date_list.count(str(format(item))))
    return render_template("date.html", dates=dates, numbers=numbers)



if __name__ == '__main__':
    app.run()
