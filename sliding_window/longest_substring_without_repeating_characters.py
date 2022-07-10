# my solution using a window but also using slices within
# my while loop could be better but a good working solution
def lengthOfLongestSubstring(s):
    res = len(set(s))
    left, right = 0, res
    while right-left != 1:
        if right == len(s)+1:
            res -= 1
            left, right = 0, res
        else:
            if len(set(s[left:right])) == res:
                return res
            else:
                left += 1
                right += 1
    return res

# neetcodes solution
# The way his sliding window is working: his right pointer of the  window moves as long as charecters
# are unique by checking its existence within the set
# once a charecter is said to not be unique by checking in the set
# the left pointer of the window moves until this letter is unique again
# the max lengths are always recorded so when you make it to the end you return the res


def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

# written by my self from memory

def lengthOfLongestSubstring(s):
    hashSet = set()
    left = 0
    res = 0
    for right in range(len(s)):
        while s[right] in hashSet:
            hashSet.remove(s[left])
            left +=1
        hashSet.add(s[right])
        res = max(res,right-left+1)
    return res