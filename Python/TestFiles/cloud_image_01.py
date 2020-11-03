from wordcloud import WordCloud
from imageio import imread
from sklearn.feature_extraction.text import CountVectorizer
import jieba
import csv

with open('./dict.txt') as f:
    contents = f.read()
#print(contents)
contents_cut = jieba.cut(contents)
contents_list = " ".join(contents_cut)
wc = WordCloud(collocations=False, 
               background_color="white",
               font_path="/System/Library/Fonts/Keyboard.ttf",
               mask=imread('QR.png'),
               width=1280, height=720, random_state=42)
wc.generate(contents_list)
wc.to_file("ciyun.png")