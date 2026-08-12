from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        count = Counter(nums)
        max_count = []
        max_count = [v for v in count.values() if v>1]
        if max_count:
            return True
        else:
            return False