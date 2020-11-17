#1.A
#2.
'''
A = [1,2,3,4]
B = [4,3,2,1]
for i in range(len(A)):
    if A[i] != B[i]:
        A[i],B[i] = B[i],A[i]
'''
#3.
a = input()
b = []
for i in a:
    b.append(int(i))
if b[0] != 0 and b[0] % 3 == 0 and b[2] == 0 and b[4] % 2 == 0:
    print('幸运字符')
else:
    print('不是幸运字符')