#Hash Table
'''
In order to improve the time complexity, an efficient method for checking whether a complement exists in an array is needed. If there is a payoff, it is necessary to search the corresponding index. The best way to keep a mapping of each element of an array to an index is a hash table.
We reduce the search time from O(n) to O(1) by trading space for speed. Hash tables are built for exactly this purpose, and support fast lookups of near constant time. The reason I said "nearly" is that if collisions happen, the search can be bad in O(n) time. However, if the hash function is chosen carefully, the search of the hash table is O(1) partitioned.
A simple implementation would use two loops. In the first iteration, we add the value and index of each element to the table. Then, in the second iteration, we check if the complement (target - nums[i]) of each element is in the table. The payoff MUST NOT be nums[i].

보수(complement)로 indexing을 한다고 생각하자.
key - value 중에 보수로 key를 만든다. 

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] not in hash_dict:
                hash_dict[target - nums[i]] = i
            else: 
                return hash_dict[nums[i]],i
                
            

        
        