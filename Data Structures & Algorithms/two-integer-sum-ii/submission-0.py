class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            need = target-numbers[i]
            if mp[need]:
                return [mp[need],i+1]
            
            mp[numbers[i]]= i+1
        return []
            