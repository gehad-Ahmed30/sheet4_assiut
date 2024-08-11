string1=input().strip()
string2=input().strip()
if (string1)>(string2):         #"acm" < "acpc" because 'a' == 'a', 'c' == 'c', but 'm' < 'p' in the next position.
    print(string2)
elif (string1)<(string2):
    print(string1)
else:
    print(string1)