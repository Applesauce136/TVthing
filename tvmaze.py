##TVmaze API
from flask import Flask, request, url_for, redirect, render_template

import urllib2
import json

tvmaze = Flask(__name__)

showSearchURL = "http://api.tvmaze.com/search/shows?q=%s"
showInfoURL =  "http://api.tvmaze.com/shows/%s"

## return list of lists of NAMES,id of top tv shows bases on search
def getShowSearch(query): 
    url = showSearchURL % (query)
    data = urllib2.urlopen(url).read()
    result = json.loads(data)
    list = []
    for s in result:
        try: 
            list2 = []
            list2.append(s["show"]["name"])
            list2.append(s["show"]["id"])
            list.append(list2)
        except: 
            pass
    return list


## return list of info for tv show by ID 
##id, name, network, summary, big picture url, little pic url
def getShowInfo(number): 
    url = showInfoURL % (number)
    data = urllib2.urlopen(url).read()
    result = json.loads(data)
    dict = {}
    dict["id"] = result["id"]
    dict["name"] = result["name"]
    dict["network"] = result["network"]["name"]
    dict["summary"] = result["summary"]
    dict["bigpicURL"] = result["image"]["original"]
    dict["smallpicURL"] = result["image"]["medium"]
    print dict
    return dict

@tvmaze.route("/")
def index():
    showSearch = getShowSearch('girl')
    titles = []
    for item in showSearch: 
        titles.append(item[0])
    showInfo = getShowInfo("139")
    return render_template("throwaway.html",titles=titles)

if __name__=="__main__":
    tvmaze.debug=True
    tvmaze.run(host="127.0.0.1",port=5000)
