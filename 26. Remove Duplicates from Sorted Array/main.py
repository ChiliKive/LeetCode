class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        f = nums[0]
        j = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 2]
    length = solution.removeDuplicates(nums)
    print(length) 
    print(nums[:length])

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = solution.removeDuplicates(nums)
    print(length)
    print(nums) 
