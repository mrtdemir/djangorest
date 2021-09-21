import os,sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
import django
django.setup()


from django.core.cache import cache,caches
import json

def writeitems(list):
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path+"/cachelist.txt", "wb")
    f.write(json.dumps(list).encode('utf8'))
    f.close()


def productmarketcaches():
    datas = cache.get('fullmarketprices')
    data_list = []
    for i in datas:
        if i['VARIETY']:
            data_list.append((i['VARIETY'],i['YEAR']))
    data_list = list(sorted(set(data_list)))
    all_list = []
    
    for variety,year in data_list:

        item = {"VARIETY":variety,"YEAR":year}
        
        [item.pop(key) for key,value in item.copy().items() if not value]
        data = [x for x in datas if item.items() <= x.items()]
        m_cache = caches['marketprice']
        cache_variety = str(variety).replace(" ","").replace("%","").replace(",","").replace(".","")
        l_item = {"CACHE_NAME":cache_variety,"VARIETY":variety,"YEAR":year}
        all_list.append(l_item)
        m_cache.set('marketprices'+str(cache_variety)+str(year), data,86400)
    writeitems(all_list)
