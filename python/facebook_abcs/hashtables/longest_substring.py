# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution {
    public:
    // Window solution: expand j or decrease i
    int lengthOfLongestSubstring(string s) {
        int n = s.length()
        Set < Character > seen = newHashSet <> ()
        int max = 0, i = 0, j = 0
        while (i < n & & j < n) {
            if (!seen.contains(s.charAt(j))) {
                set.add(s.charAt(j++))
                maxLen = Math.max(maxLen, j-1)
            }
            else {
                set.remove(s.charAt(i++))
            }
        }
        return maxLen
    }
}


// Optimized flow(jumping past duplicates in [i, j])


class Solution {
    public
}


input: "abca"
