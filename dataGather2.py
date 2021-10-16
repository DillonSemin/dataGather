import webbrowser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import time

chrome_options = Options()  
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def scroll(times, wait):
	for x in range(times):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
		time.sleep(wait)

def getData(url):
	print("Starting " + str(url))
	dataList = []
	driver.get(url)
	scroll(6, 3)
	html = driver.page_source                                                
	soup = BeautifulSoup(html, "html.parser")

	for tag in soup.find_all(class_="winrate"):
		dataList.append((tag.text).replace("%",""))
	for tag in soup.find_all(class_="pickrate"):
		dataList.append((tag.text).replace("%",""))
	with open("data.txt", "w") as file1:
		file1.write(url + "\n")
		for elem in dataList:
			file1.write(elem + "\n")

	print("Done with " + str(url))

urls = ["https://u.gg/lol/tier-list?rank=overall&region=na1"]
open('file.txt', 'w').close()
for url in urls:
	getData(url)
driver.close()










