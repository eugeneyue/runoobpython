# !/usr/bin/env python3

from math import pi
import math,copy
from collections import deque
import sys
#from fibo import fib,fib2
#from fibo import *
import fibo
from datetime import date
import random
import unicodedata
import calendar

# def area(length=0,height=0):
#     return int(length)*int(height)

# #print("The numbr of the area is %d" % area(2,2))
# l,h= 2,2
# print("length=",l, "height=", h, "area=", area(l,h) )
# print(area())

# def fun(a):
#     a = 3
#     return int(a)+3

# a = 4
# print(fun(a))
# print(a)

# def fun2(c):
#     temp = len(c)
#     c[temp-1] = 2
#     return c

# b = [1,2,3]
# print(fun2(b))
# print(b)

# def printinfo(arg1,*vartuple):
#     print(arg1)
#     print(vartuple)
#     print(type(vartuple))
# printinfo(70,60,50)

# def printinfo2(arg1, **vardict):
#     print(arg1)
#     #print(vardict)
#     for key,values in vardict.items():
#         print(key,values)
#     print(type(vardict))
# printinfo2(1, a=2, b=3)

# def f(a,b,*,c):
#     return a+b+c
# print(f(1,2,c=3))

# sum = lambda arg1, arg2=0 : arg1 + arg2
# print(sum(10))

# def f(a,b,c,d,*,e,f):
#     print(a,b,c,d,e,f)
# f(10,20,c=30,d=40,e=50,f=60)

#print(pi)
# print(math.pi)

# num = [1,2,3]
# print(tuple(num))

# a = [1,2,3]
# a[len(a):] = [4]
# print(a)
# print(len(a))
# a.pop(1)
# print(a)
# print(a.index(1))
# t = (4,5,8,1)
# a.extend(t)
# print(a)
# print(sorted(a))
# print(a)

# b = [1, 3, 4, 5, 8, 1]
# b.reverse()
# print(b)

# c = [1, 3, 4, 5, 8, 1]
# c2 = deque(c)
# c2.popleft()
# print(c2)

# ver = [1,2,3]
# output = [x*3 for x in ver]
# print(output)
# output2 = [x*3 for x in ver if x>=3]
# print(output2)

# matrix,temp = [[1,2,3,4],[5,6,7,8],[9,10,11,12]],[]
# for i in range(0,3):
#     temp.extend([j for j in matrix[i]])
# print(temp)

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# for row in matrix:
#     print(row)
# print(matrix[0][0])
# print(type(matrix))

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# list1,list2,list3 = [],[],[]
# for i in range(4):
#     for j in range(3):
#         list1.append(matrix[j][i])
#     list2.append(list1)
#     list3 = copy.deepcopy(list2)
#     list2 = list3
#     list1.clear()
# print(list3)

# test,add = [],[1,2]
# test.append(add)
# add.clear()
# print(test)

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# result = [[row[i] for row in matrix] for i in range(4)]
# print(result)

# matrix,transposed = [[1,2,3,4],[5,6,7,8],[9,10,11,12]],[]
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# print(transposed)

# matrix,transposed = [[1,2,3,4],[5,6,7,8],[9,10,11,12]],[]
# for i in range(4):
#     temp = []
#     for row in matrix:
#         temp.append(row[i])
#     transposed.append(temp)
# print(transposed)

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# list1,list2 = [],[]
# for i in range(4):
#     for j in range(3):
#         list1.append(matrix[j][i])
#     list2.append(list1)
#     list1 = []
#     # print(id(list1))
# print(list2)

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# list1,list2 = [],[]
# for i in range(4):
#     for j in range(3):
#         list1.append(matrix[j][i])
#     list2.append(list1)
#     list1.clear()
#     #print(id(list1))
#     print(id(list2))
# print(list2)

# dictionary = {x:x**2 for x in (2,4,6)}
# print(dictionary)

# print(dict(sape=4139,guido=4127))

# knights = {'gallahad': 'The pure', 'robin':'The brave'}
# for k,v in knights.items():
#     print(k,v)

# for i,v in enumerate(['tic','tac','toe']):
#     print(i,v)

# a = [1,2,3]
# b = [4,5,6]
# for x,y in zip(a,b):
#     print("{0} + 3 = {1}".format(x,y))

# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)
# print('\nPython Path:',sys.path)

# local = fibo.fib
# fibo.fib(100)
# local(100)

# if __name__ == '__main__':
#     fibo.fib(100)

# for x in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# table = {'Google': 1, 'Runoob': 2, 'Taobao':3}
# for name,number in table.items():
#     print('{0:10} ==> {1:10}'.format(name,number))

# num = 3.1415926
# num1 = 5
# num2 = 1000
# num3 = 0.25
# print('{:.3f}'.format(num))
# print('{:+.2f}'.format(num))
# print('{:0<4d}'.format(num1))
# print('{:,}'.format(num2))
# print('{:.0%}'.format(num3))

# f = open("c:/Users/gtxcdn2/Desktop/learn/foo.txt","w")
# f.write("Python \nYes \nGood!")
# f.close()
# f = open("c:/Users/gtxcdn2/Desktop/learn/foo.txt","r")
# str = f.read()
# print(str)
# f.close()

# f = open("c:/Users/gtxcdn2/Desktop/learn/foo.txt","r")
# str = f.readlines()
# print(str)
# f.close()

# f = open("c:/Users/gtxcdn2/Desktop/learn/foo1.txt","a")
# value = ('www.runoob.com', 14)
# s = str(value)
# f.write(s)
# f.close()
# f = open("c:/Users/gtxcdn2/Desktop/learn/foo1.txt","r")
# result = f.read()
# print(result)
# f.close()

# with open('c:/Users/gtxcdn2/Desktop/learn/foo1.txt','r') as target:
#     result = target.read()
#     print(result)

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip)
#     f.close()
# except OSError as err:
#     print("OS Error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexcepted error:", sys.exc_info()[0])
#     raise

# for arg in sys.argv[1:]:
#     try:
#         # f = open('c:/Users/gtxcdn2/Desktop/learn/foo1.txt','w')
#         f = open(arg,'a')
#     except IOError as err:
#         print("Cannot open this file.")
#     else:
#         writetest = '\ntest'
#         f.write(writetest)
#         f.close()

# class Myclass():
#     """一个简单的类实例"""
#     i = 123456
#     def f(self):
#         return 'hello world'
# x = Myclass()
# print("Myclass类的属性i为：",x.i)
# print("Myclass类的方法f输出为：",x.f())

# class complex():
#     def __init__(self,real,fake):
#         self.r = real
#         self.f = fake

# x = complex(3.0,-4.5)
# print(x.r,x.f)

#---------------------------------------------------------------------------------------------------------

# class people:
#     name = ''
#     age = 0
#     __weight = 0
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s says: 'I am %d years old and weigh %d kg.'" %(self.name,self.age,self.__weight))
# # p = people('Runoob',10,30)
# # p.speak()

# class student(people):
#     grade = 0
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print("%s says: I am %d years old and in %dth grade" %(self.name,self.age,self.grade))
# # s = student('ken',10,60,3)
# # s.speak()

# class speaker:
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak1(self):
#         print("I am %s and my topic is %s" %(self.name,self.topic))

# class sample(speaker,student):
# # class sample(student,speaker):
#     a = ''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
#         # super(sample,self).__init__(n,a,w,g) #并没有覆盖父类的init方法
#         # super(sample,self).__init__(n,t)

# test = sample("Tim",25,80,4,"Python")
# test.speak1()

#---------------------------------------------------------------------------------------------------------

# class Parent():
#     def myMethod(self):
#         print("调用父类\n")
# class Child(Parent):
#     def myMethod(self):
#         # print("调用子类\n")
#         # super().myMethod()
#         super(Child,self).myMethod()
# c = Child()
# c.myMethod()
# super(Child,c).myMethod()
# super().myMethod()

# class A():
#     def add(self,x):
#         y = x + 1
#         print(y)
# class B(A):
#     def add(self,x):
#         super().add(x)
# c = B()
# c.add(2)

#---------------------------------------------------------------------------------------------------------

# class Bird:
#     def __init__(self):
#           self.hungry = True
#     def eat(self):
#           if self.hungry:
#                print ('Ahahahah')
#           else:
#                print ('No thanks!')

# class SongBird(Bird):
#      def __init__(self):
#           Bird.__init__(self)
#           self.sound = ('Squawk')
#      def sing(self):
#           print ("sing")

# sb = SongBird()
# sb.sing()    # 能正常输出
# sb.eat()     # 报错，因为 songgird 中没有 hungry 特性

#---------------------------------------------------------------------------------------------------------
# 菱形继承
# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')


# class B(A):
#     def __init__(self):
#         print('enter B')
#         super().__init__()
#         print('leave B')


# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')


# # class D(B, C):
# class D(C,B):
#     def __init__(self):
#         print('enter D')
#         super().__init__()           # 不像经典类继承方法一样分开写，super只要写一遍就行
#         print('leave D')

# d = D()
# super 广度优先
# 跟随子类的继承顺序
# D(B,C): D - B - C - A - A - C - B - D
# D(C,B): D - C - B - A - A - B - C - D
#---------------------------------------------------------------------------------------------------------

# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')

# class B(A):
#     def __init__(self):
#         print('enter B')
#         A.__init__(self)
#         print('leave B')


# class C(A):
#     def __init__(self):
#         print('enter C')
#         A.__init__(self)
#         print('leave C')


# class D(C,B):
#     def __init__(self):
#         print('enter D')
#         B.__init__(self)                                # BC的顺序决定深度优先的顺序
#         C.__init__(self)
#         print('leave D')

# d = D()

# 父类.__init__(self,参数) => 深度优先
# 跟随构造函数中的继承顺序
# D(C,B): D - B - A - A - B - C - A - A - C - D
#---------------------------------------------------------------------------------------------------------

# class JustCounter():
#     __secretCount = 0
#     publicCount = 0

#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount) #私有属性无法访问
#---------------------------------------------------------------------------------------------------------

# if True:
#     msg = 'True'
# print(msg)

#---------------------------------------------------------------------------------------------------------

# num = 1
# def fun():
#     global num
#     print(num)
#     num = 123
#     print(num)
# fun()
# print(num)

#---------------------------------------------------------------------------------------------------------

# def outer():
#     num = 10
#     def inner():
#         nonlocal num
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

#---------------------------------------------------------------------------------------------------------

# a = 10
# def test():
#     global a
#     a += 1
#     print(a)
# test()

#---------------------------------------------------------------------------------------------------------

# now = date.today()
# print(now)

# birthday = date(1994,12,24)
# age = now - birthday
# print(age)

#---------------------------------------------------------------------------------------------------------

# Python Hello World 实例
# str = 'Hello World'
# print(str)

# Python 数字求和
# numbers,sum = [0,0],0
# for num in numbers:
#     numbers[num] = int(input("Please input the number:\n"))
#     sum += numbers[num]
# print("The sum of the two numbers is %d" %sum)

# Python 平方根
# num = 12
# print("%.2f" % math.sqrt(num))

# Python 二次方程
# print("计算的是一元二次方程ax**2 + bx + c = 0\n")
# a,b,c,d,result1,result2 = 0,0,0,0,0,0
# a = float(input("请输入a:\n"))
# b = float(input("请输入b:\n"))
# c = float(input("请输入c:\n"))
# d = (b**2) - (4*a*c)
# result1 = (-b + math.sqrt(d)) / (2*a)
# result2 = (-b - math.sqrt(d)) / (2*a)
# print("结果是{0}和{1}".format(result1,result2))

# Python 计算三角形的面积
# a = float(input("请输入a边长:\n"))
# b = float(input("请输入b边长:\n"))
# c = float(input("请输入c边长:\n"))
# s = (a + b + c)/2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print("%.2f" % area)

# Python 计算圆的面积
# r = float(input("请输入半径长:\n"))
# s = pi*(r**2)
# print("圆面积为：%.3f" % s)

# Python 随机数生成
# s = random.randint(1,2) #两个参数，从1~2包含1和2
# print(s)

# Python 摄氏温度转华氏温度
# c = float(input("请输入摄氏度:\n"))
# f = (c * 1.8) + 32
# print("华氏度是%.1f度" % f)

# Python 交换变量
# a = input("请输入a:\n")
# print("a = {0}".format(a))
# b = input("请输入b:\n")
# print("b = {0}".format(b))
# a,b = b,a
# print("a = {0}".format(a))
# print("b = {0}".format(b))

# Python if 语句
# print("以下代码判断数字是正数、负数还是0\n")
# a = int(input("请输入数字a:\n"))
# if a < 0:
#     print("Negative")
# elif a == 0:
#     print("0")
# else:
#     print("Positive")

# Python 判断字符串是否为数字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except(TypeError,ValueError):
#         pass
#         # print("Error")

#     try:
#         import unicodedata
#         print(s)
#         unicodedata.numeric(s)
#         print(s)
#         return True
#     except(TypeError,ValueError):
#         pass
#     return False

# print(is_number('四'))
# print(is_number('1'))
# print(is_number('foo'))
# print(is_number('1.3'))     #因为是float啊！！！！
# print(is_number('-1.37'))   #因为是float啊！！！！
# print(is_number('1e3'))     #因为是float啊！！！！

# Python 判断奇数偶数
# num = int(input("请输入一个大于等于0的整数：\n"))
# if num%2 == 0:
#     print("Even")
# elif num%2 != 0:
#     print("odd")
# else:
#     print("Wrong type")

# Python 判断闰年
# 整百年能被400整除的是闰年
# 非整百年能被4整除的是闰年
# num = int(input("请输入一个年份：\n"))
# if num%100 == 0:
#     if num%400 == 0:
#         print("闰年Leap year")
#     else:
#         print("不是闰年Leap year")
# elif num%4 == 0:
#     print("闰年Leap year")
# else:
#     print("不是闰年Leap year")

# Python 获取最大值函数
# numlist = [0,0,0,0,0]
# 方法一
# for i in range(len(numlist)):
#     numlist[i] = int(input("请输入数字:\n"))
# print(numlist)
# print(max(numlist))
# 方法二
# def getmax(list):
#     for x in range(len(list)):
#         for y in range(len(list)-x-1):
#             if list[y] > list[y+1]:
#                 list[y],list[y+1] = list[y+1],list[y]
#     return(list)
# for i in range(len(numlist)):
#     numlist[i] = int(input("请输入数字:\n"))
# print("原始的列表是：{0}".format(numlist))
# print("排序后的列表是: {0}".format(getmax(numlist)))
# print("最大值是: {0}".format(numlist[len(numlist)-1]))

# Python 质数判断
# 一个大于1的自然数，除了1和它本身以外不再有其他的因数
# num = int(input("请输入数字进行判断:\n"))
# if num > 1:
#     for i in range(2,num):
#         if (num % i) == 0:
#             print("{0}不是质数".format(num))
#             print("{0} x {1} = {2}".format(i,num//i,num))        #整除
#             break
#     else:
#         print("{0}是质数".format(num))
# else:
#     print("既不是质数也不是合数")

# 输出100以内的质数
# temp,result = [],[]
# for a in range(2,101):
#     temp.append(a)

# for i in temp:
#     for j in range(2,i):
#         if i % j == 0:
#             print(j)
#             break
#     else:
#         result.append(i)
#         """
#         当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码；
#         如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
#         """
# print("Temp:", temp)
# print("Result:", result)

# Python 输出指定范围内的素数
# temp,result = [],[]
# start = int(input("请设置起始（大于1的整数）：\n"))
# finish = int(input("请设置结束（大于1的整数且不小于起始）：\n"))
# while start<=finish:
#     for a in range(start,finish+1):
#         temp.append(a)

#     for i in temp:
#         for j in range(start,i):
#             if i % j == 0:
#                 break
#         else:
#             result.append(i)
#             """
#             当迭代对象完成所有迭代后且此时的迭代对象为空时，如果存在else子句则执行else子句，没有则继续执行后续代码；
#             如果迭代对象因为某种原因（如带有break关键字）提前退出迭代，则else子句不会被执行，程序将会直接跳过else子句继续执行后续代码
#             """
#     print("结果:", result)
#     break
# else:
#     print("请输入正确的范围！")

# Python 阶乘实例
# print("***本代码提供阶乘计算服务***")
# num = int(input("请输入要进行计算的整数： "))
# result = 1
# for i in range(1,num+1):
#     result *= i
# print("结果是：{0}".format(result))

# Python 九九乘法表
# 方法一：
# for i in range(1,10):
#     for j in range(1,10):
#         print("{0}*{1}={2} ".format(i,j,i*j),end=" ")
#     print('\n')
# 方法二：
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}*{1}={2} ".format(i,j,i*j),end=" ")
#     print('\n')

# Python 斐波那契数列
# print("***本代码输出100以内的Fibonacci***")
# a,b,i = 0,1,0
# while i <= 100:
#     print("%d" % a,end=" ")
#     a,b,i = b,a+b,a
# print("***本代码输出10项Fibonacci***")
# a,b = 0,1
# for i in range(10):
#     print("%d" % a,end=" ")
#     a,b = b,a+b

# Python 阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
# print("***本代码输出1000以内的阿姆斯特朗数***")
# sum = 0
# for i in range(1,10001):
#     temp = str(i)
#     length = len(temp)
#     for j in temp:
#         sum += int(j)**length
#     if sum == i:
#         print(i,end=" ")
#     sum = 0

# Python 十进制转二进制、八进制、十六进制
# print("***本代码输出进制转换结果***")
# dec1 = int(input("请输入一个十进制数： "))
# print("对应的十进制是：", dec1)
# print("对应的二进制是：", bin(dec1))
# print("对应的八进制是：", oct(dec1))
# print("对应的十六进制是：", hex(dec1))

# Python ASCII码与字符相互转换
# list1,list2,list3 = [],[],[]
# for i in range(11):
#     list1.append(i)
# for j in list1:
#     list2.append(chr(j))
# print(list2)
# for k in list2:
#     list3.append(ord(k))
# print(list3)

# Python 最大公约数算法
# 最大公约数指两个或多个整数共有约数中最大的一个
# 辗转相除法
# a = int(input("请输入一个正整数："))
# b = int(input("请再输入一个正整数："))
# def zdgys(a,b):
#     while a%b != 0:
#         a,b = b,a%b
#     print("最大公约数是{0}".format(b))
# if a < b:
#     a,b = b,a
#     zdgys(a,b)
# elif a == b:
#     print("最大公约数是{0}".format(a))
# else:
#     zdgys(a,b)

# Python 最小公倍数算法
# 两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数。甲、乙两数的积一定等于甲、乙两数的最大公因数与最小公倍数的积。
# a = int(input("请输入一个正整数："))
# b = int(input("请再输入一个正整数："))
# def zdgys(a,b):
#     while a%b != 0:
#         a,b = b,a%b
#     return b
# result = a*b//zdgys(a,b)
# print("最小公倍数是：{0}".format(result))

# Python 简单计算器实现
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multi(x,y):
#     return x*y
# def div(x,y):
#     if y == 0:
#         return "分母不能为0"
#     else:
#         return x/y
# print("***请选择加减乘除其中一个计算方法***\n")
# print("加1减2乘3除4\n")
# choice = int(input("请输入对应数字："))
# a = int(input("请输入一个数："))
# b = int(input("请再输入一个数："))
# if choice == 1:
#     print(add(a,b))
# elif choice == 2:
#     print(sub(a,b))
# elif choice == 3:
#     print(multi(a,b))
# elif choice == 4:
#     print(div(a,b))
# else:
#     print("1234")

# Python 生成日历
# a = int(input("请输入年份："))
# b = int(input("请再输入月份："))
# print('\n')
# print(calendar.month(a,b))

# Python 使用递归斐波那契数列 - 递归非常的浪费性能
# def recur_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return(recur_fibonacci(n-1) + recur_fibonacci(n-2)) # 计算上一项和上上项的和
# num = int(input("请输入要输出几项: "))
# if num <= 0:
#     print("请输入大于0的整数")
# else:
#     for i in range(num):
#         print(recur_fibonacci(i),end=" ")

# Python 文件 IO
# with open(r'C:\Users\gtxcdn2\Desktop\runoob\foo.txt','a+') as target:
#     # print(target.read())
#     target.write('\ntest0424')

# Python 字符串判断
# Python 字符串大小写转换
# Python 计算每个月天数
# Python 获取昨天日期
# Python list 常用操作
# Python 约瑟夫生者死者小游戏
# Python 五人分鱼
# Python 实现秒表功能
# Python 计算 n 个自然数的立方和
# Python 计算数组元素之和
# Python 数组翻转指定个数的元素
# Python 将列表中的头尾两个元素对调
# Python 将列表中的指定位置的两个元素对调
# Python 翻转列表
# Python 判断元素是否在列表中存在
# Python 清空列表
# Python 复制列表
# Python 计算元素在列表中出现的次数
# Python 计算列表元素之和
# Python 计算列表元素之积
# Python 查找列表中最小元素
# Python 查找列表中最大元素
# Python 移除字符串中的指定位置字符
# Python 判断字符串是否存在子字符串
# Python 判断字符串长度
# Python 使用正则表达式提取字符串中的 URL
# Python 将字符串作为代码执行
# Python 字符串翻转
# Python 对字符串切片及翻转
# Python 按键(key)或值(value)对字典进行排序
# Python 计算字典值之和
# Python 移除字典点键值(key/value)对
# Python 合并字典
# Python 将字符串的时间转换为时间戳
# Python 获取几天前的时间
# Python 将时间戳转换为指定格式日期
# Python 打印自己设计的字体
# Python 二分查找
# Python 线性查找
# Python 插入排序
# Python 快速排序
# Python 选择排序
# Python 冒泡排序
# Python 归并排序
# Python 堆排序
# Python 计数排序
# Python 希尔排序
# Python 拓扑排序

#---------------------------------------------------------------------------------------------------------