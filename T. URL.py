def extract(s):
    start=s.find("?")  #return index ?
    string=s[start+1:]
    x=string.split('&')     #['name=value', 'age=25'].
    dic_result={}


    for i in x:
        name,value=i.split('=')              #
        dic_result[name]=value       #store in dictionery {'name:value', ....}.
    
    for key in ['username', 'pwd', 'profile', 'role', 'key']:
        print(f"{key}: {dic_result[key]}")

s=input()
extract(s)
    