def isPalindrome(s):
    # sts and chars have bulit in func isalnum() where c is a char
    # this function returns whether or not the current char is an alphanumeric char
    # chars have a c.lower(), where c is a char
    # c == 'A'  then c.lower() == 'a'

    # wow is a palindrome   


    s1=''  # does not contain non-alpha chars
    # what is the difference between traversing a string vs traversing an array

    for c in s: 
        # why does s[c] not work in line 15??
        if c.isalphanum():
            s1+=c.lower()
    
    return s1==s1[::-1]   # sub_arr[start:end:step]

    # time complexity: O(n) where n is the size of string s
    # space complexity: O(2 x n) => O(n)
    # b/c we allocate size of s in s1 and create a new arr when doing s1[::-1]


    # two pointer solution:
    # time complexity: O(n)
    # space complexity: O(1) b/c we traverse in place of str s
    l, r = 0, len(s) - 1
    while l < r:


# memorize all convertions and built in methods that exist in Python
# understand the meaning to have return and continue statements
 


