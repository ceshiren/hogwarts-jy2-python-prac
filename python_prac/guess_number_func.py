# -*- coding: utf-8 -*-
# @Author : feier
# @File : guess_number_func.py
from random import randint


def user_input_num(input_msg, err_msg):
    '''
    定义用户输入整数方法
    :param input_msg: 输入时的提示信息
    :param err_msg: 用户输入错误的提示信息
    :return: 转化为整数类型的数字
    '''
    while True:
        user_num = input(input_msg)
        # 判断用户输入内容的类型
        if user_num.isdigit():
            user_num = int(user_num)
            break
        else:
            print(err_msg)
    return user_num


def guess_number(guess_num, target_num):
    '''
    猜数字
    :param guess_num: 允许的最多的猜数次数
    :param target_num: 要猜的目标数字
    :return:
    '''
    # 定义局部变量（定义在函数内容，作用域在本函数内）
    input_msg = "你猜猜 1～10 之间我选择的是哪个数字呀？"
    err_msg = "输入的不是整数喔，请重新输入～"
    # 循环允许的次数
    for i in range(guess_num):
        # 调用用户输入整数的方法
        user_num = user_input_num(input_msg, err_msg)
        # 判断用户输入的数字是否为与目标数字相等
        if user_num == target_num:
            # 如果猜对了，输出【恭喜你猜对啦～】
            print("恭喜你猜对啦～")
            # 跳出循环，完成猜字游戏
            break
        else:
            # 如果猜错了，前几次提供提醒信息
            if i != guess_num - 1:
                if user_num > target_num:
                    print(f"你猜的数字 {user_num} 比较大喔，再试试吧～")
                else:
                    print(f"你猜的数字 {user_num} 比较小喔，再试试吧～")
            else:
                # 最后一次如果猜错了，输出【猜错啦，正确答案是 X！】
                print(f"猜错啦，机会用完了～正确答案是 {target_num}！")
    # 最后输出【游戏结束】
    print("游戏结束")


if __name__ == '__main__':
    # 选择一个 [1, 10] 范围内的随机整数作为目标数字
    target_num = randint(1, 10)
    # 允许的最多猜数的次数
    guess_num = 3
    # 调用函数，函数名(参数)
    guess_number(guess_num, target_num)
