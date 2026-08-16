class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if not nums_set:
            return 0
        seen=defaultdict(list)
        for num in nums_set:
            if num - 1 not in nums_set :
                seen[num].append(num)
                for i in range(num+1, num+len(nums_set)):
                    if i in nums_set:
                        seen[num].append(i)
                    else:
                        break
        max_len = 0
        for k, v in seen.items():
            max_len=max(max_len, len(v))
        return max_len



       
            