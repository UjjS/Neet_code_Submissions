# from Typing import List, Dict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        max_streak=0
        count=0
        for i in range(len(nums)):
            if nums[i]-1 not in st:
                streak=1
                while streak+nums[i] in nums:
                    streak+=1
                max_streak = max(max_streak, streak)
        return max_streak

            
