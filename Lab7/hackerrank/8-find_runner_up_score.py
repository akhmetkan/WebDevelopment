if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
maxi=-100
arr.sort()
for i in arr:
    if i==maxi:
        continue
    pre_maxi = maxi
    maxi = max(i, maxi)
print(pre_maxi)
