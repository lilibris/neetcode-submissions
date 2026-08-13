class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rtn=[]
        if len(nums) < k:
            return []
        count = Counter(nums)
        sorted_c=sorted(count.items(), key=lambda x:-x[1])
        return [item for item,_ in sorted_c[:k]]