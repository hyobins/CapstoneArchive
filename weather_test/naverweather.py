from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests


where = input('어느 지역의 날씨가 궁금하세요? ')
html = requests.get('https://search.naver.com/search.naver?query='+where+' 날씨')
soup = bs(html.text, 'html.parser')

data1 = soup.find('div', {'class':'weather_box'})

address = data1.find('span', {'class':'btn_select'}).text
print('\n현재 '+address+'의 날씨정보입니다.')

find_temp = data1.find('span',{'class':'todaytemp'}).text
data2 = data1.findAll('dd')
find_dust = data2[0].find('span',{'class':'num'}).text
find_ultra_dust = data2[1].find('span',{'class':'num'}).text
find_ozone = data2[2].find('span',{'class':'num'}).text

print('현재기온: '+ find_temp)
print('미세먼지: '+ find_dust)
print('초미세먼지: '+ find_ultra_dust)
print('오존지수: ' + find_ozone)


#시간대별기온 
current = soup.find('div',{'class':'info_list weather_condition _tabContent'})
time = current.findAll('dd',{'class':'item_time'})
curData1 = current.findAll('dd',{'class':'weather_item _dotWrapper'})

#(시간대별)강수
current2 = soup.find('div',{'class':'info_list rainfall _tabContent'})
curData2 = current2.findAll('dd',{'class':'weather_item _dotWrapper'})

#list 형태로 출력
result = []
for i in range(1,5):
    line = []
    time1 = time[i].find('span',{'class':''}).text #시간
    line.append(time1)
    temp = curData1[i].find('span',{'class:':''}).text #온도
    line.append(temp+'°')
    rain = curData2[i].find('span',{'class:':''}).text #강수
    line.append(rain+'%')
    result.append(line)

print('시간대별 예보\n')
print(' 시간 | 온도 | 강수')
for (x,y,z) in result:
    print(x,'|',y,'|',z)







                                  
