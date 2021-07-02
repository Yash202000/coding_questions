class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_median(l,countl):
            if countl%2==0:
                return (l[countl//2]+l[(countl//2) - 1])/2
            else:
                return l[countl//2]
            
        i=0
        j=0
        ans=[]
        l1=len(nums1)
        l2=len(nums2)
        if l1==0:
            return(find_median(nums2,l2))
        elif l2==0:
            return(find_median(nums1,l1))
        else:
            while l1!=i and l2!=j:
                if nums1[i] < nums2[j]:
                    ans.append(nums1[i])
                    i+=1
                else:
                    ans.append(nums2[j])
                    j+=1

            while l1!=i:
                ans.append(nums1[i])
                i+=1

            while l2!=j:
                ans.append(nums2[j])
                j+=1

            return(find_median(ans,len(ans)))




"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def find_median(l,countl):
            if countl%2==0:
                return (l[countl//2]+l[(countl//2) - 1])/2
            else:
                return l[countl//2]
        nums1.extend(nums2)
        nums1.sort()
        return find_median(nums1,len(nums1))


"""        