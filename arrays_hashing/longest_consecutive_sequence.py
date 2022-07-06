# This is neetcodes solutuion
# His for loop and if statement finds the the least number in sequences
# then his while loop finds the length of the sequence
# for empty lists longest is 0 for lists with 1 elemnt
# longest gets changed to 1 because length is set to 1 then longest is set to max of 
# length or longest

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest
