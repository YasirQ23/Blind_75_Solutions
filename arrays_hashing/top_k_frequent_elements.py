#neetcode solution
#Hes creating a list of frequencys each list is empty in this list
#then creats a map of the numbers
#then loops through the map the key of the map is the number
#and the value is its frequency since you can now add it to that location in a the fequency list
# then you can travese the list backwards to get the most frequent answers
#this is called bucket sort maybe 

class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res