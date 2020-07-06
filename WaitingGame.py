import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {2:.3f}".format(int(hours), int(mins), sec))
    if time_lapsed == 4:
        print("you are on time")
    elif time_lapsed > 4:
        print("You are too slow")
    else:
        print("You are too fast")


input("Press Enter to start")
start_time = time.gmtime()
print("You started at:", start_time[5])
input("Press Enter to stop")
end_time = time.gmtime()
print("You ended at:", end_time[5])

time_lapsed = end_time[5] - start_time[5]
time_convert(time_lapsed)
