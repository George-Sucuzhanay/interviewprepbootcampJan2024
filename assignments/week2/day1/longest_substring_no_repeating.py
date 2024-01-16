# longest substring w/o repeating characters
# brute force inefficent version of dynamicially sized sliding window

def lengthofLongestSubstring(s):
    max_length = 0
    for l in range(len(s)):
        char_set = set() # like a map but no repeating chars
        # set is a collection of items that are unique and are mutable
        # char set is a set of characters, and we only have 26 chars
        for r in range(l, len(s)):
            if s[r] in char_set:
                break
            else:
                char_set.add(s[r])
                max_length = max(max_length, len(char_set))
    return max_length

# time complexity: O(n^2)
# space complexity: O(26) => O(1)

# l and r start in the same position

# optimized version

def betterLengthOfLongestSubstring(s):
    l, r, max_length = 0, 0, 0
    char_set = set()
    while r < len (s):
        if s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        else:
            char_set.add(s[r])
            max_length = max(max_length, len(char_set))
            r += 1
    return max_length

# time complexity: O(n)
# space complexity: O(26) => O(1)

# done 11 problems :)