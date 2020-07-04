import time
"""
start = time.time()
time.clock()    
x = 0
time_finish = 0
while x < length:
    x = time.time() - start
    time_finish = time_finish + 1
    print "X count: %d" % (x) 
    time.sleep(1)  
print(time_finish)  """
"""
from datetime import datetime, timedelta
time_finish = (datetime.now() + timedelta(seconds=length)).strftime("%H:%M:%S")
print("Current Time =", time_finish)
current_time = time_finish.strftime("%H:%M:%S")
print("Current Time =", current_time)"""

length = 180
epoch_time = int(time.time())
print(epoch_time + length)