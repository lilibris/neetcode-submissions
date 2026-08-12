from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if not nums:
            return False
        max_count = 0
        max_count = max(v for v in count.values())
        if max_count > 1:
            return True
        else:
            return False
        