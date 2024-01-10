def maxArea(height):

    #brute force

    max_area = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = (r-l)*min(height[l], height[r]) # r-l is our width our height is min of l and r
            max_area = max(max_area, area)
    return max_area

# time complexity: O(n^2)
# space complexity: O(1)


def maxAreaTwoPointer(height):
    l, r = 0, len(height) - 1

    while l <  r:
        area = max((r-l)*min(height[l], height[r]), area)
        # make my new area the exisiting area or new area calculated

        if height[l] < height[r]:
            l+=1
        else:
            r-=1

    return area

# time complexity: O(n)
# space complexity: O(1) 
