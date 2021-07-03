class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums2len=len(nums2)
        for i in nums1:
            temp=-1
            t=nums2.index(i)
            for j in range(t,nums2len):
                if nums2[j]>i:
                    temp=nums2[j]
                    break
            ans.append(temp)
        return ans
    
