from collections import defaultdict  
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        mps = defaultdict(list)
        for word in words:
            key = tuple(sorted(word))
            mps[key].append(word)
        return list(mps.values())