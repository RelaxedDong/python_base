#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 22:57

class MusicPlayer(object):
    '''音乐播放器'''
    #记录一个被创建对象的引用
    instance = None
    init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(MusicPlayer, cls).__new__(cls)
            return cls.instance
        return cls.instance

    def __init__(self,name):
        if self.init_flag:
            self.name = name
            MusicPlayer.init_flag = False



music1 = MusicPlayer('播放器1')
music2 = MusicPlayer('播放器2')
print(music1.name)
print(music2.name)

#思考：初始化一次？




