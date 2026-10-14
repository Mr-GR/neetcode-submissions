class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0 

        right = 0 

        check = []

        lst_s = list(s)

        lst_t = list(t)

        while left < len(lst_s) and right < len(lst_t):
            if lst_s[left] == lst_t[right]:
                check.append(lst_t[right])
                left += 1 
                right += 1
            else:
                right += 1

        return len(lst_s) == len(check)





        
        