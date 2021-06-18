# [5,2,[7,-1],3,[6,[-13,8],4]


"""
# [ 1,2,3]
def find(array):
    if len(array)==0:
        return 0
    else:
        return array.pop(0)+find(array)
"""

def find(array,n=1):
    if len(array)==0:
        return 0
    else:
        item = array.pop(0)
        if type(item)==int:
            return item + n*find(array)
        else:
            return find(item,n+1)
    

print(find( [5,2,[7,-1],3,[6,[-13,8],4]] ))