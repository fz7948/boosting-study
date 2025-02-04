# https://leetcode.com/problems/bulls-and-cows/description/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls_count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls_count += 1
        from collections import Counter
        secret_counter = Counter(secret)
        guess_counter = Counter(guess)
        
        
        cows_count = 0
        cows_count -= bulls_count
        for k,v in secret_counter.items():
            if k in guess_counter:
                cows_count += min(guess_counter[k], v)
        
        return str(bulls_count)+"A"+str(cows_count) + "B"