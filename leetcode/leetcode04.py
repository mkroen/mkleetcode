from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        i,j = 0, 0
        while True:
            if i >= len_nums1:
                nums += nums2[j:]
                break
            if j >= len_nums2:
                nums += nums1[i:]
                break
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        is_double = not (len_nums1+len_nums2)%2
        index = (len_nums1+len_nums2-1) // 2
        if is_double:
            return (nums[index] + nums[index+1])/2
        else:
            return nums[index]
    
    def findMedianSortedArrays_v2(self, nums1: List[int], nums2: List[int]) -> float:
        # 有空处理下，不需要额外空间的方法，有点问题，几十个用例过不了
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        length = len_nums1 + len_nums2
        is_double = not length%2
        index = (length-1) // 2
        ans = []
        tag = 0
        tag1 = 0
        tag2 = 0
        import pdb
        pdb.set_trace()
        while True:
            if len_nums1 <= tag1:
                ans.append(nums2[index-tag+len_nums1])
                if len(ans) < is_double+1:
                    ans.append(nums2[index-tag+1])
                break
            if len_nums2 <= tag2:
                ans.append(nums1[index-tag+len_nums2])
                if len(ans) < is_double+1:
                    ans.append(nums1[index-tag+1])
                break
            if nums1[tag1] < nums2[tag2]:
                last = nums1[tag1]
                tag1 += 1
            else:
                last = nums2[tag2]
                tag2 += 1
            if index == tag:
                ans.append(last)
                if len(ans) < is_double+1:
                    if len_nums1 <= tag1:
                        ans.append(nums2[tag2])
                    elif len_nums2 <= tag2:
                        ans.append(nums1[tag1])
                    else:
                        ans.append(min((nums2[tag2],nums1[tag1])))
                break
            tag += 1
        return sum(ans)/len(ans)

S = Solution()
a = [1,3]
b = [2]
print(S.findMedianSortedArrays(a,b))