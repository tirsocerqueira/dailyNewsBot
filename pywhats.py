import pywhatkit as kit
import requests

#Retrieving data from New York Times
res = requests.get("https://api.nytimes.com/svc/topstories/v2/world.json?api-key=zwEN89uPuhAG8Ysrrb7D18xjuRHwAkSL")
registros = res.json()['results']

msg=""

for i in registros:
    msg+=i['title']
    msg+='\n'
    msg+=(i['url'])
    msg+='\n'

print(msg)

#Sending data to Suscribers
kit.sendwhatmsg("+34656366579",msg,16,33)
