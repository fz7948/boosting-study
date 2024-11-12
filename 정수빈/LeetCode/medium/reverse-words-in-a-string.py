# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = list(filter(lambda x: x != "", map(lambda x: x.strip(), s.strip().split(" "))))
    s = s[::-1]
    return " ".join(s)
    
print(reverseWords("a good   example"),"example good a" )