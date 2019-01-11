
from person import Person
from Gun import gun
from bulletbox import BulletBox


#弹夹
bulletBox = BulletBox(5)

#枪

gun = gun(bulletBox)


# 人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.putBut()
per.putBut()
per.putBut()
per.putBut()
per.fire()



'''
人
类名：Person
属性：枪
行为：fire


枪
GUN
属性：bulletbox
行为：shoot


弹夹
bullebox
属性

'''

