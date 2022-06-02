import collections
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        return max(count.values())>=2