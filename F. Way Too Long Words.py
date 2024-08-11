number=int(input())
for i in range(number):
    n=input().strip()
    if len(n) <= 10:
        print(n)
    else:
        x=len(n)-2
        print(f"{n[0]}{x}{n[-1]}")