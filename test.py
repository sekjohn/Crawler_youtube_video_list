from selenium import webdriver as wd
from selenium import webdriver
from bs4 import BeautifulSoup 
import time 

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = wd.Chrome(executable_path="/Users/lionrocket/Desktop/toutube_list/chromedriver",options=options)

url = 'https://www.youtube.com/c/cbs15min/videos' 
driver.get(url) 

last_page_height = driver.execute_script("return document.documentElement.scrollHeight") 
while True: 
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") 
    time.sleep(3.0) 
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight") 
    if new_page_height == last_page_height: 
        break 
    last_page_height = new_page_height 

html_source = driver.page_source 
driver.close() 
soup = BeautifulSoup(html_source, 'html.parser')

#print(soup)
#youtube_play_list = soup.find_all("a",{"class":"yt-simple-endpoint inline-block style-scope ytd-thumbnail"})
#youtube_play_list = soup.find_all("href")
#youtube_play_list = soup.select("a#thumbnail yt-simple-endpoint inline-block style-scope ytd-thumbnail href")
youtube_play_list = soup.select('a#thumbnail')


str_=""
for i in range(len(youtube_play_list)):
    A = dict(youtube_play_list[i].attrs)
    if 'href' in A:
        str_+=f"https://www.youtube.com/{A['href']}\n"

with open("youtube_list.text","w") as f:
    f.write(str_)


