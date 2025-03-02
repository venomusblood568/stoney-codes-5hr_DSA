# Question Link -> https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        stack = []
        n = len(q) - k
        while k :
            stack.append(q.popleft())
            k -= 1
        while stack:
            q.append(stack.pop())
        while n:
            q.append(q.popleft())
            n -= 1
        return q
