nums = [1,12,-5,-6,50,3]
k = 4
#Output: 12.75000
#Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# def bigAvg(x,y):
#     hashMap = {}
#     counter1 = 0
#     counter2 = counter1+y
#     while counter2 != len(x):
#         hashMap[sum(x[counter1:counter2])] = hashMap.get(sum(x[counter1:counter2]),0) + 1
#         counter1 +=1
#         counter2 += 1
#     return max(hashMap)/y

# def bigAvg(x,y):
#     hashSet = set()
#     counter1 = 0
#     if y==1:
#         return max(x)
#     while counter1+y != len(x):
#         hashSet.add(sum(x[counter1:counter1+y])/y)
#         counter1+=1
#     return max(hashSet)
