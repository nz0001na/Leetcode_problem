'''
72. Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Approach 1:
https://www.youtube.com/watch?v=We3YDTzNXEk
https://www.youtube.com/watch?v=MiqoA-yF-0M


'''


def minDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = [[None for j in range(len2+1)] for i in range(len1+1)]

    for i in range(0, len1+1):
        dp[i][0] = i
    for j in range(0, len2+1):
        dp[0][j] = j

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1

    return dp[len1][len2]


word1 = "intention"
word2 = "execution"
print(minDistance(word1, word2))