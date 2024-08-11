n=input()
flag_n=n
for i in range(1,len(n)):
    x=(n[:i])
    y=(n[i:])

    x_sort=''.join(sorted(x))        #convert strint
    y_sort=''.join(sorted(y))

    concanate=x_sort+y_sort
    if concanate < flag_n:
        flag_n=concanate
print(flag_n)

    
        

    