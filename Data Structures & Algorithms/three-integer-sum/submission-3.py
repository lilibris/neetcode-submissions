class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        
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
                    right -= 1
                elif cur_2sum < target_2sum:
                    left += 1
                else:
                    right -= 1
        if output:
           
            seen =set()
            unique_out = []
            for item in output:
                print(item)
                t = tuple(item)
                if t not in seen:
                    
                    unique_out.append(item)
                seen.add(t)
            return unique_out

        else:
            return output

                    




            