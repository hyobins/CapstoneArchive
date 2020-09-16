from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://blog.naver.com/atlas100/222086300913')
soup = bs(html.text, 'html.parser')

data = soup.find('div', {'class':'se-main-container'})
text = data.find('span', {'class':'se-fs-fs16 se-ff-nanummyeongjo'})

print(text)
