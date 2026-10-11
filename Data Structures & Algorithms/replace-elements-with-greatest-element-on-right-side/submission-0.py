class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        right = len(arr) - 1
        max_value = -1

        while right >= 0:
            current = arr[right]

            arr[right] = max_value 

            if current > max_value:
                max_value = current

            right -= 1
        return arr 
            