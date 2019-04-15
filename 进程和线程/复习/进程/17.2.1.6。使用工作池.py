#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/3/18 10:33
# 本Pool类代表工作进程池。它具有允许以几种不同方式将任务卸载到工作进程的方法。

from multiprocessing import Pool,TimeoutError,current_process
import time
import os

def f(x):
    print('*'*30,os.getpid())
    return x*x

# if __name__ == '__main__':
#     with Pool(processes=4) as pool:
#         print(pool.map(f,range(10)))
#         # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#
#         # for i in pool.imap_unordered(f,range(10)):
#         #     print(i)
#         # print same numbers in arbitrary order
#
#         # res = pool.apply_async(f,(20,))  # runs in *only* one process
#         # print(res.get(timeout=1)) # prints "400"
#
#         # res = pool.apply_async(os.getpid, ()) # runs in *only* one process
#         # print('PID is:',res.get(timeout=1))   # prints the PID of that process
#
#         mutiprocess_results = [pool.apply_async(os.getpid,()) for i in range(4)]
#         print([res.get(timeout=1) for res in mutiprocess_results])
#
#         # make a single worker sleep for 10 secs
#         res = pool.apply_async(time.sleep,(10,))
#         try:
#             print(res.get(timeout=1))
#         except TimeoutError:
#             print("We lacked patience and got a multiprocessing.TimeoutError")
#
#         print("For the moment, the pool remains available for more work")
#     print("Now the pool is closed and no longer available")

# 请注意，池的方法只能由创建它的进程使用

"""from multiprocessing import Pool
p = Pool(5)

p.map(f, [1,2,3])
"""

# 此程序包中的功能要求__main__子程序可以导入该模块。这在编程指南中有所涉及，
# 但值得在此指出。这意味着某些示例（例如multiprocessing.pool.Pool示例）在交互式解释器中不起作用