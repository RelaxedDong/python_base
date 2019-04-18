#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/18 20:35
import time

def ReadFile(filename):
    with open(filename,'rb') as f:
        start = time.time()
        count = 0
        while True:
            data = f.readline(1000).decode('utf-8')
            if 'flower' in data:
                count += 1
            if not data:
                break
    print('出现次数',count)
    end = time.time()
    print('耗时 %.02fs'%(end-start))

"""
出现次数 172032
耗时 2.82s
"""

def main(filename):
    ReadFile(filename)

if __name__ == '__main__':
    filename = 'test'
    main(filename)




























