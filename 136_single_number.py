'''
136. Single Number
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Method:
XOR operation



'''

# brute-force
def singleno(nums):
    res = 0
    for i in range(len(nums)):
        res ^= nums[i]
    return res




# nums = [4,1,2,1,2,4,5]
nums = [1,0,1]
print(singleno(nums))