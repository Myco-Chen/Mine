#1.B
#2.B
#3.
a = input()
b = ['0','1','2','3','4','5','6','7','8','9']
c = 0
for i in range(len(a)):
    if a[i] in b:
        c += 1
print(c)