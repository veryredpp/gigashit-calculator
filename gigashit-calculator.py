from urllib import request
from tkinter import *
import webbrowser
import urllib
import base64
import os
window=Tk()
def browser(url):
   webbrowser.open_new_tab(url)
window.title("Shit/Gigashit Calculator")

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
url = "https://redstoner.me/downloads/gigashitfiles/gigashit.ico"
headers = {"User-Agent" : user_agent,} 
request = urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
b64pic = base64.encodebytes(response.read())
response.close()
icondata= base64.b64decode(b64pic)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()
window.wm_iconbitmap(tempFile)
os.remove(tempFile)

Label(text="CPU").grid(column=1,row=1)

Label(text="CPU Single Core Performance (Find it out in website below)").grid(column= 1,row=2)
singlecoreentry = Entry()
singlecoreentry.grid(column=1,row=3)

cpulink = Label(text="cpubenchmark.net",font=('Arial Bold', 10), fg="blue", cursor="hand2")
cpulink.bind("<Button-1>", lambda e:
browser("https://www.cpubenchmark.net/singleThread.html"))
cpulink.grid(column=1,row=4)

corecounttext = Label(text="CPU Core Count").grid(column=1,row=5)
corecountentry = Entry()
corecountentry.grid(column=1,row=6)

Label(text="CPU Clock Speed (Ghz)").grid(column=1,row=7)
clockspeedentry = Entry()
clockspeedentry.grid(column=1,row=8)

Label(text="").grid(column=1,row=9)

Label(text="RAM").grid(column=1,row=10)

ramamounttext = Label(text="Memory Amount (RAM) (GB)").grid(column=1,row=11)
ramamountentry = Entry()
ramamountentry.grid(column=1,row=12)

ramspeedtext = Label(text="Memory Speed (RAM) (Mhz)").grid(column=1,row=13)
ramspeedentry = Entry()
ramspeedentry.grid(column=1,row=14)


Label(text="").grid(column=1,row=15)

Label(text="Storage").grid(column=1,row=16)

Label(text="Storage Read Speed (MB/s)").grid(column=1,row=17)
storagereadentry = Entry()
storagereadentry.grid(column=1,row=18)

Label(text="Storage Write Speed (MB/s)").grid(column=1,row=19)
storagewriteentry = Entry()
storagewriteentry.grid(column=1,row=20)


Label(text="").grid(column=1,row=21)

Label(text="Internet").grid(column=1,row=22)

Label(text="Internet Download Speed (Mbps)").grid(column=1,row=23)
internetdownentry = Entry()
internetdownentry.grid(column=1,row=24)

Label(text="Internet Upload Speed (Mbps)").grid(column=1,row=25)
internetupentry = Entry()
internetupentry.grid(column=1,row=26)

Label(text="Ping to ISP (ms) (Be sure to choose your ISP's closest server to you)").grid(column=1,row=27)
pingentry = Entry()
pingentry.grid(column=1,row=28)
pinglink = Label(text="speedtest.net",font=('Arial Bold', 10), fg="blue", cursor="hand2")
pinglink.bind("<Button-1>", lambda e:
browser("https://www.speedtest.net/"))
pinglink.grid(column=1,row=29)

#Start of second row/results
shitsresult = Label(text="")
shitsresult.grid(column=2,row=1)
metric1label = Label(text="")
metric1label.grid(column=2,row=3)
metric1results = Label(text="")
metric1results.grid(column=2,row=4)
Label(text="").grid(column=2,row=5)
metric2label = Label(text="")
metric2label.grid(column=2,row=6)
metric2results = Label(text="")
metric2results.grid(column=2,row=7)
def clicked():
   global singlecoreentry
   #CPU
   singlecore = int(singlecoreentry.get())
   corecount = int(corecountentry.get())
   clockspeed = int(clockspeedentry.get())
   #RAM
   ramamount = int(ramamountentry.get())
   ramspeed = int(ramspeedentry.get())
   #Storage
   storageread = int(storagereadentry.get())
   storagewrite = int(storagewriteentry.get())
   #Internet
   internetdown = int(internetdownentry.get())
   internetup = int(internetupentry.get())
   ping = int(pingentry.get())
   #Calculating outputs
   shits = ((((singlecore/2740*corecount*clockspeed)/2*(ramamount*ramspeed)/2))*1000+(storageread+storagewrite)/2*(internetdown*internetup)/ping)*10
   #Metrics based on 10^n
   kiloshits = shits / (10**3)
   megashits = shits / (10**6)
   gigashits = shits / (10**9)
   terashits = shits / (10**12)
   petashits = shits / (10**15)
   #Metrics based on 2^n
   kibishits = shits / (2**10)
   mebishits = shits / (2**20)
   gibishits = shits / (2**30)
   tebishits = shits / (2**40)
   pebishits = shits / (2**50)
   #Results
   shitsresult.configure(text= "{:,}".format(round(shits)) + " S (shits)")
   #Metrics based on 10^n

   if shits > 1000:
      metric1label.configure(text="Metric based on 10^n")
      if kiloshits > 1000:
         if megashits > 1000:
            if gigashits > 1000:
               if terashits > 1000:
                  metric1results.configure(text= str(round(petashits,2))+" PS (Petashit/s)")
               else:
                  metric1results.configure(text= str(round(terashits,2))+" TS (Terashit/s)")
            
            else:
               metric1results.configure(text= str(round(gigashits,2))+" GS (Gigashit/s)")
         else:
            metric1results.configure(text= str(round(megashits,2))+" MS (Megashit/s)")
      else:
         metric1results.configure(text= str(round(kiloshits,2))+" KS (Kiloshit/s)")
   #Metrics based on 2^n
   if shits > 1024:
      metric2label.configure(text="Metric based on 2^n:")
      if kiloshits > 1024:
         if megashits > 1024:
            if gigashits > 1024:
               if terashits > 1024:
                  metric2results.configure(text= str(round(pebishits,2))+" PiS (Pebishit/s)")
               else:
                  metric2results.configure(text= str(round(tebishits,2))+" TiS (Tebishit/s)")
            
            else:
               metric2results.configure(text= str(round(gibishits,2))+" GiS (Gibishit/s)")
         else:
            metric2results.configure(text= str(round(mebishits,2))+" MiS (Mebishit/s)")
      else:
         metric2results.configure(text= str(round(kibishits,2))+" KiS (Kibishit/s)")
     
btn = Button(text="Click here to calculate your shits™",command=clicked).grid(column=1, row=30)

window.geometry("650x700")
window.mainloop()
