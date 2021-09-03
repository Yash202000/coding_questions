class Solution:
    def tribonacci(self, n: int) -> int:
        ndict={0:0,1:1,2:1}
        def tribon(n,ndict):
            if n not in ndict:
                ndict[n]=tribon(n-1,ndict)+tribon(n-2,ndict)+tribon(n-3,ndict)
            return ndict[n]
        
        return tribon(n,ndict)
                
        