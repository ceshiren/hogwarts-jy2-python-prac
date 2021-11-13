# -*- coding: utf-8 -*-
# @Author : feier
# @File : guess_number.py

'''
判断用户输入内容的类型
提示用户猜测的数字与目标数字的大小关系
给 3 次猜数字的机会
'''

from random import randint

# 选择一个 [1, 10] 范围内的随机整数作为目标数字
target_num = randint(1, 10)
# 允许的最多猜数的次数
guess_num = 3
# 循环允许的次数
for i in range(guess_num):
    while True:
        # 提示用户输入一个 1 ~ 10 之间的整数
        user_num = input("你猜猜 1～10 之间我选择的是哪个数字呀？")
        if user_num.isdigit():
            user_num = int(user_num)
            break
        else:
            print("输入的不是整数喔，请重新输入～")

    # 判断用户输入的数字是否为与目标数字相等
    if int(user_num) == target_num:
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
