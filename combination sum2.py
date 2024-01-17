def f(target, candidates,temp,index):
        if target==0:
            if sorted(list(temp)) not in memo:
                memo.append(sorted(list(temp)))
            return
        else:
            #prev = -1
            for i in range(index,len(candidates)):
                if target>=0:
                    
                    temp.append(candidates[i])
                    f(target-candidates[i],candidates,temp,i+1)
                    temp.remove(candidates[i])
                #prev = candidates[i]
        return memo
f(target,candidates,temp,0)


    