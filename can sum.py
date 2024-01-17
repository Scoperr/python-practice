c=0
def f(s,l):
    if s==0:
        return True
    elif s<0:
        return False
    else:
        for i in l:
            rem = s-i
            if f(rem,l):
                return True
        else:
            return False
        
s = int(input())
l = list(map(int, input().split((','))))
print(f(s,l))