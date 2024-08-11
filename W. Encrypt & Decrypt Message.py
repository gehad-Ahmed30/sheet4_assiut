n=int(input())
s=list(input())        #[E,g,y,p,t]

Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

encryption={}
decryption={}
result=[]

for i in range(len(Original)):
    encryption[Original[i]]=Key[i]
    decryption[Key[i]]=Original[i]

if n==1:
    for char in s:
        result.append(encryption.get(char,char))      #.get in dictionery print value and take key
else:
    for char in s:
        result.append(decryption.get(char,char))

print(''.join(result))  #convrt list to string


