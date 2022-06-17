'''
Two Pointers
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
난이도: 중

그냥 제곱하고 sort()하면 O(N logN)
핵심: 양쪽 절대값이 제일 크다라는 것을 알아차려야함
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start,end =0,len(nums)-1
        answer = [None]*len(nums)
        i = end 
        while(start <= end):
            if nums[start]**2 <= nums[end]**2:
                answer[i] = nums[end]**2
                end -=1 
            else:
                answer[i] = nums[start]**2
                start += 1
            i -=1
        
        return answer
            
                
                

        
        