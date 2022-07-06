# this is neetcodes solution with changes for readability for myself
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # count and count 2 are just product sums
        # count is foward fount 2 is backwards
        res = [1] * (len(nums))
        count = 1
        for i in range(len(nums)):
            res[i] = count
            count *= nums[i]
        count2 = 1
        for i in range(len(nums)):
            res[-i-1] *= count2
            count2 *= nums[-i-1]
        return res