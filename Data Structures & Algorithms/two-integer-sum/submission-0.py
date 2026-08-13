class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        for index, num in enumerate(nums):
            rest = target - num
            if rest in seen:
                return [nums.index(rest), index]
            seen.add(num)