# # =====================Проблема 3====================== # DONE
# a = 2**3
# b = 3**2
# if a>b:
#     print(f"Число a = {a} больше чем b = {b}")
# else:
#     print(f"Число b = {b} больше чем a = {a}")


# # =====================Проблема 22======================
# a, b, c = map(int, input("Введите 3 числа a, b, c: ").split())
# if a > b and a > c:
#     print("Число a больше чем b и c")
# elif b > a and b > c:
#     print("Число b больше чем a и c")
# elif c > a and c > b:
#     print("Число c больше чем a и b")
# else:
#     print("Error")

# =====================Проблема 15======================
# # a, b, c = map(int, input("Введите 3 числа a, b, c: ").split())
# a = 17391
# b = 546
# c = 934
# if a % 17 > b % 17 and a % 17 > c % 17:
#     print("Число а больше, чем другие.")
# elif b % 17 > a % 17 and b % 17 > c % 17:
#     print("Число b больше, чем другие.")
# elif c % 17 > a % 17 and c % 17 > b % 17:
#     print("Число c больше, чем другие.")

# # =====================Проблема 39======================
# a = 13
# b = 172
# if a * a < b:
#     print(f"a^2 = {a*a} меньше чем b = {b}")
#     a = a * a * a
#     if a > b:
#         print(f"а^3 = {a} больше чем b = {b}")
#     else:
#         print(f"а^3 = {a} все еще меньше чем b = {b}")

# # =====================Проблема 5======================
# a = int(input("Введите число a :"))
# if a % 2 != 0:
#     print(f"Вы ввели нечетное число а.")
# else:
#     print(f"Вы ввели четное число а.")
# if a % 3 != 0:
#     print(f"Число a делится не 3 без остатка.")
# else:
#     print(f"Число a делится на 3 без остатка.")



# # =====================Проблема 3======================
# a = int(input("Введите любое число от 0 до 100 :"))
# if a >= 0 and a <= 21:
#     print("Ваше число в диапозоне до 21")
# elif a >= 57 and a <= 100:
#     print("Ваше число в диапозоне от 57 до 100")
# else:
#     print("Ваше число в недоступном диапозоне")



# # =====================Проблема 7======================
# if True or False:
#     print("Срабатывает при любом условии")



# # =====================Проблема 9======================
# a = int(input("Введите любое число: "))
# if a > 3:
#     if a > 4:
#         if a > 5:
#             if a > 6:
#                 print("Ваше число больше 6")
#             else:
#                 print("Ваше число 6")
# else:
#     print("Ваше число меньше 6")



# # =====================Проблема 45======================
# a = 10 // 5
# b = 10 // 5
# if a == b:
#     print("Число a и b равны.")
#     print("Сумма их равна", a+b)
# else:
#     print("Число a и b разные.")
#


# # =====================Проблема 33======================
# a = -4
# if a < 0:
#     print(a)
#

# # =====================Проблема 11======================
a = 10
b = 5
if a > 0 and b > 0:
    print("а и б больше ноля")

# # =====================Проблема 0======================

if a > b:
    print(a+2)
else:
    print(b+2)

