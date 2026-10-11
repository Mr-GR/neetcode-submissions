class Solution:
    def calPoints(self, operations: List[str]) -> int:
        curr = [] 

        for elem in operations:
            if elem == '+':
                curr.append(curr[-1] + curr[-2])
            elif elem == 'D':
                curr.append(curr[-1] * 2)
            elif elem == 'C':
                curr.pop()
            else:
                curr.append(int(elem))
        ans = sum(curr)
        return ans
