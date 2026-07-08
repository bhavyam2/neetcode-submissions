class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answerS = defaultdict(list)
        answerT = defaultdict(list)        
        for i in s:
            answerS[i].append(i)
        for x in t:
            answerT[x].append(x)
        if (answerS == answerT):
            return True
        return False