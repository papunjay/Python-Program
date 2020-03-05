import time
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time lapsed={}:{}:{}".format(int(hours),int(mins),int(sec)))
input("Press Enter to start")
start_time=time.time()
input("Press Enter to stop")
stop_time=time.time()
time_diff=stop_time-start_time
#print(time_diff)
time_convert(time_diff)