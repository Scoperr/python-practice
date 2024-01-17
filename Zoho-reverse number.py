n = int(input())
s = int("-123")
if '-' in str(n):
    if '0' == str(n)[len(str(n))-1]:
        print("-"+str(n)[1:len(str(n))-1][::-1])
    else:
        print("-"+str(n)[1:][::-1] )
elif '0' == str(n)[len(str(n))-1]:    
    print(str(n)[:len(str(n))-1][::-1])
else:
    print(str(n)[::-1])
