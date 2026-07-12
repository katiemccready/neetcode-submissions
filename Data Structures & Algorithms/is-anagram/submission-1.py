class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t