# not - imprime o contrario 
x = True
y = False
# print(not x)
# print(not y)

# and - se as duas forem verdadeiras, da true
x = True
y = False
# print(x and x)

# or - se uma das 2 forem verdadeiras, da true
x = True
y = False
# print(x or y)

# expressoes logicas/booleanas
x = 10
y = 1 
res = not x > y
# print(res)

x = 10
y = 1
z = 5.5
res = x > y and z == y # True and False
# print(res)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x
# res = True or not False and True
# res = True or True and True
# res = True
# print(res)