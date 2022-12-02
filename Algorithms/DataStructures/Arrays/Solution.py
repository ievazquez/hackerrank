from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        elements = nums.copy()
        elements.sort()
        while left < right:
            currValue = elements[left] + elements[right]
            if currValue == target :
                ans.append(nums.index(elements[left]))
                ans.append(nums.index(elements[right]))
                break
            if currValue > target :
                right -= 1
            else:
                left += 1
        return ans

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        i = 0
        ans = []
        map = {}
        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if x in map:
                return [map[x], i]
            map[nums[i]] = i
        return ans
"""

def sumTarget( nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] > target :
            right -= 1
        elif  nums[ left ] + nums[right] < target:
            left += 1
        else:
            return True

    return False


"""
""""
nums =
[2,7,11,15]
target =
9

nums =
[3,3]
target =
6

nums =
[3,2,4]
target =
6

[0,4,3,0]
0

    num = [1, 2, 4, 6, 9, 14]
    target = 13

"""

"""
force brute
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
"""
if __name__ == "__main__":
    #num = [3,2,4]
    #target = 6
    num = [0,4,3,0]
    target = 0
    solution = Solution()
    print(solution.twoSum_2(num, target))