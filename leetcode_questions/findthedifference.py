class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = collections.Counter(s)
        b = collections.Counter(t)
        for i in b.keys():
            if b[i]!=a[i]:
                return i

"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_char_no = 0
        for i in t:
            ascii_char_no+=ord(i)
        for j in s:
            ascii_char_no-=ord(j)
        return chr(ascii_char_no)

"""