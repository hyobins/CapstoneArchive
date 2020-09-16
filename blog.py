import requests
import json
from urllib.parse import quote
import pandas as pd
 
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query="+encText+"차박"+"&sort=sim&display=100&start="+str(start)
    result = requests.get(url=url,
                          headers={"X-Naver-Client-Id":"doyEYm6zc4qz9ayfO5RA","X-Naver-Client-Secret":"8InHQwMIoT"})
    print(result)  # Response [200]
    return result.json()
 
def results(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword, num * 110 + 1)['items'] 
    return list


listt = []
location = input('검색하고싶은 지역?')
result = results(location)
listt = listt+result
file = open('result.json','w+')
file.write(json.dumps(listt))

df = pd.read_json('result.json')
df.to_csv('/Users/ihyobin/Desktop/crolling_results/crawling_result.csv',encoding='utf-8-sig',index=False)
