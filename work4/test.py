n = 0
for i in range(1, 101):
    if i % 2 == 0:
        n += i
    else:
        n -= i
print(n)



num = [1,2,3,4]
ll = []
for i in num:
    for j in num:
        for k in num:
            n = int(str(i) + str(j) + str(k))
            if ll.count(n) < 1:
                print(n)
                ll.append(n)



