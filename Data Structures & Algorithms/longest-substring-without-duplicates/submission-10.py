class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max = 0
        ind_map = {}
        l = 0
        for i in range(len(s)):
            if s[i] in ind_map:
                l = max(l, ind_map[s[i]] + 1)
            ind_map[s[i]] = i
            curr_max =  max(curr_max, i - l +1)
        return curr_max