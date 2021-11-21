"""
某群有多个成员，群主给成员发普通红包。发红包的规则是：
1、群主负责发红包。红包金额从群主余额中扣除，按成员人数平均分成n等份，以备领取。
每个红包的金额为整数，如果有余数则加到最后一个红包中。

2、成员负责抢红包。抢到的红包金额存到自己余额中。
3、抢完红包后需要进行报数，打印格式“我是XX，现在有 XX 块钱。”。

请根据描述信息，完成案例中所有类的定义，类之间的继承关系，以及发红包、抢红包的操作。
"""
import random

class Person:

    def __init__(self, money, name):
        self.money = money
        self.name = name

    # 报数
    def show(self):
        print(f"我是{self.name}，现在有 {self.money} 块钱。")


class Manager(Person):

    # 发红包
    # 1、群主负责发红包。
    # 红包金额从群主余额中扣除，
    # 按成员人数平均分成n等份，以备领取。
    # 每个红包的金额为整数，如果有余数则加到最后一个红包中。
    def send(self, money, num) -> list:
        red_list = []

        # 判断红包金额和余额的关系
        if money > self.money:
            print("没有钱，大家洗洗睡吧")
            return red_list

        # 扣钱
        self.money -= money

        # 包红包
        avg = money // num  # 3
        mod = money % num  # 1
        for i in range(num - 1):
            red_list.append(avg)
        red_list.append(avg + mod)

        print(red_list)
        return red_list


class Member(Person):

    # 抢红包
    # 2、成员负责抢红包。抢到的红包金额存到自己余额中。
    def grab(self, red_list):

        print(f"芝麻开门，手气最佳一定是：{self.name}")
        # 判断一把
        if not red_list:
            print("一块钱都不给。退群！")
            return None
        # 抢
        random_idx = random.randint(0, len(red_list) - 1)
        luck_money = red_list.pop(random_idx)

        # 赶紧存到我们都钱包
        self.money += luck_money

        return self.money


if __name__ == '__main__':
    print("="*10, "游戏开始", "="*10)

    manager = Manager(100, "子谦")
    a = Member(0, "耿")
    b = Member(0, "李盼")
    c = Member(0, "Pathfinder")

    manager.show()
    a.show()
    b.show()
    c.show()

    print("=" * 10, "开始发红包", "=" * 10)
    red = manager.send(money=10, num=3)

    print("=" * 10, "开始抢红包", "=" * 10)
    a.grab(red)
    b.grab(red)
    c.grab(red)

    print("=" * 10, "游戏结束，报数", "=" * 10)
    manager.show()
    a.show()
    b.show()
    c.show()
