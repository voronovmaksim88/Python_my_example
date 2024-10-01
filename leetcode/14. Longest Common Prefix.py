# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
#
# Example 2:
#
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i]
# consists of only lowercase English letters.


class Solution:
    def LongestCommonPrefix(self, strs: list[str]) -> str:
        common_str = ""
        min_str = strs[0]
        for i in strs:
            if len(i) < len(min_str):
                min_str = i
        print(min_str)

        for i in range(0, len(min_str)):
            print(i, end=" ")
            print(min_str[i])

            equally = False
            for j in strs:
                if min_str[i] == j[i]:
                    equally = True
                else:
                    equally = False
                    break

            if equally:
                common_str += min_str[i]
            else:
                break

        return common_str


a = Solution()
strs = ["flower", "flow", "flight"]
print(a.LongestCommonPrefix(strs))
