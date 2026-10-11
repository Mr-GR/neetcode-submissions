class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        for elem in nums:
            temp.append(elem)
        ans = nums + temp
        return ans 