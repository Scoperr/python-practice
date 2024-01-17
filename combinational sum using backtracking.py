import itertools as it
#tot = 0
def find_combinations(target,arr,ans):
    if target == 0:
        if(len(list(temp))<=3):
            ans.append(list(temp))

        return
    for i in range(len(arr)):
        if target-arr[i]>=0:            
            temp.append(arr[i])
            find_combinations(target-arr[i], arr, ans)
            temp.remove(arr[i])
target = int(input())
arr = list(range(1,int(input())+1))
temp = []
ans = []
#tot = 0
find_combinations(target,arr,ans)
#print(tot)
print(len(ans))
print(ans)