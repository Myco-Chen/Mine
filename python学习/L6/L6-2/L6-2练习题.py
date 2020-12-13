#1.A
#2.B
#3.
def go(front,left,right):
    if front == 'red' and left == 'green':
        return 'R'
    elif right == 'green' and left != 'green':
        return 'L'
    return 'F'