"""
#worst time complexity solution :(

def bitstring(n):
    s=''
    while n>1:
        s+=str(n%2)
        n//=2
        
    if n==1:
        s+='1'
    return s

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        else:
            ans = [0]
            for i in range(1,n+1):
                s = bitstring(i)
                ans.append(s.count('1'))
            return ans
                

"""



class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [-1]*(n+1)
        ans[0]=0
        for i in range(1,n+1):
            if i%2==0:
                ans[i] = ans[i//2]
            else:
                ans[i] = ans[i//2]+1
                
        return ans