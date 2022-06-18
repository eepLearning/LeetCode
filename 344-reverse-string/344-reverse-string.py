#Topic: Two Pointers
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        #그냥풀기
        345 ms / 18.4 MB 
        s.reverse()
        '''
        start = 0
        end = len(s) -1 
        while start < end:
            s[start],s[end] = s[end],s[start]
            end -= 1
            start += 1
            
        