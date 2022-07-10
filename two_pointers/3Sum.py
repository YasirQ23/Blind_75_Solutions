# My solution was too slow :(
from collections import Counter


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    hashMap = {}
    counter = 0
    nums.sort()
    for left in range(len(nums)-2):
        if left != 0 and nums[left] == nums[left-1]:
            continue
        for middle in range(left+1, len(nums)-1):
            if middle != left+1 and nums[middle] == nums[middle-1]:
                continue
            for right in range(middle+1, len(nums)):
                if right != middle+1 and nums[right] == nums[right-1]:
                    continue
                current_res = [nums[left], nums[middle], nums[right]]
                if sum(current_res) == 0 and Counter(current_res) not in hashMap.values():
                    counter += 1
                    hashMap[counter] = Counter(current_res)
                    res.append(current_res)
    return res

# neetcodes Solution


def threeSum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
