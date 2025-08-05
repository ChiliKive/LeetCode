class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[s]
        
        numbers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            value = numbers[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total

        
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.romanToInt("IX"))

