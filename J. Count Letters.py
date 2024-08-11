n=input().strip()
count_dic={}

for i in n:
  if i in count_dic:
    count_dic[i]+=1
  else:
    count_dic[i]=1

n=sorted(count_dic.keys())
for letter in n:
  print(f"{letter} : {count_dic[letter]}")
    
   
