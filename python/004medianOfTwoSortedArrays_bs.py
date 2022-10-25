
from typing import List
# [1,3,4]
#[5,7,8]
# 3, 4 -> 6
# []
class MedianOfTwoSortedArrays(object):
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(num1) + len(num2)
        self.num1 = num1
        self.num2 = num2
        if n % 2 == 0:
            return self.getMedian(n // 2 - 1, 0, len(num1), 0, len(num2), True)
        return self.getMedian(n // 2, 0, len(num1), 0, len(num2), False)


    def getMedian(self, idx: int, left1: int, right1: int, left2: int, right2: int, getNext: bool):
        # if one of it len is 0 return other's kth
        num1Len = right1 - left1
        num2Len = right2 - left2
        # print(idx, left1, right1, left2, right2)

        print(left1, left2)
        if num1Len == 0:
            if getNext:
                return float(self.num2[left2+idx] + self.num2[left2+idx + 1])/2
            return self.num2[left2+idx]
        if num2Len == 0:
            if getNext:
                return float(self.num1[left1+idx] + self.num1[left1+idx + 1])/2
            return self.num1[left1 +idx]
        # if k == 0, return smaller one
        if idx == 0:
            if getNext:
                nums = self.num1[left1: left1 + 2] + self.num2[left2: left2 + 2]
                nums.sort()
                return float(nums[0] + nums[1])/2
            return min(self.num1[left1], self.num2[left2])
        # if half is still larger than one of the num, make the other half
        halfIdx = (idx + 1) // 2
        if num1Len < halfIdx:
            return self.getMedian(idx - halfIdx, left1, right1, left2+halfIdx, right2, getNext)
        if num2Len < halfIdx:
            return self.getMedian(idx - halfIdx, left1+halfIdx, right1, left2, right2, getNext)

        a = self.num1[left1 + halfIdx - 1]
        b = self.num2[left2 + halfIdx - 1]
        if a < b:
            return self.getMedian(idx - halfIdx,left1+halfIdx, right1, left2, right2, getNext)

        return self.getMedian(idx - halfIdx, left1, right1, left2+halfIdx, right2, getNext)

m = MedianOfTwoSortedArrays()
print(m.findMedianSortedArrays([1,3], [2]))
# print(m.findMedianSortedArrays([1,3,4], [5,7, 8]))
