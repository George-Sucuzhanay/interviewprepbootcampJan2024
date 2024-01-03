
def isAnagram( s: str, t: str) -> bool:
    # 1) create s hashmap
    # 2) for every element in s create a key-value pair
    # 3) traverse s' hashmap ensuring that a element in t exisit
    #     yes: increase value by 1
    #     no: return false
    # 4)
    # could either get both s and t into hashmap lookup the values of the same keys (check to see if the same num occurances occur)
    # or 
    # (picked this one)traverse t and increase value then at the end check for even numbers
    # O(n) time complexity

    s_map = {}

    for i in s:
        if i in s_map:
            s_map[i] += 1
        else:
            s_map[i] = 1

    for j in t:
        if j in s_map:
            s_map[j] += 1
        else:
            s_map[j] = 1

    for z in s_map:
        if s_map[z] % 2 != 0:
            return False
    return True


s = "anagram"
t = "nagaram"

print(isAnagram(s,t));

# leetcode 242