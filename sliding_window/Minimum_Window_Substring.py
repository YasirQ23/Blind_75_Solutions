from typing import Counter
## my soultion very intresting but wont work
def minWindow(s,t):
    t = Counter(t)
    l=0
    res = []
    for r in range(len(s)):
        if s[r] in t and t[s[r]] > 0:
            t[s[r]] -= 1
        while sum(t.values()) == 0:
            if res == [] or r-l < res[1]-res[0]:
                res = [l,r]
            if s[l] in t:
                t[s[l-1]] += 1
                l+=1
            else:
                l+=1
    return res

## neetcodes solution
def minWindow(s,t):
    if t == "": return ""
    
    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)
    
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        
        if c in countT and window[c] == countT[c]:
            have += 1
    
        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if resLen != float("infinity") else ""
