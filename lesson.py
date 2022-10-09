# import math
# num = 1
# name = "1"
# new_name = int(name)
# print(new_name, type(new_name))

# print("hi","mike",sep=",",end=".\n")
# print("hi","mike",sep=",",end="\n")

# result = math.sqrt(25)
# print(result)

# print('I don\'t know')
# print(r'C:\name\name')
# print("""\
# line1
# line2\
# """)
# word = "python"
# print(word[:2])
# word = "J" + word[1:]
# print(word)
# print(len(word))

# 文字列のメソッド
# s = 'My name is Mike. Hi Mike'
# print(s)
# is_start = s.startswith('My')
# print(is_start)
# print(s.find("Mike"))
# print(s.rfind("Mike"))
# print(s.count("Mike"))
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.replace("Mike","Nancy"))

# 文字列の代入
from ast import If
from multiprocessing.connection import wait
import re

name = "My name is {0} {0}".format("jun", "sakai")
"My name is {name} {family}".format(name="jun", family="sakai")
# print(name)
# f-strings
a = "a"
# print(f"a is {a}")

# list
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[::2])
# print(l[::-1])
# listの代入、削除
# l[2] = "a"
# l[2:5]=["A","B","C"]
# l[2:5]=[]
# l[:]
# l.append(11)
# l.insert(0, 100)
# l.pop()
# l.pop(0)
# del,remove
# print(l)

# 結合
a = [1, 2]
b = [3, 4]
x = a + b
a += b
# print(x,a)
x = [5, 6]
y = [7, 8]
x.extend(y)
# print(x)
# 検索
r = [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(r.index(3,3))
# print(r.count(3))
# if 3 in r:
#     print("e")
# sort
# r.sort()
# print(r)
# r.sort(reverse=True)
# print(r)
# r.reverse()
# print(r)

i = [1, 2, 3, 4, 5]
j = i.copy()
# j = i[:]
j[0] = 100
# print(i)
# print(j)

"""
タプル
代入出来ない
"""
t = (1, 2, 3, 4, 1, 2)
tt = ([1, 2, 3], [1, 2, 3])
tt[0][0] = 100
# print(tt)
type(tt)
num_t = 10, 20
x, y = num_t
# print(x,y)
# 入れ替え
i = 10
j = 20
i, j = j, i
# print(i,j)

# dict
d = {"x": 10, "y": 20}
d["z"] = 1000
# print(d)
dict(a=10, b=20)
dict([("a", 10)])
# print(d.keys())
# print(d.values())
d2 = {"x": 1000, "j": 500}
d.update(d2)
# d.pop("x")
del d["y"]
# print("z" in d)
# コピー
x = {"a": 1}
y = x.copy()
y["a"] = 1000
# print(x)
# print(y)

# if分
x = 10
# if x < 0:
#     print("negative")
# elif x == 0:
#     print("zero")
# else:
#     print("positive")

a = 5
b = 10
# if a>0:
#     print("a is")
#     if b > 0:
#         print("b is")

# in out
y = [1, 2, 3]
x = 1
# if x in y:
#     print("in")
# if 100 not in y:
#     print("not in")

is_ok = False
# if not is_ok:
#     print("hello")

# 値がない判定
is_ok = []
# is_ok = ""
# if is_ok:
#     print("ok")
# else:
#     print("no")

# none '=='は好まない→'is'を使用
is_empty = None
# print(is_empty)
# if is_empty is None:
#     print("none!!")

# while break continue
count = 0
# while count < 5:
#     print(count)
#     count += 1

# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#     count += 1

# while else
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print("done")

# input関数
# while True:
#     word = input("Enter:")
#     num = int(word)
#     if word == "ok":
#         break
#     print("next")

# for break continue else
some_list = [1, 2, 3, 4, 5]
# for i in some_list:
#     print(i)

# for i in  ["apple","banana","orange"]:
#     if i == "b":
#         print("stop")
#         break
#     print(i)
# else:
#     print("i ate all!")

# range関数 iに_も使用できる
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(2, 10, 3):
#     print(i)

# enumerate関数 indexも取得できる
# for i,v in enumerate(["a","b","c"]):
#     print(i,v)

# zip関数
days = ["Mon","Tue","Wen"]
fruits = ["apple","banana","orange"]
drinks = ["coffee","tea","beer"]
# for i in range(len(days)):
#     print(days[i], fruits[i], drinks[i])

# for day, fruit, drink in zip(days,fruits,drinks):
#     print(day,fruit,drink)

# dict for 
d = {"x": 100, "y": 200}
# d.items() タプルで帰ってくる→アンパッキングで値が変数に入る
# for k,v in d.items():
#     print(k, v)

# 関数
def say():
    return "hi"
res = say()
print(res)

def what(color):
    print(color)
what("red")
# 数値の型だけど文字列なども入れられてしまう
def add_num(a: int, b: int) -> int:
    return a + b
res = add_num("a","b")
print(res)