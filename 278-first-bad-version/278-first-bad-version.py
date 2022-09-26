#Binary Search
# check : 2

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start,end = 1,n
        if start == end:
            return 1
        while start <= end:
            pivot = (start+end)//2
            if isBadVersion(pivot):
                end = pivot - 1
            else:
                start = pivot + 1
        return start
                
    
        