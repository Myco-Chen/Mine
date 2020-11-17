str = input('\033[1;37;40m 请输入五个以上的正整数:\033[0m')
nums = eval(str)
n = list()
for i in range(len(nums)):
    n.append(nums[i])

n.sort()
for j in n:
    print(j,end=' ')