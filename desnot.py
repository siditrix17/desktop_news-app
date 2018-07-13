import new
import datetime
import time
import schedule

import gi

gi.require_version('Notify', '0.7')
from gi.repository import GLib, Notify


#gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("siditrix___notification")


def notification_banner(): 
 message = new.meth()
 for i in range(len(message)-1):
  summary='News'
  body=message[i]
  notification = Notify.Notification.new( 
     	summary,
	body
    
  )
 # Actually show on screen
  notification.show()
  time.sleep(5)
  notification.close()



f=open('data.json','w')
new.write()
notification_banner()

schedule.every(15).minutes.do(notification_banner)
while True:
    schedule.run_pending()
    time.sleep(1)
