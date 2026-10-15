class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #if (j-i+1)-maxf<=k
        count = {}
        left = 0
        res = 0
        maxf = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxf = max(maxf, count[s[right]])
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res          
    """    
        res=0
        for i in range(len(s)):
            count,maxlen= {}, 0
            for j in range(i,len(s)):
                count[s[j]]=1+count.get(s[j],0)
                maxlen=max(maxlen,count[s[j]])
                
                if (j-i+1)-maxlen<=k:
                    res=max(res,j-i+1)
        return res
    """