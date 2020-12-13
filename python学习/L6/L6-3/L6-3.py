#1.C
#2.D
def findmax():
    list = []
    while True:
        a = input()
        if a == 'Q':
            break
        try:
            a = int(a)
            list.append(a)
        except ValueError:
            break
    m = max(list)
    return m

print(findmax())