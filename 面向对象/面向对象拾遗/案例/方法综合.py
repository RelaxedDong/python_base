#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 21:28


class Game(object):
    '''一款游戏'''
    top_score = 0
    name = '植物大战僵尸'
    def __init__(self,player_name):
        self.player_name = player_name

    @classmethod
    def show_top_score(cls):
        print('游戏最高分是%d'%cls.top_score)

    @staticmethod
    def show_help():
        print('帮助信息')

    def start_game(self):
        print(Game.name)
        print('%s开始游戏'%self.player_name)


player = Game('donghao')
Game.show_top_score()

Game.show_help()
player.start_game()
Game.top_score = 100
Game.show_top_score()
# print(Game.__doc__)用于描述该对象的作用

#静态方法：方法内部，不需要访问实例属性和类属性
#实例方法：方法内部，需要访问实例属性（实例方法内部可以使用 类名，访问类属性）
#类方法： 方法内部 只需要访问类属性

