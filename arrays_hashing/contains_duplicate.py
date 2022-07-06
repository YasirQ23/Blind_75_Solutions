class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False

# I first used a map instead of a set
# The reason why were using the set is because
# the membership test within sets are the fastest.
# we could use a Map isntead of a set but this way is more effient.

