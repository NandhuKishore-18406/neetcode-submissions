class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) != len(t):
            return False
        elif len(s) == len(t):
            for i in range(0,len(s)):
                listt = list(t)
                if s[i] in listt:
                    count = count + 1
                    listt.remove(s[i])
                    
            if count == len(s):
                return True

            else:
                return False
        