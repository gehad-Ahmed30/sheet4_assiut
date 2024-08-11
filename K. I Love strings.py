n=int(input())

for i in range(n):
    x,y=input().split()
    list_num=[]
    min_len=min(len(x),len(y)) #take min length 
    for j in range(min_len):
        list_num.append(x[j])
        list_num.append(y[j])
    if len(x) > len(y):
        list_num.append(x[min_len:])
    elif len(y) > len(x):
        list_num.append(y[min_len:])
    print(''.join(list_num))

