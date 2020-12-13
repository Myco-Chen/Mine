#1.D
#2.C
#3.
a = input()
b = ''
c = len(a) - 1
for i in range(len(a)):
    b += a[c-i]
print(b)