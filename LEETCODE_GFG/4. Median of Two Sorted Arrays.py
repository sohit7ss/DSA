class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def merge_two(left, right):
            result = []
            i, j = 0, 0
            n, m = len(left), len(right)

            while i < n and j < m:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < n:
                result.append(left[i])
                i += 1

            while j < m:
                result.append(right[j])
                j += 1

            return result

        m_arr = merge_two(nums1, nums2)
        n = len(m_arr)

        if n % 2 == 0:
            median = (m_arr[n // 2 - 1] + m_arr[n // 2]) / 2
        else:
            median = m_arr[n // 2]

        return median


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l3=sorted(nums1+nums2)
        if len(l3)%2==0:
            m=(l3[len(l3)//2-1]+l3[len(l3)//2])/2
        else:
            m=l3[(len(l3)+1)//2-1]
        return(float(m))