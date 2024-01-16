def search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start + end) // 2 # integer division w/ flooring
        if target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            end = mid - 1
        else:
            return mid
    return -1

    # time: log n
    # space: O(1)



