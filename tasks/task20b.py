#В три переменные a, b и c явно записаны программистом три целых попарно неравных между собой числа. Создать программу,
# которая переставит числа в переменных таким образом, чтобы при выводе на экран последовательность a, b и c
# оказалась строго возрастающей.

a=int(input("Input first number: "))
b=int(input("Input second number: "))
c=int(input("Input third number: "))
list=[a,b,c]
print(list)
list.sort()
print(list)

