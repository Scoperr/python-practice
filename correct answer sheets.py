def linearSearch(arr, n):
    for i in range(n):
        if arr[i]-1 is i:
            return i
    return -1
def permute(arr,start,end):
    global c
    if start==end:
        if linearSearch(arr, len(arr))!=-1:
            c+=1
            #f.append(list(arr))
        return
    for k in range(start,end+1):
        arr[start],arr[k] = arr[k],arr[start]
        permute(arr,start+1,end)
        arr[start],arr[k] = arr[k],arr[start]
n = int(input())
c = 0
permute(list(range(1,n+1)),0,n-1)
print(c)