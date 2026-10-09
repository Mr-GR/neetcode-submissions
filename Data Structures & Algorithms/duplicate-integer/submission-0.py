class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for elem in nums:
            if elem in duplicate:
                return True
            duplicate.add(elem)
        return False