'''
Python has a module named datetime to work with dates and times
One of the classes defined in the datetime module is datetime class. We then use now() method to create a datetime object containing the current local date and time.
Commonly used classes in the datetime module are:
        date Class
        time Class
        datetime Class
        timedelta Class
'''
import datetime
print(dir(datetime))        #['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
dt_obj  = datetime.datetime.now() ; print(dt_obj)       #2020-11-11 14:09:11.992404
dt_obj1 = datetime.date.today() ; print(dt_obj1)        #2020-11-11
dt_obj2 = datetime.date(2019, 4, 13) ; print(dt_obj2)   #2019-04-13
#date() in the above example is a constructor of the date class. The constructor takes three arguments: year, month and day.

from datetime import datetime
a = datetime(2018, 11, 28)  ; print(a)    ##datetime(year, month, day)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)  ; print(b)   ## datetime(year, month, day, hour, minute, second, microsecond)

from datetime import date
today = date.today()    # date object of today's date
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


from datetime import time
a = time(11, 34, 56, 4567)
print(a)
print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

'''
TIME MODULE :
'''
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

import time
print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

#DIGITAL CLOCK
import time
while True:
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)


#DIGITAL CLOCK _ 2
import time
while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)


'''
FORMATTING DATETIME :
The way date and time is represented may be different in different places, organizations etc.
It's more common to use mm/dd/yyyy in the US, whereas dd/mm/yyyy is more common in the UK.
Python has strftime() and strptime() methods to handle this.

The strftime() method is defined under classes date, datetime and time.
The method creates a formatted string from a given date, datetime or time object.


'''
from datetime import datetime
now = datetime.now()    # current date and time

t = now.strftime("%H:%M:%S") ; print("time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S") ; print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S") ; print("s2:", s2)
x

'''
FLUSHING :
https://www.geeksforgeeks.org/python-sys-stdout-flush/
Not working properly in Atom . execute below codes one by one .
'''
import sys
import time

for i in range(10):
    print(i)
    time.sleep(1)


import sys
import time

for i in range(10):
    print(i,end=' ')
    time.sleep(1)


import sys
import time

for i in range(10):
    print(i, end =' ')
    sys.stdout.flush()
    time.sleep(1)

import sys
import time

for i in range(10):
    print(i, end =' ', flush = True)
    time.sleep(1)
