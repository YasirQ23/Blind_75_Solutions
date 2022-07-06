class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap ={}
        for i in s:
            hashMap[i] = hashMap.get(i,0)+1
        for i in t:
            hashMap[i] = hashMap.get(i,0)-1
        for i in hashMap:
            if hashMap[i] != 0:
                return False
        return True
            

#This is my answer and also neetcodes answer so perfect !!!