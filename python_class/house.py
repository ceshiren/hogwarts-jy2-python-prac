# -*- coding: utf-8 -*-
# @Author : feier
# @File : house.py

'''
class 类名:
    类属性....

    类方法....
'''

class House:
    # 属性：类变量，在类之中，在方法外面
    door = ""
    floor = ""
    # 私有属性
    __key = True

    # 构造函数，类实例化的时候自动执行的方法
    def __init__(self, door, floor):
        print("构造函数")
        # 在构造函数中定义实例变量
        # 实例变量，类中，方法中，以 self. 开头
        self.table = "餐桌"
        self.kitchen = "cook"
        # 把接受到的值赋值给实例变量
        self.door = door
        self.floor = floor

    # 方法
    def sleep(self):
        # 局部变量，类的方法中
        bed = "席梦思"
        print(self.kitchen)
        print(f"在房子里可以躺在{bed}上睡觉")

    def cook(self):
        # 在其他方法中调用实例变量
        print(self.table)
        print("在房子里可以做饭")

    @classmethod
    def class_method(cls):
        print("类方法")

    def open_door(self):
        # 调用类变量也需要前面加上 self
        if self.__key == True:
            print("开门成功")
        else:
            print("没钥匙，不能开门")

    # 定义私有方法
    def __open_save(self):
        print("打开保险箱")

    def get_key(self):
        self.__open_save()




if __name__ == '__main__':
    House.class_method()
    # 实例化: 变量 = 类名()
    # 北欧风房子
    # 位置参数
    north_house = House("white", "black")
    # 中式风房子
    # 关键字参数
    china_house = House(floor="red", door="yellow")

    china_house.open_door()
    # china_house.__open_save()
    china_house.get_key()

    print(north_house.door)
    print(china_house.door)

    # 类的外部不能调用私有属性
    # print(House.__key)
    # print(north_house.__key)

    # House.sleep()

    china_house.class_method()
    # china_house.sleep()

    # # 定义北欧风房子的属性
    # north_house.floor = "black"
    # north_house.door = "white"
    #
    # # 定义中式风房子的属性
    # china_house.door = "yellow"
    # china_house.floor = "red"

    # # 调用类属性
    # House.floor = "blue"
    # print(north_house.floor)

    # north_house.sleep()
    # north_house.cook()




