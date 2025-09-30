class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #num1,num2=set(nums1), set(nums2)
        #return list(num1&num2)

        #두 포인트로풀기
        nums1.sort()
        nums2.sort()
        result=set()
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                result.add(nums1[i])
                i+=1
                j+=1
        return list(result)