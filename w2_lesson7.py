#     # problem 1
# a = ['awesome', 'nine', ['k-pop'], 1.23, 123, {'one': 1}]
# check = []
# for x in a:
#     try:
#         s = set(x)
#         check.append(True)
#     except TypeError:
#         check.append(False)
# if all(check):
#     print('Данные можно конвертировать в Set')
# elif not all(check):
#     print('Данные нельзя конвертировать в Set')
#     # problem 2
# numbers = set()
# for x in range(5):
#     num = int(input('num: '))
#     numbers.add(num)
# print(min(numbers))
#     # problem 3
# func = input(''' ''')
# try:
#     eval(func)
# except:
#     print('Wrong')
# else:
#     print('Correct')

# problem 4
# credit = int(input('Сколько хотите взять в кредит?'))
# result = credit * (3.47 / 100)
# print('Переплата составила: ', round(result, 2))

# problem 1 and 2
# a = [10, 'text']
# try:
#     print(a[0]+a[1])
# except TypeError:
#     print('TypeError')
#
# try:
#     print(a[2])
# except IndexError:
#     print('IndexError')
#
# try:
#     print(b)
# except NameError:
#     print('NameError')

# # problem 3
# at = 10
# e = 15
# wo = 20
#
# for e in range(-at, at):
#     print(wo / e)
#     if at > 5:
#         print(f"{at} > 5")
#
#     # problem 4
# lst = []
# for i in range(10):
#     lst.append(i)
#     a = list(reversed(lst))
#     sls_obj = slice[0:8]
#     print(sls_obj)

    # problem 1
# a[1] = str(a[1])
# a.append({'dict': 1})
# lol = 20
# c = lol
# x = set(a)
# print(x)
# print(a[2])
# print(c)
