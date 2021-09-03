class Solution:
    def generate(self,num:int)-> List[List[int]]:
        
        def gen(n,r):
            l = [1]
            t=len(r)-1
            for i in range(t):
                tempres = r[i]+r[i+1]
                l.append(tempres)
            l.append(1)
            return l
        
        
        res = []
        pres = [1]
        for i in range(num):
            res.append(pres)
            pres  = gen(i-1,res[i])
        return res
            
            