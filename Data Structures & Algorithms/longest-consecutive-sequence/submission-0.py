class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        streak,longest=0,0

        for num in st:
            if (num-1) not in st:
                streak=1
                while (num+streak) in st:
                    streak+=1
                longest=max(streak,longest)
        return longest
        

            
            