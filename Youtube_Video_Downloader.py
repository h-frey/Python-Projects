from pytube import *
import sqlite3
import os
num = 0
db_conn = sqlite3.connect("ytdownloads.db")
cursorObj = db_conn.cursor()

# cursorObj.execute("CREATE TABLE downloads(id integer PRIMARY KEY, title text, views real,length real, rating real)")
def cli():
    
    link = input("Enter the link: ")
    yt = YouTube(link)
    
    def details(vid):
        print()
        print((" "*20)+"Title: ", yt.title)
        print((" "*20)+"Number of views: ", yt.views)
        print((" "*20)+"Video length: ", yt.length, "seconds")
        print((" "*20)+"Ratings: ", yt.rating)
        
        print((" "*20)+"Downloading...")
        print()

    def down_load():
        
        ys = yt.streams.get_highest_resolution()
        details(ys)
        # path = os.path.join(os.path.expanduser('~'), 'documents', 'python', 'file.txt')
        # print(path)
        path = os.path.join(os.path.expanduser('~'),'Downloads')
        ys.download(path)
        global num
        num+=1
        cursorObj.execute("INSERT INTO downloads VALUES('1','title', 'views', 'length', 'rating')")
        print("Download Complete!!!")

   
    down_load()
    

run=1
while run:
    cli()
    ans=input("Press 'y' to quit or any other key to continue: ")
    ans_1=input("Press 'y' again to quit: ")
    if ans == "y" and ans_1 =="y":
        run=0
    else:
        continue
