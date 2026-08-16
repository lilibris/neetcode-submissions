class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen=defaultdict(list)
        for num in nums_set:
            if num - 1 not in nums_set and num + 1 in nums_set:
                seen[num].extend([num, num+1])
                for i in range(num+2, num+len(nums_set)):
                    if i in nums_set:
                        seen[num].append(i)
                    else:
                        break
        max_len = float("-inf")
        for k, v in seen.items():
            if len(v) > max_len:
                max_len = len(v)
        return max_len



       
            