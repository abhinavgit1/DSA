class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i,el in enumerate(operations):
            if el == '+':
                res.append(res[-1] + res[-2])
            elif el == 'D':
                res.append(2*res[-1])
            elif el == 'C':
                res.pop()
            else:
                res.append(int(el))
        return sum(res)