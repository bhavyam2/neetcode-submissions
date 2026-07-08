class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap1 = defaultdict(list)
        result = []
        for i in strs:
            key = sorted(i)
            hashmap1[tuple(key)].append(i)
        
        for key in hashmap1.values():
            result.append(key)

        return result