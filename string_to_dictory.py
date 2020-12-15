str = "k:1|k1:2|k2:3|k3:4"
a = str.split("|")#split函数分割之后得到一个列表
print(a)
d = {}
for i in a:
    key,value = i.split(':')
    d[key] = value
print(d)