class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = []
        temp = 0
        
        for num in nums:
            temp += num
            if num > temp:
                temp = num
            output.append(temp)
   
        return max(output)