class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        seen=set()
        for num in nums:
            if seen and num in seen:
                return True
            seen.add(num)
        else:
            return False