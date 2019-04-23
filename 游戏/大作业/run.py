#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/4/22 15:18
import pygame
import sys
import demo_bird
import demo_pig
from pygame.locals import  *

def main():
    pygame.init()
    bg = pygame.image.load("bg.png")  # 加载背景图片
    bgpos = bg.get_rect()  # 获取背景大小矩形
    size = width, height = 1024, 576 #屏幕大小
    screen = pygame.display.set_mode(size)  # 屏幕展示
    pygame.display.set_caption('愤怒的小鸟')  # 创建标题

    pygame.mixer.music.load("Angry_Birds.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()  # 开始播放


    bird = demo_bird.Bird()  # 创建bird对象
    i = 0  # 开始时猪数量
    score = 0 #初始化分数
    group = pygame.sprite.Group()  # 生成一个精灵组

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # 退出程序

        key = pygame.key.get_pressed()  # 获取键盘
        if key[K_LEFT]:  # 按下左键
            bird.move_left()
        if key[K_RIGHT]:  # 按下右键
            bird.move_right()
        if key[K_UP]:  # 按下上键
            bird.move_up()
        if key[K_DOWN]:  # 按下下键
            bird.move_down()
        screen.blit(bg, bgpos)  # 加载背景图片
        screen.blit(bird.img, bird.rect)  # 加载小鸟素材

        i = i + 1  # 增加猪的数量
        if i % 30 == 0: #生成猪的条件
            pig = demo_pig.Pig()  # 生成pig对象
            group.add(pig)  # 添加进去
        for p in group.sprites():  # 取出对象
            p.move()  # 移动
            screen.blit(p.img, p.rect)  # 显示到屏幕上
            if pygame.sprite.collide_mask(bird, p):  # 检测是否碰撞
                pause(score) #游戏失败。进入gameover页面
            else:
                score += 0.1 #没有碰撞分数+0.1
        score_font = pygame.font.SysFont("arial", 48)  # 定义分数字体
        score_text = score_font.render("Score : %d" % score, True,  (121, 205, 205)) #渲染分数
        screen.blit(score_text, (10, 5)) #显示到屏幕

        pygame.display.flip()  # 刷新
        pygame.time.Clock().tick(60) #控制帧速率


def pause(score):
    pygame.mixer.music.stop() #停止声音播放
    #print('结束分数:',int(score))
    bg_go = pygame.image.load('gameover.jpg') #加载游戏结束图片
    bg_goes = bg_go.get_rect() #获取矩形大小
    size = width, height = 1024,576 #定义宽高
    screen = pygame.display.set_mode(size) #定义一个屏幕

    pygame.display.set_caption('GameOver') #定义标题

    while True:
        for event in pygame.event.get(): #获取事件
            if event.type == pygame.QUIT: #点击 x符号 时候
                sys.exit()  # 退出程序
        img_src = 'restar.png'  #图片按钮
        img = pygame.image.load(img_src) #加载图片
        img_srcpos = img.get_rect() #获取矩形大小

        mouse_pre = pygame.mouse.get_pressed() #获取鼠标
        mouse_pos = pygame.mouse.get_pos(mouse_pre) #获取鼠标位置

        left = img_srcpos.left  #获取图片左边位置
        right = img_srcpos.right  #获取图片右边位置
        top = img_srcpos.top  #获取图片上边位置
        bottom = img_srcpos.bottom  #获取图片下边位置

        if left<mouse_pos[0]<right and top<mouse_pos[1]<bottom: #鼠标落在图片上时。
            img_src = 'restar_02.png'  # 图片按钮
            img = pygame.image.load(img_src)  # 加载图片2,当鼠标在重玩儿按钮上时，按钮有一个变淡的效果。相当于重新加载一张图片
            if mouse_pre[0]: #当点击了 重玩儿时候
                main() # 重新执行主函数

        screen.blit(bg_go, bg_goes) #渲染图片
        screen.blit(img,img_srcpos) #渲染图片

        score_font = pygame.font.SysFont("arial", 48)  # 定义分数字体
        score_text = score_font.render("Score : %d" % score, True,  (0, 255, 0)) #显示游戏失败的分数
        screen.blit(score_text, (412, 5)) #显示到屏幕上

        pygame.display.flip()#更新界面

if __name__ == '__main__':
    main()
    # import traceback
    # try:
    #     main()
    # except SystemExit:
    #     pass
    # except:
    #     traceback.print_exc()
    #     pygame.quit()
    #     input()
    #pause()


