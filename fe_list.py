def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(1,11):
    print(f(i))
s = f(10)
print(s)