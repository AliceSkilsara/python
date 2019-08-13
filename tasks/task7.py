# Проверьте, является ли введённое пользователем с клавиатуры натуральное число — простым.
# Постарайтесь не выполнять лишних действий (например, после того, как вы нашли хотя бы один
# нетривиальный делитель уже ясно, что число составное и проверку продолжать не нужно).
# Также учтите, что наименьший делитель натурального числа n, если он вообще имеется,
# обязательно располагается в отрезке [2; √n].
import math

number = int(input("Input your number: "))
d = 2
if (number > 2):
    while (d <= math.sqrt(number)):
        if number % d == 0:
            print("It is composite number")
            break
        d += 1
    else:
        print("It is a prime number")
else:
    print("Your number is too small")