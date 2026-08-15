class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        output = []
        prefix[0]=suffix[-1] =1
        for i in range(1, n): # prefix[i] product of all elements to the left of i, exclude i 
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(n-2, -1, -1): # suffix[i] product of all elements to the right of j, exclude j 
            suffix[j] = suffix[j+1]* nums[j+1]
        for i in range(n):
            output.append(prefix[i]*suffix[i])
        return output

