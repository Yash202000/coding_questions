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


class Solution:
    def climbStairs(self, n: int) -> int:
        
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
                print()
                l[i]=temp
                return temp
        print(l)
        return computeSteps(0,n,l)

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: 
            return 1
        elif n == 2:
            return 2
        
        first, second, third = 1, 2, 3
        for i in range(3,n+1):
            third = first + second
            first, second = second, third
            
        return third

"""
