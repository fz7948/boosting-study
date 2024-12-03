# https://leetcode.com/problems/integer-to-english-words/
# 난이도: hard
# Frequency 정렬

class Solution:
    def numberToWords(self, num: int) -> str:
        unit = [None, "Thousand", "Million", "Billion", "Trillion"]
        ten_unit = [None, "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        hundred = "Hundred"
        one_unit = [None, "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

        def makeTen(num):
            ret = ""
            num_ten = num % 100
            if num >= 100:
                ret += one_unit[num // 100] + " " + hundred
            if num_ten >= 20:
                n = num_ten // 10
                m = num_ten % 10
                j = ""
                if ret:
                    j += ret + " "
                if ten_unit[n]:
                    j += ten_unit[n] + " "
                if one_unit[m]:
                    j += one_unit[m]
                return j.strip()
            elif num_ten >= 10:
                if ret:
                    return ret + " " + ten[num_ten % 10]
                else:
                    return ten[num_ten % 10].strip()
            else:
                if ret and one_unit[num_ten % 10]:
                    return ret + " " + one_unit[num_ten % 10]
                elif ret:
                    return ret
                return one_unit[num_ten % 10]

        if num == 0:
            return "Zero"
        num2 = num
        split_num = []
        while num2:
            split_num.append(num2 % 1000)
            num2 //= 1000
        
        idx = 0
        ans = []
        while split_num:
            n = split_num.pop(0)
            if unit[idx] and makeTen(n):
                ans.append(makeTen(n) + " " + unit[idx])
            elif makeTen(n):
                ans.append(makeTen(n))
            idx += 1
        ans = " ".join(ans[::-1])
        return ans
        
            
        