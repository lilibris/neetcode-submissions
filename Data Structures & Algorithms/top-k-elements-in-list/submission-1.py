class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=defaultdict(int)
        for num in nums:
            seen[num] +=1
        sorted_seen = sorted(seen, key=lambda x:-x)
        return sorted_seen[:k]