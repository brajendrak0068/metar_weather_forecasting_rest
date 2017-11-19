#this http service module which calls the third party api and caches the response in redis

import requests
from django.core.cache import cache
from weather_forecasting.utils import text_to_json
from django.conf import settings

def get_data(url, expiry, no_cache):
    cache_key  = settings.DJANGO_ENV + ':'+ url;   #append the current running env to cache key

    if not no_cache:
        cached_response  =  cache.get(cache_key)
        if cached_response:    
            return {'data': cached_response, 'status_code': 200} #if response present in cache then return it   

    r = requests.get(url)
    json_content = None
    if r.status_code == 200:
        json_content = text_to_json.convert(r.content)    #convert text to dictionary
        cache.set(cache_key, json_content, timeout=expiry)  #set the final data in redis with expriry 
    else: 
        json_content = r.content
    
    return {'data':json_content, 'status_code':r.status_code}


