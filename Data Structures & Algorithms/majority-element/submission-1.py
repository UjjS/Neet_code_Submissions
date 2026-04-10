from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        max_key = max(count_dict, key=count_dict.get)
        return max_key
