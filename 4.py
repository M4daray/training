class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ """
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0:
            median = (arr[floor(len(arr)/2)-1] + arr[floor(len(arr)/2)]) / 2 
        else:
            median = arr[floor(len(arr)/2)]

        return median