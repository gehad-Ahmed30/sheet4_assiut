def cal_count(n):
    
    n=n.lower()
    list_str={
        'e': 0,
        'g': 0,
        'y': 0,
        'p': 0,
        't': 0
    }
    min_count = float('inf')
    for char in n:
        if char in list_str:
          list_str[char]+=1
            
            
    for char in 'egypt':
            min_count = min(min_count, list_str[char])
    
    return min_count

n=input()
print(cal_count(n))
