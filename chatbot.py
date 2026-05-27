#infinite loop
import webbrowser
from datetime import datetime
helloIntent = ["hey","hi","hello","hie","wassup","hy"]
byeIntent = ["bye","tata","c u","see you","ttyl","bie"]

import urllib.request as url #step1 and 2-rq and res
import bs4#beautiful soup 4 - step3 -fetch the data

#you can install bs4 by going to cmd ->pip install bs4 and 
#pip install lxml-to fetch data from html and xml

while True:
    msg = input("Enter msg : ")
    if msg in helloIntent:
        print("hey")

    elif msg in byeIntent:
        print("bye...👋")
        break#break is used to exit the loop

    elif msg.startswith("open"):
        webbrowser.open("https://"+msg.split()[-1]+".com")

    elif "date" in msg:
        dt = datetime.now()
        print(dt.strftime("%d-%m-%Y,%a"))
    
    elif "time" in msg:
        dt = datetime.now()
        print(dt.strftime("%H:%M:%S,%a"))

    elif "news" in msg:
        path = "https://indianexpress.com/section/india/?ref=l1_home"
        response = url.urlopen(path)
        data = bs4.BeautifulSoup(response,'lxml')
        news = data.find_all("h2",class_="title")
        x=1
        for headline in news:
            print(x," =>",headline.text)
            print("**************************")
            x+=1

    else:
        print("Sorry i don't understand")
