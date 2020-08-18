def count_number():
    s1 = int(input('请输入被除数:'))
    s2 = int(input('请输入除数:'))
    s3 = s1//s2
    s4 = s1 - s2*s3
    print('商%s余%s'%(s3,s4))

if __name__ == '__main__':
    while True:
        count_number()