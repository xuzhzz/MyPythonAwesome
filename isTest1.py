from copy import deepcopy, copy

# 引用

a = 1
b = a
a = 3

print(b)

a = [1, 2]
b = a
c = copy(a)
d = deepcopy(a)
a.append(3)
print('a id:%s,%s' % (id(a), a))
print('b id:%s,%s' % (id(b), b))
print('c id:%s,%s' % (id(c), c))
print('d id:%s,%s' % (id(d), d))