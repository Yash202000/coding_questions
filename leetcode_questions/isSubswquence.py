class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls:
            j = 0
            for i in range(lt):
                if s[j]==t[i]:
                    j+=1
                    if j == ls:
                        return True
            return False
        else:
            return True