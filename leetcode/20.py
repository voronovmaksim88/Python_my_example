"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""

s = "(])"
result = True
test_str = ""
test_str += s[0]

for i in range(1, len(s)):
    if s[i] == "(" or s[i] == "[" or s[i] == "{":
        test_str += s[i]
        # print(test_str)
    if s[i] == ")" or s[i] == "]" or s[i] == "}":
        if len(test_str) == 0:
            result = False
            break
        if (test_str[len(test_str) - 1] == "(" and s[i] == "]") or \
                (test_str[len(test_str) - 1] == "(" and s[i] == "}") or \
                (test_str[len(test_str) - 1] == "[" and s[i] == ")") or \
                (test_str[len(test_str) - 1] == "[" and s[i] == "}") or \
                (test_str[len(test_str) - 1] == "{" and s[i] == ")") or \
                (test_str[len(test_str) - 1] == "{" and s[i] == "]"):
            result = False
            break

        if test_str[len(test_str) - 1] == "(" and s[i] == ")" or \
                test_str[len(test_str) - 1] == "[" and s[i] == "]" or \
                test_str[len(test_str) - 1] == "{" and s[i] == "}":
            test_str = test_str[0:- 1]

if len(test_str) > 0:
    result = False

if test_str == "":
    print(result)
else:
    print(result)
