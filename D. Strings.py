string1=input().strip()
string2=input().strip()
result1=string1+string2
x=string2[0]+string1[1:]
y=string1[0]+string2[1:]
print(f"{len(string1)} {len(string2)}")
print(F"{result1}")
print(f"{x} {y}")

