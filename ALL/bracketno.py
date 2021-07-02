"""
"Bracket Number" https://www.codingninjas.com/codestudio/problem-details/bracket-number_1229411
"""

t="(pq)()"
stack=[]
ptr=0
for i in t:
    if i=="(":
        ptr+=1
        stack.append(ptr)
        print(ptr,end=" ")
    elif i==")":
        print(stack.pop(),end=" ")

 