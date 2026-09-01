class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Comparison of dictionaries
        if len(s) != len(t):
            return False # not same number of letters so immediately fail
        # Can be sure at this point that the length of s == len(t)
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
        return s_dict == t_dict
