"""
Q.3 Draw this Pattern 👇

    *
   * * 
  * * *
 * * * *
* * * * *

"""

k=int(input("Enter no hight of pyramid: "))
def create(k):
    for i in range(1,k+1):
        print(" "*(k-1),"* "*i)
        k-=1

create(5)