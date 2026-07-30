class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            ans = max(ans, r-l + 1)
        return ans