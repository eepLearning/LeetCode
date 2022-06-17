#Binary Search
#Insert할 Position을 찾는 문제
#난이도: 중
#bisect solution
#return bisect.bisect_left(nums,target)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start,end = 0, len(nums)-1
        
        while start <= end:
            pivot = (start + end) //2 
            
            if nums[pivot] == target:
                return pivot
            
            elif nums[pivot] > target :
                end = pivot - 1
            else:
                #nums[pivot] < target:
                start = pivot+1
        return start
     