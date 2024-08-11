n=int(input())
for i in range(n):
    N=input().strip()
    if '010' in N or '101' in N:
        print("Good")
    else:
        print("Bad")