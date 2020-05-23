'''
69. Sqrt(x)
https://www.youtube.com/watch?v=VYtEKhxKd1Q

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.


'''

def mysqrt(x):
    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2
        b = mid*mid
        if b == x:
            return mid
        elif b < x:
            left = mid + 1
        else:
            right = mid - 1

    # return right
    return left-1


x =90
print(mysqrt(x))