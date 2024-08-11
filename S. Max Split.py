n=input()

count_l=0
count_r=0
list_n=[]
flag_index=0


for i in range(len(n)):
    if n[i]=='L':
        count_l+=1
    elif n[i]=='R':
        count_r+=1

    if count_r==count_l:
        list_n.append(n[flag_index:i+1])
        flag_index=i+1
        count_l=0
        count_r=0


print(len(list_n))

for i in list_n:
    print(i)
