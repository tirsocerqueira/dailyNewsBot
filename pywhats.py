import pywhatkit as kit
import requests
from datetime import datetime

#Retrieving data from New York Times
res = requests.get("https://api.nytimes.com/svc/topstories/v2/world.json?api-key=zwEN89uPuhAG8Ysrrb7D18xjuRHwAkSL")
registros = res.json()['results']

#Data format
msg="\U0001F4F0 DAILY NEWS "
for i in registros:
    msg+='\U0001F4F0 '
    msg+=i['title']
    msg+='\n'
    msg+=(i['url'])
    msg+='\n'

#Sending data to Suscribers
currentDateAndTime = datetime.now()
hour=currentDateAndTime.strftime("%H")
minute=currentDateAndTime.strftime("%M")
hour=int(hour)
minute=int(minute)+1
#Pay attention to the empty block and add a number
kit.sendwhatmsg("",msg,hour,minute,15)
