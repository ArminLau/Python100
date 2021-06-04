"""
Case010: Output current time in local time format, with interval one second
"""
import time
for i in range(10):
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("current time: " + local_time + "  timestamp: ", end="")
    time_stamp = time.mktime(time.strptime(local_time,"%Y-%m-%d %H:%M:%S"))
    print(time_stamp)
    time.sleep(1)