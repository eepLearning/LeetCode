#Binary Search
#Binary Search 알고리즘은 정렬된 배열에서 타켓을 찾는 대표적인 로그 시간(logn) 알고리즘이다
# UP & Down 게임처럼 탐색이 진행될 때마다 범위를 절반씩 좁혀가면서 탐색한다. 

class Solution:
    def search(self, nums, target):
        start = 0 
        end = len(nums)-1
        while start <= end:
            pivot = (end+start)//2
            if nums[pivot] == target:
                return pivot 
            elif nums[pivot] > target:
                end = pivot-1
            else:
                start = pivot + 1
        return -1
                
        
        