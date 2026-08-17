class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        seen = {}
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            right = len(nums) -1 
            left = i +1
            target_2sum = 0 -num
            while left < right:
                cur_2sum = nums[left] + nums[right]
                if cur_2sum == target_2sum:
                    output.append([num, nums[left], nums[right]])
                    left +=1
                elif cur_2sum < target_2sum:
                    left += 1
                else:
                    right -= 1
        return output

                    




            