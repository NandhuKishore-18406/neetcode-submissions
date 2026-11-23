class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) != len(t):
            return False
        elif len(s) == len(t):
            for i in range(0,len(s)):
                if s[i] in s and s[i] in t:
                    count = count + 1
            if count == len(s):
                return True

            else:
                return False
        