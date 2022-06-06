
from wordcloud import WordCloud
import pymongo
client = pymongo.MongoClient()
db = client['bishe4']
result = db['top250'].find()
dict_in = {}
for i in result:
    dict_in[i['movie_name']] = int(i['movie_num'])

wc = WordCloud(font_path='C:/Windows/Fonts/STXINGKA.TTF',background_color='white',
                      width=4000,height=4080)

wc.generate_from_frequencies(dict_in)
wc.to_file(r'static/assets/img/word11.jpg')


