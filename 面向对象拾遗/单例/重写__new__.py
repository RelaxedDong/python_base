#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 22:32

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print('创建对象，分配内存空间')
        a = super().__new__(cls)
        a = super(MusicPlayer,cls).__new__(cls)
        #重写__new__方法一定要返回 return super().__new__()
        #否则python解释器得不到分配了空间的对象引用， 就不会调用对象的初始化方法
        #__new__是一个静态方法staticmethod。在调用时需要主动传递cls参数
        print(a)
        return a

    def __init__(self):
        print('播放器初始化')


music = MusicPlayer()
music.name = 12

print(music.name)