# https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-10
# hash table 생각보다 아이디어는 간단한데, 최적화(?) 간단하게 필요함..?

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import Counter, defaultdict

        words1_counter = []
        for w1 in words1:
            words1_counter.append(Counter(w1))
        
        words2_counter = defaultdict(int)
        for w2 in words2:
            counter = Counter(w2)
            for w in w2:
                # print(w2, w)
                words2_counter[w] = max(counter[w], words2_counter[w])
        # print(words2_counter)
        
        ans_idx = set()
        for i, w1c in enumerate(words1_counter):
            check = True
            for k, v in words2_counter.items():
                if not k in w1c:
                    check = False
                    break
                elif w1c[k] < v:
                    check = False 
                    break
            if check:
                ans_idx.add(i)
        ans = []
        for i in ans_idx:
            ans.append(words1[i])
        return ans
            