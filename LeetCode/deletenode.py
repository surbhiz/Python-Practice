

class Solution:
    def deleteNode(self, node):
        result = []
        for i in head:
            if node != i:
                result.append(i)
        print((result))


head = [1, 2, 3, 1, 4, 5]
node = 3
print(Solution.deleteNode([], node))
