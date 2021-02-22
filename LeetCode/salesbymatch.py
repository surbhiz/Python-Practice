class Solution:
    def sockMerchant(self, n, ar):
        result = []
        for i in ar:
            if n == 0:
                return 0
            else:
                if i not in result:
                    result.append(i)
        print((result))


n = 5
ar = 1, 1, 2, 1, 3
print(Solution.sockMerchant([], n, ar))
