def sum(f,s):
    return (f+s)
def printt(l):
    for i in l:
        print(chr(i+96),end=" ")
def cal_fib(n):
    f=1
    s=1
    if n==2:
        return 1
    else:
        for i in range(n-2):
            sum = f+s
            f=s
            s=sum
        return sum
n = int(input("Enter number of rows: "))
l1=[]
l2=[]
for i in range(1,n+1):
    if i==1:
        l1 = [1]
        print('a')
    elif i==2:
        print('a a')
        l2 = [1,1]
    else:
        l = []
        for i in range(0,len(l1)):
            l.append(sum(l1[i],l2[i]))
        l.append(l2[i+1])
        l.append(cal_fib(len(l2)+1))
        printt(l)
        print()
        l1=l2
        l2=l