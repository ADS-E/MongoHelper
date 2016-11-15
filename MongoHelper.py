__author__ = 'Sasa2905'
import pymongo
from pymongo import MongoClient
from urllib.request import urlopen

client = MongoClient("mongodb://145.93.174.51:27017/")
db = client["webshops"]
collection = client["information"]
posts = db.information

def insertURLInfo(url, content, webshop, inscope, category, meta, address, year):
    post = {"URL":url, "content":content,"webshop":webshop, "inscope": inscope, "category": category, "meta": meta,
            "address":address, "year": year}
    try:
        posts.insert_one(post)
    except:
        print("Failed, server error")

def getResultByURL(url):
     return posts.find_one({"URL": url})

url = "http://www.bol.com"
f = urlopen(url)
html =  f.read()
webshop = True
inscope = True
category = "Electronics"
meta = "jfreifje fkerkfe"
address = "Pietjelaan 25"
year = "2016"
insertURLInfo(url,html,webshop,inscope,category,meta,address,year)
print(getResultByURL(url))
