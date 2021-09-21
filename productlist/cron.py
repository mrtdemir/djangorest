import os,sys,platform
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
import django
django.setup()
import json
from django.core.cache import cache

def writeitems(listname,cachename,product_name):
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path+"/urunlist/"+listname+".txt", "wb")
    datas = cache.get(cachename)
    context = dict()
    for data in datas:
        context[data['URUN_ID']] = data[product_name] 
    f.write(json.dumps(context).encode('utf8'))
    f.close()

def makelist():
    all_list = (
        ('fao','URUN'),('usda','KALEM'),('mapuretimler','MADDE_ADI'),
        ('tufe','KALEM_ADI'),('tuik','KALEM'),('tuikdirexternal','KALEM'),
        ('tuikexternal','KALEM'),('tuikotsexternal','KALEM'),('tuikotsdirexternal','KALEM'),
        ('worldagriculture','KALEM'),('ufe','KALEM_ADI'),
        )
    for table,column in all_list:
        writeitems(table+"list",table,column)
        writeitems("full"+table+"list","full"+table,column)

def fullproductpricelist():
    datas = cache.get('fullmarketprices')
    data_list = []
    for i in datas:
        if i['VARIETY']:
            data_list.append((i['VARIETY'],i['YEAR']))
    data_list = list(sorted(set(data_list)))

    context = dict()
    for variety,year in data_list:

        if variety not in context:
            context[variety] =list()
        context[variety].append(year)
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path+"/urunlist/fullproductlist.txt", "wb")
    f.write(json.dumps(context).encode('utf8'))
    f.close()

def productpricelist():
    datas = cache.get('marketprices')
    data_list = []
    for i in datas:
        if i['VARIETY']:
            data_list.append((i['VARIETY'],i['YEAR']))
    data_list = list(sorted(set(data_list)))

    context = dict()
    for variety,year in data_list:

        if variety not in context:
            context[variety] =list()
        context[variety].append(year)
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path+"/urunlist/productlist.txt", "wb")
    f.write(json.dumps(context).encode('utf8'))
    f.close()