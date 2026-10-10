class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # iterate throuh the array 
        # count = 0 
        # array = ans = []
        # nums=[1,0,1,1,0,1]
        # nums=[1,1,0,1,1,1]
        count = 0 

        left = 0 

        ans = []

        while left < len(nums):
            if nums[left] == 1:
                count += 1 
                left += 1 

            elif nums[left] == 0:
                ans.append(count)
                count = 0
                left += 1
                
        ans.append(count)

        return max(ans)



