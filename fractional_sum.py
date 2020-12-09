a = 2
b = 1
sum1 = 0
for i in range(1,20):
    sum1 += a/b
    c = a
    a = a + b
    b = c
print(sum1)