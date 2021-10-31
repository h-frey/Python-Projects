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
        #print((" "*20)+"Video Size: " +str(int(yt.filesize)//1024//1024)+" MBS")
        print((" "*20)+"Downloading...")
        print()

    def down_load():
        choice = input("Press '1' for '480p' or '2' for 'best resolution' ")
        if choice == "1":
            ys1 = yt.streams.filter(res="480p", progressive=True).first()
            details(ys1)
            ys1.download("C:\\Users\\Humphrey\\Downloads")

        elif choice == "2":
            ys = yt.streams.get_highest_resolution()
            details(ys)
            ys.download("C:\\Users\\Humphrey\\Downloads")

        with open("C:\\Users\\Humphrey\\Code Scripts\\Personal Scripts\\Youtube_Video_Downloader_history.txt", "a") as file:
            file.write(yt.title+" "*10 + str(yt.length//(60)) +
                    " "*10+str(yt.views))
            file.write("\n")
            file.close()
        print("Download Complete!!!")

    cap=input("Do you want captions(Y/N)? ")
    if cap=="Y" or cap=="y":
        try:
            caption = yt.captions["en"]
        except AttributeError:
            caption = yt.captions["a.en"]

        srt_captions = caption.generate_srt_captions()

        subtitle_file = "C:\\Users\\Humphrey\\Downloads\\%s.srt" %(yt.title)

        with open(subtitle_file, "a") as f:
            f.write(srt_captions)
            f.close()
        down_load()
    else:
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
