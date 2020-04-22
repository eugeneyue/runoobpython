#!/usr/bin/env python

import sys

# print("命令行参数为:")
# for i in sys.argv:
# 	print (i)
# print('\n python路径为', sys.path)

# str = input("Please enter one string:\n")
# print("The reverse one is " + str[-1::-1])

# def reverse(input):
	
# 	temp1 = input.split(" ")
# 	temp2 = temp1[-1::-1]
# 	output = ' '.join(temp2)
# 	return output

# if __name__ == '__main__':

# 	str = input("Please enter one string\n")
# 	print(reverse(str))

# a,b,temp = 0,1,1
# for i in range(0,11):
# 	print(temp,end=" ")
# 	temp = a + b
# 	a = b
# 	b = temp

# a,b = 0,1
# for i in range(0,11):
# 	print(b,end=" ")
# 	a,b = b,a+b

# number = -7
# while(1):
# 	guess = int(input("Please guess a number:\n"))
# 	if guess == number:
# 		print("Bingo!")
# 		break
# 	elif guess == 'q':
# 		break
# 	else:
# 		print("Please try again!")

# a = 0
# for i in range(1,101):
# 	a += i
# print(a)

# b,i = 0,1
# while i < 101:
# 	b += i
# 	i += 1
# print(b)

# count = 0
# while count < 5:
# 	print(count, "< 5")
# 	count += 1
# else:
# 	print(count, ">= 5")

# str = 'Runoob'
# for letter in str:
# 	if letter == 'b':
# 		break
# 	else:
# 		print(letter)

# for num in range(10,0,-1):
# 	if num == 5:
# 		break
# 	else:
# 		print(num)

# str = 'Runoob'
# for i in str:
# 	if i == 'o':
# 		# pass
# 		continue
# 	else:
# 		print(i, end="")

# a = 'pythyon'
# b = 2
# for i in a:
# 	if i == 'y':
# 		pass
# 		b = 3
# 	# else:
# 	# 	print(i + str(b))
# 	print(i + str(b))

# for i in range(2,10):
# 	for j in range(2,i):
# 		if (i % j == 0):
# 			print(str(i) + "不是质数")
# 			break
# 	else:
# 		print(str(i) + "是质数")

# for char in 'PYTHON STRING':
# 	if char == ' ':
# 		break
# 	if char == 'o':
# 		continue
# 	print(char, end="")

# list = [1,2,3,4]
# it = iter(list)
# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration:
# 		sys.exit()

# num = iter(list(range(1,101)))
# for i in num:
# 	print(str(i),end=" ")
# 	if i == 20:
# 		break
# 	

# a,b,temp = 0,1,0
# n = input("Please enter a count: ")
# for i in range(0,int(n)):
# 	temp = a+b
# 	a,b = b,a+b
# 	print(temp,end=" ")

def fibonacci(n):
	a,b,counter = 0,1,0
	while True:
		if counter > n:
			return
		yield a
		a,b = b, a+b
		counter += 1
f = fibonacci(10)
print(type(f))