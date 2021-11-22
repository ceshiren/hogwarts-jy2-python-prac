# 写一个面向对象的例子：
# 比如创建一个类（Animal）【动物类】，
# 类里有属性（名称，颜色，年龄，性别），
# 类方法（会叫，会跑）
class Animal:
    name = ''
    color = ''
    age = ''
    gender = ''

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def speak(self):
        print("会叫")

    def run(self):
        print(f"{self.name} 会跑")


# 创建子类【猫】，继承【动物类】
class Cat(Animal):

    # 重写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender):
        super(Cat, self).__init__(name, color, age, gender)
    # 添加一个新的属性，毛发=短毛
        self.fur = '短毛'

    # 添加一个新的方法， 会捉老鼠
    def catch_mouse(self):
        print(f"{self.name}会捉老鼠")

    # 重写父类的【会叫】的方法，改成【喵喵叫】
    def speak(self):
        print("喵喵叫")


# 创建子类【狗】，继承【动物类】
class Dog(Animal):

    # 复写父类的__init__方法，继承父类的属性
    def __init__(self, name, color, age, gender):
        super(Dog, self).__init__(name, color, age, gender)

    # 添加一个新的属性，毛发=长毛
        self.fur = '长毛'

    # 添加一个新的方法， 会看家
    def house_keeping(self):
        print(f"{self.name}会看家")

    # 复写父类的【会叫】的方法，改成【汪汪叫】
    def speak(self):
        print("汪汪叫")


# 在入口函数中创建类的实例
if __name__ == '__main__':
    # 创建一个猫猫实例
    cat = Cat('波斯', '橘黄', 2, '公的')

    # 调用捉老鼠的方法
    cat.catch_mouse()

    # 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    print(cat.name, cat.color, cat.age, cat.gender, "捉到了老鼠")
    print(f"名字：{cat.name}, 颜色：{cat.color}, 年龄：{cat.age}, "
          f"性别：{cat.gender}, 毛发:{cat.fur}, 捉到了老鼠。")

    # 创建一个狗狗实例
    dog = Dog('旺财', '黑色', 3, '母的')

    # 调用【会看家】的方法
    dog.house_keeping()

    # 打印【狗狗的姓名，颜色，年龄，性别，毛发】
    print(dog.name, dog.color, dog.age, dog.gender, dog.fur)
    print(f"狗狗的姓名：{dog.name}，颜色：{dog.color}，年龄：{dog.age}，性别：{dog.gender}，毛发:{dog.fur}")
