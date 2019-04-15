#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 11:13
import threading
import time
def f():
    time.sleep(1)
    # print('线程标识符',threading.get_ident())
    print('当前Thread对象',threading.current_thread())


def myrace(a,b,c):
    print(threading.current_thread,'is on race')

if __name__ == '__main__':
    thread_list= []
    for x in range(3):
        t = threading.Thread(target=f,name=x)
        thread_list.append(t)
    # threading.settrace(myrace)  # 设置跟踪功能
    # threading.setprofile(func) # 启动的所有线程设置配置文件功能
    for t in thread_list:
        t.start()
    # print('当前活动的对象数', threading.active_count())
    # print('当前活动的所有对象的列表',threading.enumerate())
    print('主Thread对象',threading.main_thread())
    for t in thread_list:
        t.join()

        # threading.stack_size（[大小] ）
        # 返回创建新线程时使用的线程堆栈大小。可选的
        # size参数指定用于后续创建的线程的堆栈大小，并且必须为0（使用平台或配置的默认值）或至少为32, 768（32
        # KiB）的正整数值。如果未指定大小，则使用0

        # threading.TIMEOUT_MAX
        # 允许的最大值的超时阻断功能的（参数Lock.acquire()，RLock.acquire()，Condition.wait()
        # 等等）。指定超过此值的超时将引发一个
        # OverflowError。