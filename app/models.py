# a = "anjan"
# print("BEFORE", id(a))
# a = a+"kumar"
# print("AFTER", id(a))
# print("===============================")
# l = [1,2,3]
# print("BEFORE", id(l))
# l.append(0)
# print("AFTER", id(l))
# l = l+[5,6]
# print("2nd AFTER", id(l))
# print(type(eval(str("[1,2,3],(1,3)"))))
# print(eval(float("inf")))
# a = [{"name": "kumar", "marks": 98},
#      {"name": "anjan", "marks": 87},
#      {"name": "bhanu", "marks": 78}
#      ]
# a.sort(key=lambda i: i["marks"])
# print(a)
#
# dict4 = {1: True}
# print(all(dict4))
# print(bool(11))
# l = [10, 20, 30, 40]
# sum = 0
# for i in l:
#     sum += i
# print(sum)
# a = 7
# print(complex(a))
# num = 12345
# new = 0
# while num > 0:
#     n1 = num % 10
#     new = new*10 + n1
#     num = num//10
#     breakpoint()
# print(new)
# import re
# a = "ravi6302731789hdjd dhdj s7306948189whhnbneweh66788dnj5467389657hg"
# b = re.findall("\d+",a)
# for i in b:
#     #print(i)
#     if len(i) == 10 and (i[0] in ["6","7","8","9"]):
#         print(i)
#     else:
#         pass
# # print(b)
# a = "ravi6302731789hdjd dhdj s7306948189whhnbneweh66788dnj5467389657hg"
# num = ""
# mobile = []
# for i in a:
#     if i.isdigit():
#         num = num + i
#     else:
#         if len(num) == 10 and num[0] in '9876':
#             mobile.append(num)
#         num = ""
# else:
#     if len(num) == 10 and num[0] in '9876':
#         mobile.append(num)
# print(mobile)
# print(isinstance("56", int))
# print(float("6"))
# print(help("a".split()))
# a = [1,2,3,4,3,5]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         pass
# print(b)
# aa = {"anjan":1, "kumar" : 2}
# a1 = [1,2,3]
# k = str(a1)
# j =str(aa)
# print(type(j))
# print(j,k)

# a = 1234
# b = 1234
# print(id(a) == id(b))
# print(id(a), id(b))
# a = 1234
# print(a is b)

# data = [
#     {"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 0}, {"a": 2, "b": 3, "c": 4}, {"a": 1, "b": 2, "c": 10},
#     {"a": 4, "b": 2, "c": 11}, {"a": 1, "b": 2, "c": 12}, {"a": 1, "b": 2, "c": 22}, {"a": 1, "b": 2, "c": 32},
#     {"a": 4, "b": 2, "c": 44}, {"a": 2, "b": 3, "c": 55}
# ]
#
# di = {}
# for i in data:
#     key = (i['a'], i['b'])
#     if key in di:
#         di[key].append(i['c'])
#     else:
#         di[key] = [i['c']]
#         print(di)
#
# final_li = []
# for k, v in di.items():
#     temp_di = {'a': k[0], 'b': k[1], 'c': v}
#     final_li.append(temp_di)
#
# print(final_li)
# a = 12345
# b = 12345
# print(id(a) == id(b))
# print(id(a), id(b))
# src = r.get_git_ref("heads/source branch name")
# src.delete()
# d = [{"name": "sai", "age": 24, "course": "python"},
#       {"name": "anjan", "age": 25, "course": "django"},
#       {"name": "kumar", "age": 23, "course": "c+"}]
#
# a = sorted(d, key=lambda i: i["age"])
# print(a,"before operator")
#
# import operator
# d.sort(key=operator.itemgetter("course"))
# print(d,"========================")
# def fun(data):
#     if data[0] == data[1] and data[1]==data[2] :
#         return 0
#     elif data[0] == data[1] and data[0]!=data[2]:
#         return data[2]
#     elif data[0] == data[2] and data[0]!=data[1]:
#         return data[1]
#     elif data[1] == data[2] and data[0] != data[1]:
#         return data[0]
#     else:
#         return data[0]+data[1]+data[2]
#
# print(fun([3,2,3]))

# def fun(x, y, z):
#     if x == y and y == z:
#         return 0
#     elif x == y and x != z:
#         return z
#     elif x == z and x != y:
#         return y
#     elif y == z and x != y:
#         return x
#     else:
#         return x + y + z
# print(fun(3, 2, 3))
# def sample_fun(data, new_data):
#     for i in range(len(data)):
#         for j in range(i,len(data)):
#             if data[i]*data[j] == new_data:
#                 return i, j
#             else:
#                 continue
# print(sample_fun([1,2,3,4],12))
# import pdb;pdb.set_trace()
# def func1():
#     try:
#         return 1
#     finally:
#         return 2
#
#
# def func2():
#     try:
#         raise ValueError()
#     except:
#         return 1
#     finally:
#         return 3
#
# print(func1())
# print(func2())
