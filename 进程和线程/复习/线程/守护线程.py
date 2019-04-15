import time
import threading

"""如果你设置一个线程为守护线程，就表示你在说这个线程是不重要的，在进程退出的时候，不用等待这个线程退出。如果你的主线程在退出的时候，不用等待那些子线程完成，
那就设置这些线程的daemon属性。即在线程开始（thread.start()）之前，调用setDeamon（）函数，设定线程的daemon标志。（thread.setDaemon(True)）就表示这个线程“不重要”。
　　如果你想等待子线程完成再退出，那就什么都不用做，或者显示地调用thread.setDaemon(False)，设置daemon的值为false。新的子线程会继承父线程的daemon标志。整个Python会在所有的非守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。
"""
def fun():
    print("start fun")
    time.sleep(2)
    print("end fun")


print("main thread")
t1 = threading.Thread(target=fun,args=())
#t1.setDaemon(True)
t1.start()
time.sleep(1)
print( "main thread end")