import re # regular expression
n=input().strip()
result=re.findall(r'[a-zA-Z]+',n)
print(len(result))



