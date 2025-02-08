1.First approach to spilt the words2 List:
class Solution(object):
    def wordSubsets(self, words1, words2):
                new_list = []
        words2_count = {}
        for word in words2:
            for char in word:
                words2_count[char] = max(words2_count.get(char,0),word.count(char))
        for word in words1:
            words1_count = {}
            for char in word:
                words1_count[char] = words1_count.get(char,0)+1

            is_universal = True
            for char in words2_count:
                if words1_count.get(char,0) < words2_count[char]:
                    is_universal = False
                    break
            
            if is_universal:
                new_list.append(word)
        return new_list


2. Method-Two:
class Solution:
    def wordSubsets(self, A, B):
        cnt = Counter()
        for b in B:
            cnt |= Counter(b)
            
        return [a for a in A if not cnt - Counter(a)]