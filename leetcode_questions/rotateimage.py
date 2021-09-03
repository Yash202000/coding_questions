"""
class Solution:
    def transpose(self,matrix):
        n= len(matrix[0])
        
        for i in range(n):
            for j in range(i,n):
                
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]
                
                
    def reverse(self,matrix):
        
        n = len(matrix[0])
        
        for i in range(n):
            for j in range(n//2):
                
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
                
            
             
    def rotate(self, matrix: List[List[int]]) -> None:
        
        self.transpose(matrix)
        self.reverse(matrix)     

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
        

