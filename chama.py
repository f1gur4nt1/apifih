import os
os.system("date")
from apifih import api
import sys
from threading import Thread
email=sys.argv[1]


"""
th1 = threading.Thread(target = api.facebook(email))

#th2 = threading.Thread(target = api.instagram(email))

#th3 = threading.Thread(target = api.twitter(email))

#th4 = threading.Thread(target = api.github(email))


th1.start()
th2.start()
th3.start()
th4.start()
"""
#api.facebook(email)
#api.instagram(email)
#api.twitter(email)
#api.github(email)


def action():
  api.main(email)


th = Thread(target = action)
th.start()

print("threading")



#os.system("date")
