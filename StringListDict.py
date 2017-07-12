# 列表 append extend insert

list1 = ['l1', 'l2', 'l3']
list2 = ['l5', 'l6', 'l7']
temp = 'l4'

list1.append(temp)

print(list1)

# 通过extend可以将另一个集合中的元素逐一添加到列表中
list1.extend(list2)

print(list1)

# insert(index, object) 在指定位置index前插入元素object
list3 = []
list3.insert(0, list1)
print(list3)

# index find

# 字典 及其 常见操作
dict1 = {'name':'xuzh', 'sex': 'male'}
print(len(dict1))
print(dict1.keys())
print(dict1.values())
for key in dict1.keys():
    print(dict1.get(key))


# 遍历数据结构

# 字符串遍历

str = 'hello world'
list4 = ['2', '3', '4', '5', '6']
tuple1 = ('2', '3', '4', '5', '6')
for char in str:
    print(char)

for lis in list4:
    print(lis)

for tup in tuple1:
    print(tup)

for k, v in dict1.items():
    print('%s:%s' % (k, v))


# 带下表索引的遍历
for k, v in dict1.items():
    print(' %s:%s' % (k, v))

for i, l in enumerate(list1):
    print('(%s).%s' % (i, l))