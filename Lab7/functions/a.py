arr=[int(i) for i in input().split()]

def mini(i):
    arr.sort()
    return arr[0]


print(mini(arr))