x=int(input())
cnt=1
for i in range(2, int(x**0.5)+1):
    if(x%i==0):
        cnt=cnt+1
print(2*cnt)