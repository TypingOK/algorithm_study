# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        answer = -1
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next

        for i in range(len(temp)//2):
            answer = max(answer, temp[i] + temp[len(temp)-1 - i])
        return answer
