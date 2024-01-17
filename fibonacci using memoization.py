
memo = {0:0,1:1}
def ff(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = ff(n-1) + ff(n-2)
        return memo[n]
n = int(input("Enter number: "))
print(ff(n-1))
print(memo)