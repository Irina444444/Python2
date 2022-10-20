n = int(input())
num = []
for x in range (1,n+1):
    num.append(x)
print (num)

s = 1
for item in num:
    if item % 2 == 0:
        s *= item
print(s)