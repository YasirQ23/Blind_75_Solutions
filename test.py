# nums = [1,12,-5,-6,50,3]
# k = 4

# def bigAVG(nums,k):
#     pointer = 0
#     maxNum = sum(nums[0:4])
#     curNum = sum(nums[0:4])
#     while pointer + k != len(nums):
#         curNum -= nums[pointer]
#         pointer += 1
#         curNum += nums[pointer+k]
#         maxNum = max( maxNum, curNum)
#     return maxNum/k


# print(bigAVG(nums,k))


from typing import Counter


list_=[1,2,3,4,4,4]
print(type(Counter(list_)))
counter2 = Counter(list_)
hashMap={}
hashMap[0] = counter2
print(hashMap)