class Solution:
    def deleteNode(self, node):
        head.reverse()
        head.remove(head[node-1])
        head.reverse()
        print(head)


head = [1, 2, 3, 1, 4, 5]
node = 1
print(Solution.deleteNode([], node))
