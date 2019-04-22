#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/22 15:25
import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # 初始化
        position = 230,230 #初始位置
        self.img = pygame.image.load('ab.png')  #加载小鸟素材
        self.rect = self.img.get_rect() #获取矩形大小
        self.rect.center = position #指定中心
        self.image = self.img #绑定图片

    def move_left(self):
        """小鸟左边移动"""
        self.speed = [-10,0]
        if self.rect.left <= 0 :#当出屏幕时候
            self.rect.left = 0
        else:
            self.rect = self.rect.move(self.speed) #开始移动

    def move_right(self):
        """小鸟右边移动"""
        self.speed = [10,0]
        if self.rect.right >= 1024 :#当出屏幕时候
            self.rect.right = 1024
        else:
            self.rect = self.rect.move(self.speed) #开始移动

    def move_up(self):
        """小鸟上边移动"""
        self.speed = [0,-10]
        if self.rect.top <= 0 :#当出屏幕时候
            self.rect.top = 0
        else:
            self.rect = self.rect.move(self.speed) #开始移动

    def move_down(self):
        """小鸟下边移动"""
        self.speed = [0,10]
        if self.rect.bottom >= 576 :#当出屏幕时候
            self.rect.bottom = 576
        else:
            self.rect = self.rect.move(self.speed) #开始移动

