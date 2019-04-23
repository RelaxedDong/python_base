#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/22 16:42
import pygame
from random import randint

class Pig(pygame.sprite.Sprite):
    def __init__(self):
        """初始化"""
        pygame.sprite.Sprite.__init__(self)
        y = randint(60,560) # 生成随机数，猪出现。x轴固定，出现。
        position= [924, y] #猪开始时，出现的位置

        self.img = pygame.image.load('pb.png')  # 加载猪的素材
        self.rect = self.img.get_rect()  # 获取矩形大小
        self.rect.center = position  # 指定中心
        self.image = self.img  # 绑定图片

        speed = [-4,0]  #猪x轴向前移动，y轴不变
        self.speed = speed


    def move(self):
        self.rect = self.rect.move(self.speed)  #开始左移动






























