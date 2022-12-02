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
        n = len(nums) - 1
        while( i < n ):
            j = i + 1
            while (j < n ):
                curr  = nums[i] + nums[j]
                if curr == target:
                    break
                j += 1

            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)
                break
            i += 1
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

if __name__ == "__main__":
    num = [3,2,4]
    target = 6
    #num = [0,4,3,0]
    #target = 0
    solution = Solution()
    print(solution.twoSum_2(num, target))