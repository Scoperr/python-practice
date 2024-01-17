def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if (len(sub_string) == 1):
            if sub_string == string[i]:
                count = count + 1
    if(len(sub_string)>1):
        for j in range(len(string)):
            for k in range(len(sub_string)):            
                if(string[j] == sub_string[k] and (j+1)<len(string)):
                    c = 0     
                    for l in range(j+1,len(string)):
                        if (k+1)<len(sub_string) and (l+1)<len(string) and string[l] == sub_string[k+1]:
                            c = c+1
                        else:
                            break
                    if c == len(sub_string)-1:
                        count = count+1
                else:
                    break   
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)