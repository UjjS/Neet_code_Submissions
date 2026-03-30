from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res=[]
        sorted_dict = dict(sorted(counter.items(), key= lambda item :item[1], reverse= True))
        return list(sorted_dict.keys())[:k]