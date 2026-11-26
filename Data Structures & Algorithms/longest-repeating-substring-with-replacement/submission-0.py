class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count= {}
        l = 0
        for r in range (len(s)):
            count[s[l]] = 1+ count.get(s[l],0)

            while (l-r+1)-max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res,l-r+1)
        return res