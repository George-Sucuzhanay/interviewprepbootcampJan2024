def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

# leetcode 1
# time complexity O(n^2)
# space complexity O(1)


# using hashmap to reduce time complexity to
# O(n)


#  def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices= [0] * 2   =>   created an array [0, 0]
#         dict = {}
#         for i, val in enumerate(nums):      enumerate
#             if val in dict.keys():
#                 indices[0] = i
#                 indices[1] = dict[val]
#                 return indices
#             dict[target - val] = i


# dict = {}
#         for i, val in enumerate(nums):      enumerate
#             if val in dict:
#                return i , dict[val]
#             dict[target - val] = i