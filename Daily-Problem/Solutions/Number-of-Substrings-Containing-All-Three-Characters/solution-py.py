class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        result = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            while all(count[char] > 0 for char in 'abc'):
                result += len(s) - right
                if s[left] in count:
                    count[s[left]] -= 1
                left += 1
        return result
