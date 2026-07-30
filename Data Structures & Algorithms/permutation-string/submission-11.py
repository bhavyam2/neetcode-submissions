class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_occur = {}
        window_occur = {}
        l = 0
        for i in s1:
            if i in s1_occur:  
                s1_occur[i] += 1
            else:
                s1_occur[i] = 1
        for i in s2[0:len(s1)]:
            if i in window_occur:  
                window_occur[i] += 1
            else:
                window_occur[i] = 1
        print(s1_occur)
        
        for x in range(len(s1), len(s2)):
            if s1_occur == window_occur: #checks if window is same
                return True
            window_occur[s2[x-len(s1)]] -= 1
            if window_occur[s2[x-len(s1)]] == 0:#shifts the left
                window_occur.pop(s2[x-len(s1)], None)
            if s2[x] in window_occur: #shifts the right
                window_occur[s2[x]] += 1
            else:
                window_occur[s2[x]] = 1
        if s1_occur == window_occur: #checks if window is same
            return True
        return False