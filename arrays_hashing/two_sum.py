class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        
        if len(nums) == 2:
            return [0,1]
        diff = [target - i for i in nums]
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == diff[j]:
                    return [i,j]

#1st solution
#2nd solution i changed it so its not rechecking number pairs it already checked
# with the use of a counter so it doesnt need to reset back

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        counter = 1
        if len(nums) == 2:
            return [0,1]
        diff = [target - i for i in nums]
        for i in range(len(nums)):
            while counter < len(nums):
                if i != counter and nums[i] == diff[counter]:
                    return [i,counter]
                counter+=1
            counter = i+1

#neet codes solution uses enumerate which takes a list and creates a hashMap
#that with its index as the key and its value as the value

class Solution:
    def twoSum(self, nums, target):
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
# Using differnce of the current number and target to see if youve seen the number
# that could be this numbers pair