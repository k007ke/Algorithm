class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 반복 풀이
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                return mid
        return -1
            
        #이진검색모듈사용
        index=bisect.bisect_left(nums,target)
        if index<len(nums) and nums[index]==target:
            return index
        else:
            return -1



        