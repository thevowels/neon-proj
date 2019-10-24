import schedule
import time
import datetime
import lcdcontrol
import dataio

arr=[]
timedata=[]
day = datetime.datetime.now().weekday()

def refreshdata():
    arr.clear()
    for x in dataio.readdata():
        arr.append(x)
    timedata.clear()
    for x in dataio.gettime():
        timedata.append(x)
    return

refreshdata()



def smth(arr,a1,a2,a3):
   datetimeobj= datetime.datetime.strptime(timedata[a1],'%H:%M')
   a=datetimeobj.strftime("%I:%M")
   b=datetimeobj.strftime("%p")
   print(a)
   print(b)
   s=str(arr[day][a2])
   p=str(arr[day][a3])
   lcdcontrol.test(a,b,s,p)
   #  lcdcontrol.alarm(a,b,arr[1],arr[2],arr[3],arr[4],arr[5])
   return

# schedule.every().day.at(timedata[0]).smth(arr,0,0,1)
# schedule.every().day.at(timedata[1]).smth(arr,1,2,3)
# schedule.every().day.at(timedata[2]).smth(arr,2,4,5)
schedule.every().day.at(timedata[0]).do(smth,arr=arr,a1=0,a2=0,a3=1)
schedule.every().day.at(timedata[1]).do(smth,arr=arr,a1=1,a2=2,a3=3)
schedule.every().day.at(timedata[2]).do(smth,arr=arr,a1=2,a2=4,a3=5)

while True:
    schedule.run_pending()
    time.sleep(1)