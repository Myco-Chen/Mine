# 1.B
# 2.正确
# 3.
"""
a = input()
a = int(a)
l1 = []
for i in range(a):
    b = int(input())
    l1.append(b)
l1.sort()
print(l1)
"""

# 4.编程题
a = input()
if len(a) == 8:
    if a.isdigit():
        print('密码是纯数字!')
    elif a.isupper() or a.islower():
        print('密码全部为小写/大写!')
    else:
        print('密码格式正确!')
else:
    print('密码不是8位！')