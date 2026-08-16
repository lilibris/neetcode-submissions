class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) == 1:
            return 1
        elif len(nums_set) == 0:
            return 0
        seen=defaultdict(list)
        for num in nums_set:
            if num - 1 not in nums_set and num + 1 in nums_set:
                seen[num].extend([num, num+1])
                for i in range(num+2, num+len(nums_set)):
                    if i in nums_set:
                        seen[num].append(i)
                    else:
                        break
            elif num -1 not in nums_set and num +1 not in nums_set:
                seen[num].append(num)
        max_len = 0
        for k, v in seen.items():
            max_len=max(max_len, len(v))
        return max_len



       
            