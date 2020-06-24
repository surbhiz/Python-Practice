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
        print("You are too fast")
    else:
        print("You are slow")


input("Press Enter to start")
start_time = time.time()
print("You started at:", start_time)
input("Press Enter to stop")
end_time = time.time()
print("You ended at:", end_time)

time_lapsed = end_time - start_time
time_convert(time_lapsed)
