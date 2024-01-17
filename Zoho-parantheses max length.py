s = input()
start = 1
end = 3
while((end-start-1) % 2 !=0):
    start = s.index('(')
    end = len(s)-1-s[::-1].index(')')
    s = s[start+1:end]
print(len(s)+2)

