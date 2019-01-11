#encoding:utf-8

class Person(object):

    def __init__(self,gun):
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def putBut(self):
        self.gun.put()