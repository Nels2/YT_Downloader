from pytube import YouTube

#ask for the link from the user
link = input("[Fella]Enter the link for YT video you intend to download, and remeber this downloads only in audio(320kbps) format. :  ")
yt= YouTube(link)

#Showing details
print("============================")
print("Title           : ",yt.title)
print("Number of Views :  ",yt.views)
print("Length of video :  ",yt.length," minutes/seconds")
print("Rating          :  ",yt.rating," of 5.0000")
print("============================")
#Getting the highest resolution possible
ys = yt.streams.get_by_itag('140')

#Starting download
print("[Fella]I'm beginning da download....")
ys.download('/home/sdsadmin/Downloads/')
print("[Fella]I finished!!")
