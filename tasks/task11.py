# Создайте программу, выводящую на экран все неотрицательные элементы последовательности 90 85 80 75 70 65 60 ….

def method(start):
    while start > 0:
        print(start)
        start -= 5


method(90)