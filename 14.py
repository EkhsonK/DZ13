def to_4(x):
    s = ''
    while x:
        s += str(x % 4)
        x //= 4
    return s[::-1]
a = []
for i in range(1, 200):
    g = to_4(i)
    if g[-3:] == '123':
        a.append(i)
print(sorted(a,reverse=True))