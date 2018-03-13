from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup
import string

XML_PARSER = "html.parser"
TIMEOUT = 10
Kai_Yuan_link = "http://www.kaiyuan.info/forum.php?mod=forumdisplay&fid=92&filter=sortid&sortid=262"
Deguorexian_link = "https://www.dolc.de/forum.php?mod=forumdisplay&fid=14&page=1&filter=typeid&typeid=32"
Huarenjie_link = "https://www.huarenjie.net/deguo/category-122-12-1.html?&areaid=63"
key_words=["慕尼黑","Garching"]
item_type_ask = '出租房屋'
item_type_ask_hrj = '供房'

print("++++++++DEMO++++++++")
## Get
driver = webdriver.PhantomJS()
driver.get(Huarenjie_link)
driver.set_page_load_timeout(TIMEOUT)
pg_src = driver.page_source
driver.close()
driver.quit()


# Parse
soup = BeautifulSoup(pg_src, XML_PARSER)
columns = soup.find_all("div", "li_dian hover ")
items=[]
for column in columns:
    type_ = column.find_all("font", "xx2")
    type = type_[0].string
    item_ = column.find_all("a")
    item = item_[0].string
    if type == item_type_ask_hrj:
        items.append(item)
print(items)
exit(0)



vice_columns = soup.find_all("em")
unit_str_list = []
for vice_column in vice_columns:
    unit = vice_column.find_all("a")
    if len(unit) != 0:
        unit_str = unit[0].string
        unit_str_list.append(unit_str)

cnt = 0
vice_items = []
for unit in unit_str_list:
    if cnt % 3 == 0:
        state = unit
    if cnt % 3 == 1:
        type = unit
    if cnt % 3 == 2:
        time = unit
        vice_items.append([state, type, time])
    cnt += 1

columns = soup.find_all("a", "s xst")
main_items = []
for column in columns:
    item = column.string.strip()
    main_items.append(item)

items=[]
for i in range(0, len(main_items)):
    if vice_items[i][1] == item_type_ask:
        items.append(main_items[i])
print("aaa")
print(items)





# Process
results = []
for item in items:
    matched = False
    for key_word in key_words:
        item_upper = item.upper()
        key_word_upper = key_word.upper()
        if item_upper.find(key_word_upper) == -1:
            matched = False
            break
        else:
            matched = True
    if matched == True:
        results.append(item)

print(results)
print("Process Done")