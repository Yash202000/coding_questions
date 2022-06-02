def findsol(posb,n,curr):

    if sum(curr)== n:
     
        posb.append(curr.copy())

    elif sum(curr)>n:
        return
    
    curr.append(1)
    findsol(posb,n,curr)
    curr.remove(1)
    curr.append(2)
    findsol(posb,n,curr)
    curr.remove(2)


l={}
def computeSteps(i,n,l):
    if i==n:
        return 1
    elif i>n:
        return 0

    elif i in l:
        return l[i]
    else:
        
        temp = computeSteps(i+1,n,l)+computeSteps(i+2,n,l)

        print(l)
        l[i]=temp
        return temp
        
print(computeSteps(0,3,l))

# ans = []
# findsol(ans,5,[])
# print(ans)
