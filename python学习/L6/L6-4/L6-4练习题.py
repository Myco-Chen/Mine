#1.A
#2.B
def findmin():
    list = []
    while True:
        a = input()
        if a == 'E':
            break
        try:
            a = int(a)
            list.append(a)
        except ValueError:
            break
    b = min(list)
    return b

print(findmin())