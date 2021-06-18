"""
# code using itertools 

from itertools import permutations
perms = permutations([1,2,3])
print(list(perms))

"""

def permute(a, l, r):
    if l==r:
        print(a)
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] 


a=list(map(int,input().split()))
permute(a,0,len(a)-1)
