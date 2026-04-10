from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = dict(Counter(nums))
        for key, value in count_dict.items():
            if value == max(count_dict.values()):
                return key
        return 0