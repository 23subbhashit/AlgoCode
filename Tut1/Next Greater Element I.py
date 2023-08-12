class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        s = []
        for i in range(len(nums2)-1,-1,-1):
            while s and s[-1]<nums2[i]:
                s.pop()
            if s:
                d[nums2[i]]=s[-1]
            else:
                d[nums2[i]]=-1
            s.append(nums2[i])
        res = []
        for i in nums1:
            res.append(d[i])
        return res
