class Solution:
    def twoSum(numbers, target: int):
        # sliding window or hashmap implementation
        # is it similar to twosum?
        # can we do a operation that looks like a + b = target
        # b = target - b

        # easiest solution O(n^2)
        output = []

        for i in range(len(numbers)):
            print("start", numbers[i])
            for j in range(i+1, len(numbers)):
                print("check with", numbers[j])
                if numbers[i] + numbers[j] == target:
                    print("its equal!")
                    output.append(i + 1)
                    output.append(j + 1)
        return output
    
        # the use of hashmaps is ideally the best solution


# 1/5/2024
# we can't use a hashmap
# we will always are going to add additonal space to use
    

# problem statement asks we use ONLY constant extra space
    
# topic: two pointer     its a relative to sliding window


# nums = [ -7, 0, 1, 2, 4, 7, 8]
# target = 11
# use left pointer in leftmost side
# use right pointer in rightmost side

# nums[l] + nums[r] = 11  this becomes a running sum
# move left pointer left to increase and move right pointer right to reduce
# only works if the array is already sorted
 

def twoSumClassExample(numbers, target):
    l, r = 0 , len(numbers) - 1
    
    while l < r:
        if numbers[l] + numbers[r] < target:
            l+=1
        elif numbers[l] + numbers[r] > target:
            r-=1
        else:
            return l + 1, r + 1
        

        
        
