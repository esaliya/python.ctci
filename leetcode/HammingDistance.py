import sys
import math


#https://leetcode.com/problems/hamming-distance/description/
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        maxVal = max(x, y)
        if maxVal == 0:
            return 0
        exp = (int (math.log2(maxVal)))
        count = 0
        for i in range(exp+1):
            count += (x & 1) ^ (y & 1)
            x = x >> 1
            y = y >> 1
        return count


def main(argv):
    s = Solution()
    print(s.hammingDistance(0,1))


if __name__ == '__main__':
    main(sys.argv)
