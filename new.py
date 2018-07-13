import requests
import json

def write():

 url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=490529578a034be7aa774834b08fce87')
 response = requests.get(url)
 w=requests.get(url).json()
 with open('data.json','w') as outfile:
     json.dump(w,outfile)

def read_fromfile():
 with open('data.json') as data_file:
  data=json.load(data_file)
  lis=[]
  for article in data['articles']:
    lis.append(article['description'])
  return lis

def remove_none_elements_from_list(lis):
    return [e for e in lis if e != None]


def meth():
 x=read_fromfile()
 p=remove_none_elements_from_list(x)
 return p 
