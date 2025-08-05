class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev_value = 0
        
        for char in reversed(s):
            if char == 'I':
                value = 1
            elif char == 'V':
                value = 5
            elif char == 'X':
                value = 10
            elif char == 'L':
                value = 50
            elif char == 'C':
                value = 100
            elif char == 'D':
                value = 500
            else:  # char == 'M'
                value = 1000
            
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        return total
        
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.romanToInt("IX"))

