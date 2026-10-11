class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 
        k = 0

        while left < len(nums):
            if nums[left] == val: 
                nums[left] = 0
                left += 1
            else:
                left += 1
                k += 1 

        nums = nums.sort(reverse=True)

        return k