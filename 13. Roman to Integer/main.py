class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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
        n = len(s)

        for i in range(n - 1):
            cur, nxt = numbers[s[i]], numbers[s[i+1]]
            if cur < nxt:
                total -= cur
            else:
                total += cur

        return total + numbers[s[-1]]

        
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.romanToInt("IX"))

