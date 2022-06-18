#Topic: Two Pointers
#난이도: 하
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        nums2 = list(nums)
        start = 0 
        end = len(nums2) -1 
        
        for i in nums:
            if i != 0:
                nums2[start] = i
                start = start + 1
            else:
                nums2[end] = i
                end = end - 1
            
            
        for i in range(len(nums)):
            nums[i] =nums2[i]
        """
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[start] = nums[start],nums[i]
                start += 1
            
            
'''
다른 풀이 
추가 메모리 없이 해결(two points)

start = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i],nums[start] = nums[start],nums[i]
        start += 1

'''
