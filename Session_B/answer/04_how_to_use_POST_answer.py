
# coding: utf-8

# ## 範例 04: 如何使用 POST
# 
# 請打開[高鐵時刻表](https://www.thsrc.com.tw/tw/TimeTable/SearchResult)的網頁，並按照簡報上介紹的方法，觀察 requests 的方式

# In[ ]:

import requests
from bs4 import BeautifulSoup
import re


# In[ ]:

# 這是我們還沒有給任何 form_data 的 requests
response = requests.get("https://www.thsrc.com.tw/tw/TimeTable/SearchResult")
print(response.encoding)
soup = BeautifulSoup(response.text, "lxml")


# In[ ]:

# 觀察 option 裡面的 value
soup.find_all("option", {"value":re.compile("[a-z0-9]{8}-[a-z0-9]{4}")})


# In[ ]:

# 在還沒給任何 form_data 之前，我們是看不到搜尋後的結果的
print(soup.find("section", class_ = "result_table"))


# In[ ]:

# 將 form_data 透過 post 的方式進行 requests
form_data = {"StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
             "EndStation":"e6e26e66-7dc1-458f-b2f3-71ce65fdc95f",
             "SearchDate":"2017/08/13",
             "SearchTime":"20:30",
             "SearchWay":"DepartureInMandarin"}
response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data)
soup_post = BeautifulSoup(response_post.text, "lxml")


# In[ ]:

# 用同樣的搜尋條件，可以看到搜尋後的結果
soup_post.find("section", class_ = "result_table").find("tr")


# ## 練習 04: 如何使用 POST (8 mins)
# 請運用 POST 方式，找出 2017 年 8 月 14 日 21:30，**南港站**到**台南站**共有幾個班次?
# 
# Hint: 先到高鐵時刻表網站，實際查詢之後，看看班次的資訊都藏在哪些 tags 裡面

# In[1]:

# your codes
import requests
from bs4 import BeautifulSoup

# 將要查詢的資料寫成 dictionary
form_data = {"StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
             "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
             "SearchDate":"2017/08/14",
             "SearchTime":"21:30",
             "SearchWay":"DepartureInMandarin"}

# requests 改用 POST，並放入剛剛寫好的 dictionary
response_post = requests.post("https://www.thsrc.com.tw/tw/TimeTable/SearchResult", data = form_data)
soup_post = BeautifulSoup(response_post.text, "lxml")

# 觀察高鐵網頁後，發現車次資訊藏在 屬性 class=column1 的標籤裡面
print(len(soup_post.find_all("td",class_="column1")))

