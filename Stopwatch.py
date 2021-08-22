"""
*Author : Tanmay Ku Mallick
*Date   : 20-08-2021
*Title  : StopWatch
"""
import time


class Stopwatch:
    @staticmethod
    def Stop_watch(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time elapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


start = input("press enter to start the timer")
print("the timer ha started ")
begin = time.time()
endtimer = input("press enter to stop the timer")
end = time.time()
elapsed = end - begin
stopWatch = Stopwatch()
stopWatch.Stop_watch(elapsed)
print("the time elapsed is ", elapsed, "seconds")
