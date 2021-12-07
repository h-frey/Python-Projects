from pytube import *
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
        ys.download("C:\\Users\\Humphrey\\Downloads")

        with open("C:\\Users\\Humphrey\\Code Scripts\\Python Scripts\\Youtube_Video_Downloader_history.txt", "a") as file:
            file.write(yt.title+" "*10 + str(yt.length//(60)) +
                    " "*10+str(yt.views))
            file.write("\n")
            file.close()
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
