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

# タプル
# 代入出来ない
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

d = {"x": 10, "y": 20}
d["z"] = 1000
print(d)
dict(a=10, b=20)
dict([("a",10)])
