i1 = int(input('\033[1;37;40m 请输入所要相加的数字：\033[0m'))
i2 = int(input('\033[1;37;40m 请输入相加的次数：\033[0m'))
sum = 0
for i in range(1,i2+1):
    i11 = i1 * (10**(i2-i))
    i22 = i11 * i
    sum = sum+i22
print('结果：',sum)