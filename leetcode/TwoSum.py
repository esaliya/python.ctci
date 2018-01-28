import sys


# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # two loop method, which is expensive
        # for i in range(0, len(nums)):
        #     t = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == t:
        #             return [i, j]
        # return []

        # dictionary based method
        seen = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if nums[i] in seen:
                return [seen[nums[i]], i]
            else:
                seen[t] = i
        return [-1,-1]


def main(argv):
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    ret = s.twoSum(nums=nums, target=target)
    print(str(ret[0]) + " " + str(ret[1]))


if __name__ == "__main__":
    main(sys.argv)
