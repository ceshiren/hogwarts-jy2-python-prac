# -*- coding: utf-8 -*-
# @Author : feier
# @File : bicycle.py

class Bicycle:

    __key = True

    def __init__(self, model, color):
        # 自行车型号
        self.model = model
        # 自行车颜色
        self.color = color

    # 骑行方法
    def run(self, km):
        print(f"人力骑行了 {km} 公里")

    def open(self):
        if self.__key == True:
            print('开锁')
        else:
            print('没钥匙')


# 继承：父类名放到子类名后的括号中
class EBicycle(Bicycle):

    def __init__(self, model, color, valume):
        self.valume = valume
        super().__init__(model, color)

    # 展示电动自行车的信息
    def look_style(self):
        print(f"本车的型号为：{self.model},颜色为:{self.color}")

    # 充电
    def fill_charge(self, vol):
        # 当前电量 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        # 电动车最大电量 30 度
        if self.valume < 30:
            print(f"充了 {vol} 度电，现在的电量是 {self.valume} 度")
        else:
            raise Exception("充电太多了，装不下了～")

    # 骑行方法
    def run(self, km):
        # 获取目前电量可以走的里程数
        power_km = self.valume * 10
        # 骑行之后的剩余电量
        rest_valume = 0
        if power_km >= km:
            print(f"我用电力骑行了 {km} 公里")
            rest_valume = self.valume - km / 10
        else:
            print(f"我用电力骑行了 {power_km} 公里")
            print("没电了～")
            super(EBicycle, self).run(km-power_km)
        return rest_valume


if __name__ == '__main__':
    # bike = Bicycle("26", "red")
    # bike.run(10)
    ebike = EBicycle("26", "red", 10)
    ebike.look_style()
    ebike.fill_charge(5)
    rest_valume = ebike.run(100)
    print(f"剩余电量为 {rest_valume} 度")
    # print(ebike.__key)
    ebike.open()
