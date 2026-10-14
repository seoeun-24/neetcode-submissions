class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        res=0
        Charset=set()

        for right in range(len(s)):
            while s[right] in Charset:
                Charset.remove(s[left])
                left+=1
            Charset.add(s[right])
            res= max(res,right-left+1)
        return res