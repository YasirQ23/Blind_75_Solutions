# My solution looks good very proud done speedy
def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height)-1
    res = 0
    while left < right:
        current_res = (right - left)*(min(height[left], height[right]))
        if current_res > res:
            res = current_res
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res

# neetcodes solution same as mine other than the res reassignment
#need to take that res assignment !!


class Solution:
    def maxArea(height):
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res
