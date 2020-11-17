i = input()
x = i.index('-')
i1 = i[0:x]
i2 = i[(x+1):(len(i)-1)]
def p():
    print(i1, i2)
    print(i, '不是幸运号码')
if i1 == '010':
    if '8' in i2:
        if int(i2) % 2 == 0:
            if int(i2) % 3 == 0:
                print(i1,i2)
                print(i,'是幸运数字')
            else:
                p()
                print(i,'不是3的倍数')
        else:
            p()
            print(i,'不是偶数')
    else:
        p()
        print(i,'不是包含数字8')
else:
    p()
    print(i,'不是来自北京')