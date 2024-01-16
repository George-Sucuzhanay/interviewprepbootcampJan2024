# leetcode 20 valid parentheses

def isValid(self, s):
    # map check occurence of diff type of symbols
    # stacks are the best way to tackle the problem
    #  ()   valid parenthesis are always palindromes
    close_to_open = {'}' : '{',  ']': '[', ')' : '('}   

    stack = []
    for c in s:
        if c in close_to_open.values():
            stack.append(s)
        elif stack and stack[-1] == close_to_open[c]:
            stack.pop()
        else:
            return False
            
    return not stack # if stack is empty return True else False