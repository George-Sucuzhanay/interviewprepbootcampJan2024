def containsDuplicateBruteForce(nums):
    #brute force time complexity of O(n^2) but a space complexity of O(1)
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True 

    return False
 
def containsDuplicateMap(nums):
    map1={}
    for i in nums:
        if i in map1:
            return True
        else:
            map1[i]=True
    
    return False

nums1 = [1,7,3,4,6,7]
nums2 = [1,7,3,4,6]
print(containsDuplicateBruteForce(nums1))
print(containsDuplicateMap(nums1))
print(containsDuplicateBruteForce(nums2))
print(containsDuplicateMap(nums2))      


# my notes 1/2/24
# leetcode 217
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         # time complexity O(n^2)
#         # arrays/lists
#         # hashmap approach records every instance so we could return the key whose value is at least 2 or nested loop
#         # revist how range method works with starting position
#         # revist all python methods that exist
#          # isDuplicate = False
#         # for i in range(len(nums)):
#         #     for j in range(i+1, len(nums)):
#         #         print(i, j)
#         #         if nums[i] == nums[j]:
#         #             isDuplicate = True
#         # return isDuplicate

#         # time complexity O(n)
#         # O(1) hashmap lookup time
#         # maps/dictionaries/hashmaps
#         # we don't even need to record num of occurances since we could just do lookups on their existence on the hashmap
#         # keys become our indicies like in arrays
        
#         map1 = {}
#         for i in nums:
#             if i in map1:
#                 return True
#             else:
#                 map1[i] = True
#         return False
