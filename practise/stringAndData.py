# -*- coding: utf-8 -*-
# s1 = 72
# s2 = 85

# r = (s2-s1)/s1 * 100
# print("%.1f %%" % r)

# n1 = 100
# n2 = 1000
# print(hex(n2-n1))

# d = {'y': 'B', 'x': 'A', 'z': 'C' }
# for k, v in d.items():
#     print(k, '=', v)


# L = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L if isinstance(s, str)]
# print(L2)

# def triangles():
# 	a, container = 1, [1]
# 	while True:
# 		index, nCon = 0, [1]
# 		length = len(container)
# 		if length>1:
# 			while index<length-1:
# 				nCon.append(container[index]+container[index+1])
# 				index = index+1
# 		yield container
# 		nCon.append(1)
# 		container = nCon

# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break

# from functools import reduce
# def fn(x, y):
#     return x * 10 + y

# def char2num(s):
# 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

# print(reduce(fn, map(char2num, '13579')))

def normalize(name):
  def toSmall(letter):
    if letter>='A' and letter<='Z':
      letter = chr(ord(letter)+32)
    return letter
  nName = list(map(toSmall, name))
  if nName[0]<='z' and nName[0]>='a':
    nName[0] = chr(ord(nName[0])-32)
  return "".join(nName)

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
























