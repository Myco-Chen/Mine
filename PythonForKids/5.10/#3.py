def checkmoney(money):
    if money >= 100 and money <= 500:
        print('你的钱在100和500之间')
    elif money >= 1000 and money <= 5000:
        print('你的钱在1000和5000之间')
    else:
        print('你的钱不多不少')


while 1:
    money = int(input('你有多少钱？'))
    checkmoney(money)