#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 15:40

class Gun(object):
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count+=count

    def shoot(self):
        self.bullet_count-=1
        print('啪啪啪,射击成功，剩余%d颗子弹'%self.bullet_count)


class Solider(object):
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(selfs):
        selfs.gun.shoot()


ak47 = Gun('ak47')
solider_666 = Solider(name='大佬')
solider_666.gun = ak47
solider_666.gun.add_bullet(20)

solider_666.fire()
solider_666.fire()
solider_666.fire()

