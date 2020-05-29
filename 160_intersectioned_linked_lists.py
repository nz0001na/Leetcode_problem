'''
160. Intersection of Two Linked Lists
Easy
https://github.com/grandyang/leetcode/issues/160

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def intersection(headA, headB):
    if not headA or not headB:
        return None
    curA = headA
    countA = 1
    while curA:
        curA = curA.next
        countA += 1

    curB = headB
    countB = 1
    while curB:
        curB = curB.next
        countB += 1

    print(countA)
    print(countB)

    curA = headA
    curB = headB
    if countA > countB:
        while countA > countB:
            curA = curA.next
            countA -= 1
    elif countA < countB:
        while countB > countA:
            curB = curB.next
            countB -= 1

    while curA and curB:
        if curA == curB:
            return curA
            # return True
        curA = curA.next
        curB = curB.next

    return None


def intersection2(headA, headB):
    if not headA or not headB:
        return None
    curA = headA
    curB = headB
    while curA != curB:
        if not curA:
            curA = headB
        else:
            curA = curA.next

        if not curB:
            curB = headA
        else:
            curB = curB.next

    return curA






# listA = [4, 1, 8, 4, 5], listB = [5, 0, 1, 8, 4, 5],
#


a = ListNode(5, None)
b = ListNode(4, a)
c = ListNode(8, b)
d = ListNode(1, c)
headA = ListNode(4, d)

d2 = ListNode(1, None)
e2 = ListNode(0, d2)
headB = ListNode(5, e2)

l = intersection2(headA, headB)
print(l)
