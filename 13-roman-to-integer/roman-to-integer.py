class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I' : 1 ,'V' : 5 ,'X' : 10 ,'L' : 50 ,'C': 100 ,'D' :500
        ,'M' : 1000}

        total = 0
        
        for i in range(len(s) -1):
            current_value = d[s[i]]
            next_value = d[s[i+1]]

            if current_value < next_value :
                total -= current_value
            else:
                total += current_value

        total += d[s[-1]]

        return total
        