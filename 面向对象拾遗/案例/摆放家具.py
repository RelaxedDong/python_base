#encoding:utf-8
# __author__ = 'donghao'
# __time__ = 2019/1/12 15:25

class HouseItem(object):
    def __init__(self,name,area):
        self.name = name
        self.area = area

class House(object):
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []
    def add_item(self,item):
        self.free_area-=item.area
        self.item_list.append(item)
    def __str__(self):
        return '户型%s,总面积%s,剩余面积%s,家具名称%s'%(self.house_type,self.area,self.free_area,[house.name for house in self.item_list])
bed = HouseItem('bed',4)
chest = HouseItem('chest',2)
table = HouseItem('table',4)

myhouse = House('大户型',100)

myhouse.add_item(bed)
myhouse.add_item(chest)
myhouse.add_item(table)

print(myhouse)