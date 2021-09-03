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
                print(i," ",temp)
                l[i]=temp
                return temp


print(computeSteps(0,5,l))
print(l)
