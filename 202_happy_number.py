'''
202. Happy Number
https://www.youtube.com/watch?v=c8J9SLaoSMU
https://github.com/grandyang/leetcode/issues/202
Easy
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 8^2
8^2 + 2^2 = 6^8
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

In base 10, the 143 10-happy numbers up to 1000 are:

1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496, 536, 556, 563, 565, 566, 608, 617, 622, 623, 632, 635, 637, 638, 644, 649, 653, 655, 656, 665, 671, 673, 680, 683, 694, 700, 709, 716, 736, 739, 748, 761, 763, 784, 790, 793, 802, 806, 818, 820, 833, 836, 847, 860, 863, 874, 881, 888, 899, 901, 904, 907, 910, 912, 913, 921, 923, 931, 932, 937, 940, 946, 964, 970, 973, 989, 998, 1000

'''
def isHappy(n):
    s = str(n)
    hashmap = {}
    while 1:
        sum = 0
        for i in range(len(s)):
            sum += int(s[i])**2
        if sum == 1:
            return True
        if sum not in hashmap:
            hashmap[sum] = 1
            s = str(sum)

        else:
            return False

n = 31
print(isHappy(n))