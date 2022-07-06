#this is neetCodes Solution
import collections

class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# my solution after reading neetcodes
class Solution(object):
    def groupAnagrams(self, strs):
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)] = ans.get(tuple(count),[])+[s]
        return ans.values()

