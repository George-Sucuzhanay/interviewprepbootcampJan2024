class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}
        result = []
        # aet : index

        for i in range(len(strs)):
            tmp = sorted(strs[i]) # understand how sorted works and the type it produces
            tmp = ''.join(tmp)
           
            # check if in my sorted dict then check it already exists in my nested list output      
        
            if tmp in output and result.count(strs[output[tmp]]) == 0 :
                print("no count")
                result.append([strs[output[tmp]], strs[i]])
            elif tmp in output:
                print("yes count")
                result[strs[output[tmp]]].append( strs[i])
            else:
                print("new entering dict first time")
                output[tmp] = i

        # combine list in list that have duplicates into one list: yes
        # include strs[i] that were never in result at all: work in progress
        print(output)
        print(result[:])
        return result



# what is above was my inital approach which did not work
        
# looking for more answers similar to my approach I got here
        


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sorted_to_anagrams = {}  # Initialize a dictionary to map sorted words to their anagram groups
    anagram_groups = []  # Initialize a list to store groups of anagrams

    for word in strs:  # Iterate over each word in the input list
        sorted_word = ''.join(sorted(word))  # Sort the characters in the word and join them to form a string

        if sorted_word in sorted_to_anagrams:
            # If the sorted word is already a key in the dictionary,
            # append the original word to the corresponding anagram group
            sorted_to_anagrams[sorted_word].append(word)
        else:
            # If the sorted word is not in the dictionary, this is a new anagram group
            new_group = [word]  # Create a new group starting with the current word
            anagram_groups.append(new_group)  # Add this new group to the list of anagram groups
            sorted_to_anagrams[sorted_word] = new_group  # Add the new group to the dictionary

    return anagram_groups  # Return the list of anagram groups


# examples of how this looks like
# sorted_to_anagrams

# {
#     'aet': ['eat', 'tea', 'ate'],
#     'ant': ['tan', 'nat'],
#     'abt': ['bat']
# }

# anagram_groups

# [
#     ['eat', 'tea', 'ate'],
#     ['tan', 'nat'],
#     ['bat']
# ]


