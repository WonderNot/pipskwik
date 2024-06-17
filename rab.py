# import random
# import json


# # 4.1
# st1 = "today is monday"
# st2 = "tomorrow is friday"
# print(st1.replace("monday", "friday"))
# print(st1.replace("friday", "monday"))
# # 4.2
# st12 = "haha! hehe! hoho!"
# print(st12.split(" "))
# print(st12.replace("! ", ", "))
# # 4.3
# str1 = str(input("polindrom: "))
# str2 = str1[::-1]
# print(str1 == str2)
# # 4.4
# str3 = str(input("почта: "))
# print(str3.split("@"))
# # 4.5
# st_1 = input("what: ")
# st_2 = input("what search: ")

# ls = ['yellow', 'green', 'red']
# ls1 = ls[::-1]
# ls2 = input().split()
# ls1 = ls1 + ls2
# s = ls1[::-1]
# print(s)

# amount_zero = int(input("Digit "))
# zero = 0
# list_zero = list(str(zero))
# a = list_zero * amount_zero
# print(a)

# st_1 = input("word1: ")
# st_2 = input("word2: ")
# a=list(st_1+st_2)
# print(a)
# a1=[st_1,st_2]
# print(a1)

# ls = input().split()
# ls[1]='yellow'
# print(ls)

# ls1 = ['cat', 'dog', 'pig', 'rabbit']
# ls1.append('rat')
# ls1 = ls1[::-1]
# ls1.append('turtle')
# print(ls1)
# ls1 = ['cat', 'rabbit', 'elephant']
# print(ls1)
# l1 = len(ls1[0])
# l2 = len(ls1[1])
# l3 = len(ls1[2])
# ls2 = [l1, l2, l3]
# print(ls2)
# cat=ls1[0]
# cat=cat[::-1].capitalize()
# cat=cat[::-1]
# rab=ls1[1]
# rab=rab[::-1].capitalize()
# rab=rab[::-1]
# el=ls1[2]
# el=el[::-1].capitalize()
# el=el[::-1]
# print(cat,rab,el)
# 3.10
# lst_1 = list(range(1, 6))
# mx = max(lst_1)
# mn = min(lst_1)
# lst_2 = [max(lst_1), 2, 3, 4, min(lst_1)]
# print(lst_2)
# 3.11
# lst_1 = list(range(1, 6))
# print(sum(lst_1))
# 3.12
# lst_1 = list(range(1, 6))
# mx = lst_1.index(max(lst_1))
# mn = lst_1.index(min(lst_1))
# lst_1[mx] = sum(lst_1)
# lst_1[mn] = sum(lst_1)
# print(lst_1)
# lst_1 = list(range(1, 6))
# lst_2=lst_1.copy()
# lst_1[0]=sum(lst_1)
# lst_1[-1]=sum(lst_2)
# print(lst_1)
# 3.13
# lst_1 = list(range(0, 11, 2))
# lst_2 = list(range(1, 10, 2))
# print(lst_1, " ", lst_2)
# 3.14
# lst_1 = list(range(0, 101, 10))
# lst_2 = list(range(0, 100, 3))
# print(lst_1, " ", lst_2)
# 3.15
# lst_1 = list(range(30, 13, -2))
# lst_2 = lst_1[-1:-4:-1]
# print(lst_1, " ", lst_2)
# 4.1
# str_1 = input("str1: ")
# str_2 = input("str2: ")
# if str_2 in str_1:
#     print("here")
# else:
#     print("not here")
# 4.2
# str_1 = input("str1: ")
# if str_1.count("f") == 1:
#     print(str_1.index("f"))
# elif str_1.count("f") >= 2:
#     print(str_1.rindex("f"), " ", str_1.index("f"))
# 4.3
# str_1 = input("str1: ")
# if len(str_1) % 2 == 0:
#     print("even")
# else:
#     print("odd")
# 4.4
# age = int(input("Age: "))
# if age == 0:
#     print("wrong age")
# elif age <= 18:
#     print("cola")
# else:
#     print("beer")
# 4.5
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a + b >= c and a + c >= b and c + b >= a:
#     print("triangle")
# 4.6
# x = int(input("1: "))
# y = int(input("2: "))
# if x > 0:
#     if y > 0:
#         print("1")
#     if y < 0:
#         print("4")
# elif x < 0:
#     if y > 0:
#         print("2")
#     if y < 0:
#         print("3")
# 4.7
# month = int(input("month: "))
# if month >= 1 and month <= 2 or month == 12:
#     print("wint")
# elif month >= 3 and month <= 5:
#     print("spri")
# elif month >= 6 and month <= 8:
#     print("summ")
# elif month >= 9 and month <= 11:
#     print("aut")
# else:
#     print("invalid num")
# 4.7
# str_1 = input("1: ")
# str_2 = input("2: ")
# str_3 = input("3: ")
# if str_1 == 'python':
#     print(str_1)
# elif str_2 == 'python':
#     print(str_2)
# elif str_3 == 'python':
#     print(str_3)
# else:
#     print("invalid")
# 4.8
# a = random.randint(0, 10)
# choc = random.randint(0, 10)
# if a % 2 == 0:
#     print("going")
#     if choc >= 5:
#         print("pol i alex")
#     elif choc >= 2:
#         print("pol")
#     else:
#         print("not enough choc")
# else:
#     print("not")
# 4.9
# shield = input("shield: ")
# armor = input("armor: ")
# r = "red"
# y = "yellow"
# b = "black"
# if armor != r and shield != b:
#     print("true")
# else:
#     print("false")
# 5.2
# l = int(input("how much: "))
# for i in range(l):
#     print('accept')
# 5.3
# l = int(input("how much: "))
# for i in range(1, l + 1):
#     print(i)
# 5.4
# a = int(input("1: "))
# b = int(input("2: "))
# if a > b:
#     for i in range(b, a+1):
#         print(i)
# if a < b:
#     for i in range(a, b+1):
#         print(i)
# 5.5
# a = int(input("line: "))
# for i in range(a):
#     print("*" * a)
# 5.4
# a = int(input("1: "))
# b = int(input("2: "))
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         print(i)
# 5.7
# str_1 = str(input("string: "))
# for i in str_1:
#     print(i * 2)
# 5.8
# str_1 = str(input("string: "))
# for i in enumerate(str_1):
#     print(i)
# 5.9
# a = int(input("1: "))
# b = int(input("2: "))
# if b > a:
#     for i in range(a, b + 1):
#         if i % 2 == 0 and i % 7 == 1:
#             print(i)
# if a > b:
#     for i in range(b, a + 1):
#         if i % 2 == 0 and i % 7 == 1:
#             print(i)
# primer
# a = int(input("1: "))
# b = [print(2 ** i) for i in range(0, a)]
# 5.10
# a = int(input("1: "))
# b = int(input("2: "))
# count = 0
# for i in range(a, b + 1):
#     count += i
# print(count)
# 5.11
# n = int(input("1: "))
# bow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# for i in range(0, n):
#     print(bow[i].capitalize())
# 5.12
# a = int(input("1: "))
# b = int(input("2: "))
# count = 0
# for i in range(a, b + 1):
#     count += i ** 2
# print(count)
# c = [int(i) for i in input().split()]
# b = [print(i ** 2) for i in c if i % 2 != 0]

# c = [int(i) for i in input().split()]
# b = [print(int(i)) for i in c if i > 5]

# 5.15
# n = int(input("1: "))
# str_1_1 = ""
# for i in range(n):
#     str_1 = str(input(f"строка {i+1} "))
#     str_1_1 += str_1+' '
# print(str_1_1)

# 6.1
# n = 1
# while n <= 10:
#     print(n ** 2)
#     n += 1
# 6.2
# first = int(input("1: "))
# last = int(input("2: "))
# count = 0
# while first <= last:
#     a = (0.1 * first)
#     first += a
#     count += 1
# print(count)
# 6.3
# a = []
# n = int(input())
# while n != 0:
#     a.append(n)
#     n = int(input())
# print(a)
# 6.4
# a = range(0, 21)
# sum = 0
# for i in a:
#     if i % 10==0:
#         sum += i
# print(f"sum {sum}")
# 6.4.1
# n = 12345678
# summ = 0
# while n > 0:
#     summ += n % 10
#     n = n // 10
# print(summ)
# 6.5
# a = input().split()
# b = [10,24,40,52,60]
# b.reverse()
# for i in b:
#     if i % 10 == 0:
#         print(b.index(i))
#         break
# 6.6
# lst = [1230, 240, 1148, 52]
# count = 0
# for i in lst:
#     if i % 10 == 0:
#         count += 1
# print(count)
# 6.6
# b = 2671537259
# lst = []
# count = 0
# while b > 0:
#     i = b % 10
#     b = b // 10
#     lst.append(i)
# lst.reverse()
# print(lst)
# for i in lst:
#     if lst[i] > lst[i - 1]:
#         count += 1
# print(count)
# 6.11

# z1
# a = int(input("bottom "))
# b = int(input("top "))
# h = int(input("anna sleeps: "))
# if a <= b:
#     if h > b:
#         print("oversleep")
#     elif h < a:
#         print("nedosleep")
#     else:
#         print("normal")
# z2
# a = int(input("year: "))
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print("vesoc")
#
# else:
#     print("no")
# z3
# s = input("type ")
# if s == "triangle":
#     a = int(input("a "))
#     b = int(input("b "))
#     h = int(input("h "))
#     p = (a + b + h) / 2
#     print((p * (p - a) * (p - b) * (p - h)) ^ 1 / 2)
# if s == "rectangle":
#     a = int(input("a "))
#     b = int(input("b "))
#     print(a * b)
# if s == "circle":
#     r = int(input("r "))
#     print(3.14 * (r) ^ 2)
# z3
# a = int(input("a "))
# b = int(input("b "))
# h = int(input("h "))
# lst = [a, b, h]
# lsr1 = sorted(lst)
# print(lsr1[2], lsr1[0], lsr1[1])
# z4
# a = int(input("a "))
# if -15 < a <= 12 or 14 < a < 17 or a >= 19:
#     print("yes")
# else:
#     print("no")
# z4
# a = 5
# sum = 0
# while a != 0:
#     a = int(input())
#     sum += a
# print(sum)
# z5
# while True:
#     a = int(input())
#     if a > 100:
#         break
#     elif a < 10:
#         continue
#     else:
#         print(a)
# a = int(input("a "))
# b = int(input("b "))
# lst = list(range(a, b + 1))
# sum = 0
# count = 0
# for i in lst:
#     if i % 3 == 0:
#         sum += i
#         count += 1
# print(sum / count)
# z6
# c = [int(i) for i in input().split()]
# sum = 0
# for i in c:
#     sum += i
# print(sum)
# z7
# c = [int(i) for i in input().split()]
# for i in c:
#     count = 0
#     for j in c:
#         if j == i:
#             count += 1
#         if count == 2:
#             print(j)
# z8
# a = int(input("a "))
# s1 = []
# for i in range(1, a + 1):
#     for j in range(i):
#         s1.append(i)
# print(*s1[:a])

# kartege
# tpl = tuple()
# tpl1 = 1, 2, 3, 'a'
# tpl2 = ()
# tpl3 = tuple("djvf", )
# a, b, c = tuple
# change
# a = 1, 3, 2, ["jwvhev", "fjewefj", 1]
# a[3][-1] = 2
# print(a[3])

# 7.1
# m = ''
# n = ''
# a = [i for i in input().split()]
# b = [i for i in input().split()]
# for i in a:
#     if i.count("@") == 1:
#         m = i
# for i in b:
#     if i.count("@") == 1:
#         n = i
#
# tp = (m, n,)
# print(tp)
# 7.4
# a = 1, 3, 2, 4, 5, 6, 7, 8, 9
# print(sum(a))
# 7.5
# list_letters = "aeyuoi"
# a = tuple(input("tuple "))
# count = 0
# c=[]
# for i in a:
#     for j in list_letters:
#         if i == j:
#             c.append(j)
# print(f"{c[0]}- {a.count(c[0])}, {c[1]}-{a.count(c[1])}")

# dict
# a = dict()
# new_dict = {1: ["mama", 'pip', 'pop']}
# print(new_dict.keys(), new_dict.values())
# d = dict(short="evr", long=1)
#
#
# d1 = {a: a ** 2 for a in range(3)}
# up
# dict1 = {"1": "1", "2": "2"}
# print(dict1.get("2"))
# print(dict1['2'])
# change
# dict1 = {"11": "1", "22": "2"}
# dict1['11']="44"
# print(dict1)
# ??
# dict1 = {"11": "1", "22": "2"}
# dict1['55']="44"
# print(dict1)

# 8.1
# d1 = {a: a ** 3 for a in range(1, 11)}
# print(d1)
# 8.2
# str_1 = "pythonist"
# a = dict()
# for i in str_1:
#     a[i] = str_1.count(i)
# print(a)
# 8.3
# n = int(input("num "))
# d1 = {a: a ** 2 for a in range(1, n+1)}
# print(d1)

# iterat
# simple_dict = {"1": "mama", "2": "pfpf"}
# for key, value in simp_dict.items():
#     print(key, value)
# 8.4
# simple_dict = {"data1": 1, "data2": 2, "data3": 3, "data4": 4, }
# proizv = 1
# for a in simple_dict.values():
#     proizv *= a
# print(proizv)
# 8.5
# simple_dict = {"pol": 4, "anna": 4, "alex": 5, }
# a = input()
# print(simple_dict[a])

# 8.6
# alco = {"whiskey": 50, "beer": 5, "wine": 30, "vodka": 15, }
# money = int(input("money "))
# for k, v in alco.items():
#     if v <= money:
#         print(k, v)

# 8.7
# menu = {"борщ": 3, "салат": 2.25, "компот": 1.50, "сосиска": 2.15, }
# sum = int(input())
# for k, v in menu.items():
#     sum1 = sum
#     sum1 -= v
#     if sum1 < 0:
#         break
#     print(f"поел {k}")
#     sum -= v
#
# print(f"осталось {sum}")

# 8.8
# oil = {"янв": 3, "фев": 3.15, "мар": 3.20, "апрель": 3.35, "май": 3.75, "июнь": 3.10}
# for k, v in oil.items():
#     if v == max(oil.values()):
#         print(k)

# 8.9
# vine = {"red vine": 42, "white vine": 37, }
# kate = int(input("red "))
# anna = int(input("white "))
# k_sum = kate * vine['red vine']
# a_sum = kate * vine['white vine']
#
# print(k_sum + a_sum)

# del
# dic.pop("")
# del dic[""]
# dic.popitem()

# zip
# list1 = [1, 2]
# list2 = [3, 4]
# rez_dic = dict(zip(list1, list2))
# print(rez_dic)

# dz_8_1
# list_k = ['name', 'age', 'city']
# print(list_k)
# list_v = input().split()
# person = dict(zip(list_k, list_v))
# print(person["age"])

# dz_8_2
# list_1 = input().split()
# print(list_1)
# d1 = {len(a): a for a in list_1}
# print(d1)

# dz_8_3
# list_1 = [int(i) for i in input().split()]
# d1 = {a: a+0.1*a for a in list_1}
# print(d1)

# dz_8_4
# cars = {"BMW": [2, 3, 4], "Tesla": ['x', 'xx', 'xxx'], }
# for v in cars.values():
#     print(v[0], v[2])
# print(cars["BMW"][0], cars["BMW"][2], cars["Tesla"][0], cars["Tesla"][2])


# sets
# s_1 = {1, 2, 3, 4}
# s_2 = set()

# add
# s_1.add(2)
# s_1.update([2, 4, 5, 6, 67])

# del
# s.pop()
# s.remove()
# s.discard()

# len(s_1)
# print(1 in s_1)

# 9.1
# s = set(input().split())
# print(s)

# 9.2
# list_1 = input().split()
# l_1 = len(list_1)
# s = set(list_1)
# l_2 = len(s)
# print(len(s))

# 9.2
# list_1 = [1, 2, 3, 3, 4, 5, 5]
# sorted(list_1)
# s = set(list_1)
# for j in s:
#     if list_1.count(j) >= 2:
#         print(f"{j} yes")
#     else:
#         print(f"{j} no")


# union unic
# a = {1f, 2f}
# b = {2, 3f}
# c = a | b
# print(c)
# peresech
# a = {1, 2f}
# b = {2f, 3, 5}
# c = a & b
# print(c)
# то что во втором искл в первом
# a = {1f, 2}
# b = {2, 3}
# c = a - b
# print(c)

# исключает то что есть в обоих множествах
# a = {1f, 2}
# b = {2, 3f, 6f}
# c = a ^ b
# print(c)

# 9.3
# set_1 = set(input().split())
# set_2 = set(input().split())
# print(len(set_1 & set_2))

# 9.4
# set_1 = set(input().split())
# set_2 = set(input().split())
# set_3 = set_1 & set_2
# list_1 = list(set_3)
# print(*list_1)

# 9.5
# str_1 = input("str_1 ")
# str_2 = input("str_2 ")
# print((set(str_2) - set(str_1)))

# min?max?sum
# sorted но перезаписать
# frozenset({})

# 91
# str_1 = input("str_1 ")
# str_2 = input("str_2 ")
# print((set(str_2) & set(str_1)))
# #92
# print((set(str_2) - set(str_1)))


# files
# with open("r.txt") as fle:
#     text = fle.readline()
#     for i in fle.readlines():
#         print(i)
#     print(text)
# write
# lst_1 = [1, 2, 3, 4]
# str_1 = "jvgfreg"
# with open("r.txt", "a") as fle:
#     fle.write(str_1)
# with open("r.txt") as fle:
#     text = fle.read()
#     print(text)
# with open("r.txt", "a") as fle:
#     for i in lst_1:
#         fle.write(str(i))


# zap
# lst_1 = []
# for i in range(10):
#     a = random.randint(1, 100)
#     lst_1.append(a)
# print(lst_1)
# with open("r.txt", "a") as simple_file:
#     simple_file.write(str(len(lst_1))+"\n")
#     for i in lst_1:
#         simple_file.write(str(i)+' ')


# lst_1 = []
# with open("r.txt") as fle:
#     for i in fle.readlines():
#         lst_1.append(i)
#     print(lst_1)
# str_1 = lst_1[1]
# str_2 = lst_1[0]
# str_3 = str_2 + str_1
# str_1.split(" ")
# print(str_3)


# day = {1: "sun", 2: "mon", 3: "tue", 4: "wed ", 5: "thu", 6: "fri", 7: "sat"}
# with open("r.txt", "a") as m_file:
#     for k, v in day.items():
#         m_file.write(str(k) + " : " + v + "\n")
# dct = dict()

# lst_1 = []
# lst_2 = []
# with open("r.txt") as m_file:
#     text = m_file.read()
#     text_2 = text.split()
# for i in text_2:
#     if i.isdigit():
#         lst_1.append(int(i))
#     if i.isalpha() and i != 0:
#         lst_2.append(i)
# dict_res = dict(zip(lst_1, lst_2))
# print(dict_res)

# s_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -4}
#
# with open("r.txt", "a") as simple_file:
#     for i in s_1:
#         simple_file.write(str(i) + "\n")

# s_2 = set()
# with open("r.txt") as m_file:
#     text = m_file.read()
#     text_2 = text.split()
#     for i in text_2:
#         if i.isdigit():
#             s_2.add(i)
#
# print(s_2)

# str_1 = input("1: ")
# str_2 = input("2: ")
# str_3 = input("3: ")
# with open("r.txt", "a") as simple_file:
#          simple_file.write(str_1 + "\n"+str_2 + "\n"+str_3 + "\n")

# lst_1 = [5, True, "a,b,c"]
# with open("r.txt", "a") as simple_file:
#           for i in lst_1:
#               simple_file.write(str(i)+"\n")


# a = {1: "a", 2: 'b'}
# with open("r1.json", "a") as simple_file:
#     text = json.dump(a, simple_file) #zapis
#     print(text)


# with open("r1.json", "r") as simple_file:
#     text = json.load(simple_file) #chit
#     print(text)

# n = [1, 2]
# w = ["m", "j"]
# to_jason = {'nim': n, "word": w}
# print(to_jason)
# with open("r1.json", "a") as simple_file:
#     simple_file.write(json.dumps(to_jason))


# exerc_1
# dt = {"python": 4, "java": 7, "data": 14, 6: "game", 1: "film"}
# lst_1_1 = []
# lst_1_2 = []
# lst_2_1 = []
# lst_2_2 = []
# for k, v in dt.items():
#     if str(k).isalpha():
#         lst_2_1.append(k)
#         lst_2_2.append(v)
# dt_1 = dict(zip(lst_2_1, lst_2_2))
# print(dt_1)
#
# for k, v in dt.items():
#     if str(k).isdigit():
#         lst_1_1.append(k)
#         lst_1_2.append(v)
#
# lst_3_1 = lst_1_1 + lst_2_2
# print(lst_3_1)
# lst_3_2 = lst_1_2 + lst_2_1
# print(lst_3_2)
# lst_3_3 = sorted(lst_3_2)
# print(lst_3_3)
# lst_3_4 = sorted(lst_3_1)
# print(lst_3_4)
# dt_2 = dict(zip(lst_3_3[::-1], lst_3_4))
# print(dt_2)

# exerc_2
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(i * j) + str("\t"), end='')
#     print()

# exerc_3
# lst_2 = []
# lst_1 = [random.randint(0, 9) for i in range(10)]
# lst_1 = sorted(lst_1)
# print(lst_1)
# st_1 = set(lst_1)
# print(st_1)
# # for i in lst_1:
# #     if lst_1.count(i) > 1:
# #         lst_2.append(i)
# #         i = ''
# count=0
# print(lst_2)
# for i in lst_1:
#     for j in st_1:
#         if i==j:

# exerc_4
# a = (1, 2, 3, 4, 5)
# b = (5, 6, 7, 5, 2)
# if sum(a) > sum(b):
#     print("a > b")
# if sum(a) < sum(b):
#     print("a < b")
# else:
#     print("a=b")
# print(f"min a {a.index(min(a))+1}, min b {b.index(min(b))+1}")

# exerc_5
# lst_1 = [random.randint(0, 9) for i in range(10)]
# lst_2 = [random.randint(0, 9) for i in range(10)]
# print(lst_1)
# print(lst_2)
# dt_1 = dict(zip(lst_1, lst_2))
# print(dt_1)

# exercise_7
# text = str(input("text ").split())
# with open("r.txt", "a") as simple_file:
#     simple_file.write(str(text)+"\n")
#     simple_file.write("\n")

# exercise_8
# d1 = {"a": 100, "b": 200, "c": 300}
# d2 = {"a": 100, "b": 200, "c": 300}
# print(d1["b"] == d2["b"])

# exercise_9
# d1 = {"a": 375, "b": 567, "c": 37, "n": 21}
# proizv = 1
# for v in d1.values():
#     proizv *= v
# print(proizv)

# exercise_199
# d1 = {"a": [375, 1000], "b": [123, 400], "c": [23, 700]}
# for k, v in d1.items():
#     print(f"{str(k)}-{v[0]}-{v[1]}")
# tovar = input("tovar: ")
# kol = int(input("kol: "))
# cost = 0
# for k, v in d1.items():
#     if tovar == k:
#         v[1] -= kol
#         cost += v[0] * kol
# for k, v in d1.items():
#     print(f"{str(k)}-{v[0]}-{v[1]}")
# print(f"cost {cost}")

# exercise_10
# a = [4, 6, 'py', 'tell', 78]
# b = [44, 'hello', 56, 'exept', 3]
# c = a + b
# tt = ''
# print(a + b)
# t_1 = c.pop(6)
# print(t_1)
# c.insert(3, t_1)
# print(c)
# for i in c:
#     if str(i).isalpha():
#         tt = c.pop(c.index(i))
# print(c)
# print(len(c))


# functions
# def sum_num(a: int, b):
#     return a + b
#
#
# def resuli_function(new: int):
#     return new + sum_num(3, 6)
#
#
# print(resuli_function(1))


# necessery argument-указан внутри

# functions_1
# def num_max(num_1: int, num_2: int, num_3: int, ):
#     return max(num_1, num_2, num_3)
#
#
# print(num_max(3, 7, 9))


# functions_2
# def list_sum(list_1: list):
#     return sum(list_1)
#
#
# print(list_sum([2, 4, 5, 6]))


# functions_3
# def list_proizv(list_1: list):
#     proizv = 1
#     for i in list_1:
#         proizv *= i
#     return proizv
#
#
# print(list_proizv([1, 2, 3]))


# functions_args
# def arrg(*args):
#     return args[::-1]
#
#
# print(arrg(4, 6, 7, 8, 9, 9))

# functions_kwarg
# def kwar(**kwargs):
#        for k,v in kwargs.items:
#     return print(kwargs['erhe'])
#
#
# print(kwar(erhe="1", erheh="1", ehreh="1", ))

# functions_lambda
# multik = lambda x, y: x * y
# print(multik(2, 4))

# functions_4
# def count_letters(str_new: str):
#     count_1 = 0
#     count_2 = 0
#     for i in str_new:
#         if i.isupper():
#             count_1 += 1
#         if i.islower():
#             count_2 += 1
#     return f"low {count_2} up {count_1}"
#
#
# str_1 = input("str: ")
# print(count_letters(str_1))


# functions_5
# def count_args(*args):
#     count = 0
#     for i in args:
#         count += 1
#     return count
#
#
# print(count_args(1, 3, 4, 56, 6))


# functions_6
# def info_kwargs(**kwargs):
#     lst_1 = []
#     for k in kwargs.keys():
#         lst_1.append(k)
#     lst_1_1 = sorted(lst_1)
#     for i in lst_1_1:
#         for k, v in kwargs.items():
#             if i == k:
#                 print(f"{i} = {v}")
#     return ""
#
#
# print(info_kwargs(d="1", b="2", c="3", a="4"))

# functions_7
# elem = [2, 4, 7, 1]
# new_elem = list(map(lambda i: i ** 3, elem))
# print(new_elem)

# functions_8
# nums = [2, 4, 7, 1, 0, 0, -9]
#
#
# def null_num(num):
#     if num == 0:
#         return True
#
#
# def posit_num(num):
#     if num > 0:
#         return True
#
#
# def neg_num(num):
#     if num < 0:
#         return True
#
#
# filtered_1 = list(filter(null_num, nums))
# filtered_2 = list(filter(posit_num, nums))
# filtered_3 = list(filter(neg_num, nums))
# print(f"0 {len(filtered_1)}, >0 {len(filtered_2)}, <0 {len(filtered_3)}")

# functions_9
# num = [88, 1, 1]
#
#
# def add_1(numer, list_new=[]):
#     list_new.append(numer)
#     return sum(list_new)
#
#
# new_elem = list(map(add_1, num))
# print(new_elem[-1])

# wrapper
# def decor(operator):
#     def inner_decor(x, y):
#         return x / y
#
#     return inner_decor
#
#
# @decor
# def divide(x, y):
#     return x * y
#
#
# print(divide(4, 2))

# functions_10
# контекстный менеджер - with open
# интератор(iter i next) и генератр(iter i next i ) - методы
# gil поток
''' асинхронность это запросы
ядра это потоки
сборщик мусора - удаляет автоматом обьекты на которые нет ссылок
посмотреть как загружантся кэш
паттерны проеткировная и шаблоны проектирования

git pull   put
git commit  dhgfsf
git push
'''
# exception
# a = 1
# b = 0
# try:
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("...")

# ex_1
# a = input()
# try:
#     if int(a) >= 18:
#         print("beer")
#     if int(a) < 18:
#         print("coca")
# except ValueError:
#     print("...")

# oop
'''clss new i class init'''


# class Car:
#     ''' piiiip '''
#     print("car")
#
#
# print(Car.__doc__)

# class Car:
#     color = "blue"
#     num_car = 0
#
#     def __init__(self, engine: int, power):
#         self.engine = engine
#         self.power = power
#         Car.num_car += 1
#
#
# setattr(Car, "pipsk", 4)
# delattr(Car, "pipsk")
# print(Car.__dict__)
# if __name__ == "__main__":
#     lada = Car(4, 100)
#     print(lada.color, lada.engine, lada.power, Car.num_car)
# print(lada.__dict__)
# lada.color = "ff"
# print(lada.__dict__)

# class Person:
#     def __init__(self, name: str, surname: str, age: int, gender: str):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.gender = gender
#
#
# Van = Person("fwf", "efuhwe", 12, "f")
# Ivan = Person("fwtj", "efuhwtyj", 77, "m")
# print(Van.__dict__, Ivan.__dict__, sep="\n")
#
#
# class Porshe:
#     model = 77
#
#     def __init__(self, time: int, space: str):
#         self.time: int = time
#         self.space = space
#
#
# Porsh_1 = Porshe(45, "triangulate")
# Porsh_1.model = 6
# Porsh_2 = Porshe(52, "sqare")
# Porsh_2.model = 4
# print(Porsh_1.__dict__, Porsh_2.__dict__, sep="\n")

class Person:
    gender = "m"

    def __init__(self, name: str, surname: str, age: int, color):
        self.age = age
        self.name = name
        self.surname = surname
        self.color = color

    # приниает атрибуты класса и чтото с ними делает
    def res_class(self):
        self.age += 10
        vitalik = self.age + 40
        self.itog(self.age, vitalik)
        return self.age, self.itog

    # не унаследовал аргументов не учаыстыует в динамических процедурох, работает без инита
    @staticmethod
    def itog(argument, a):
        c = a / 10
        return argument - 15

    # все методы и статические переменные принимает, можно переопределить, класс в классе, работает со всеми кроме инита
    @classmethod
    def if_not_theFirst_ot_TheSecond(cls):
        cls.itog(10, 10)

    @property  # можем вызвать не обращаясь к обьекту класса
    def pop(self):
        print("csw")


Van = Person("van", "efuhwe", 12, "f", "qd")
Ivan = Person("ivan", "efuhwtyj", 77, "m", "qwd")
print(Van.age, Van.gender, Van.color, end="\n")
print(Ivan.age, Ivan.gender, end="\n")