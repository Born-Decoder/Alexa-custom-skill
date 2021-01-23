import sys
import requests
import bs4

try:
    res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
except:
    print("connection error")
    exit()
wiki = bs4.BeautifulSoup(res.text,'html.parser')
response_text = ""
for i in wiki.select('p'):
    try:
        response_text += i.getText()
    except:
        break
response_list = response_text.split(". ")
response_list = [i.lower() for i in response_list]
print(response_list[0]+". " +response_list[1])

    
