# 1.B
# 2.D
# 3.D
# 4.True
# 5.
goods = {'牛奶': 4, '可乐': 5, '果汁': 6, '奶茶': 8}


def count(x, y):
    x = str(x)
    y = int(y)
    try:
        n = goods[x]
    except KeyError:
        print('没有此商品，请重新输入！')
        return None
    return y*n


if __name__ == '__main__':
    while 1:
        x = input()
        if x == 'Q':
            break
        y = input()
        n = count(x,y)
        if n is not None:
            print(n, '元')
