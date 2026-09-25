"""Classification: Hard
Beats 100% on runtime and 80% on memory usage"""

class Solution:
    def findMedianSortedArraysLinSol(self, nums1: list[int], nums2: list[int]) -> float:
        """Linear solution"""
        
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        find = l // 2
        parity = l % 2
        
        pointer_one = 0
        pointer_two = 0
        counter = 0
        e1, e2 = 0, 0
        while True:

            n1 = nums1[pointer_one] if pointer_one < l1 else float('inf')
            n2 = nums2[pointer_two] if pointer_two < l2 else float('inf')

            if n1 >= n2:
                e1, e2 = e2, n2
                counter += 1
                pointer_two += 1

            elif n1 < n2:
                e1, e2 = e2, n1
                counter += 1
                pointer_one += 1

            if counter - 1 == find:

                if parity == 1:
                    return e2

                else:
                    return (e1 + e2) / 2

    def findMedianSortedArraysLogSol(self, nums1: list[int], nums2: list[int]) -> float:

        # let nums1 be the sorter list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        
        # size of the left half
        half = (m + n + 1) // 2

        lo, hi = 0, m
        while lo <= hi:

            # elems from the nums1
            i = (lo + hi) // 2       
            # elems from the nums2
            j = half - i

            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:   # valid partition
                if (m + n) % 2:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                # too many from nums1
                hi = i - 1
            else:
                # too few from nums1
                lo = i + 1

if __name__=='__main__':
    import time

    sol = Solution()
    nums1 = list(range(1, 10**8, 2))
    nums2 = list(range(2, 10**8, 2))

    t = time.time()
    sol.findMedianSortedArraysLinSol(nums1, nums2)
    print(time.time() - t)

    t = time.time()
    sol.findMedianSortedArraysLogSol(nums1, nums2)
    print(time.time() - t)
