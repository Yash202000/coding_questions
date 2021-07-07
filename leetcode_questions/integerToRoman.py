def findhundredno(x,t,valuelist):
    curr=10**t
    mid = curr//2
    previous=10**(t-1)
    x=x*previous
    s=''
    if x==mid:
        return valuelist[mid]
    elif x<mid:
        if mid - previous == x:
            return valuelist[previous]+valuelist[mid]
        elif previous==x:
            return valuelist[previous]
        else:
            temp=0
            for i in range(3):
                temp+=previous
                s+=valuelist[previous]
                if temp==x:
                    return s
    else:

        if curr-previous==x:
            return valuelist[previous]+valuelist[curr]
        elif curr==x:
            return valuelist[curr]
        else:
            temp=mid
            for i in range(3):
                temp+=previous
                s+=valuelist[previous]
                if temp==x:
                    return valuelist[mid]+s

    return '' 

class Solution:
    def intToRoman(self, num: int) -> str:
        valuelist = {1: "I",5: "V",10: "X", 50: "L", 100: "C", 500: "D",1000: "M"}
        t=0
        s=''
        y=num
        while num:
            temp=num%10
            t+=1
            temps=findhundredno(temp,t,valuelist)

            s=temps+s
            
            num=num//10
        return s



"""
class py_solution:
    def int_to_Roman(self, num):
        lookup = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]
        res = ''
        for (n, roman) in lookup:
            (d, num) = divmod(num, n)
            print(d,' ',num)
            res += roman * d
            print(res)
        return res
#print(py_solution().int_to_Roman(1))
#print(py_solution().int_to_Roman(500))
print(py_solution().int_to_Roman(999))
#print(py_solution().int_to_Roman(1200))
#print(py_solution().int_to_Roman(3456))
"""