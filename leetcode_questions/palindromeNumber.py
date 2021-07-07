#here I learned while loop is more efficient than for loop.
t=int(input())
s=str(t)
wil=False
for i in range(len(s)//2):
    print(i," ",(-i-1))
    if s[i]!=s[-i-1]:
        print('str is not palindrom')
        wil=True
if not wil:
    print("str is palindrom")

"""
class Solution(object):
    def isPalindrome(self, x):
        if int(str(abs(x))[::-1])==x:
            return True
        return False
        
"""

