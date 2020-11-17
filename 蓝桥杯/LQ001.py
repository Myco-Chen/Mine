i = int(input('\033[1;37;40m 请输入一个正整数（N）:\033[0m'))
for j in range(1,i):
    if j % 2 == 0:
        print(j)