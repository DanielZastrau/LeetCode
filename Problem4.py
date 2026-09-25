"""Classification: Hard
Beats 100% on runtime and 80% on memory usage"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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

            n1 = nums1[pointer_one] if pointer_one < len(nums1) else float('inf')
            n2 = nums2[pointer_two] if pointer_two < len(nums2) else float('inf')

            if n1 > n2:
                e1, e2 = e2, n2
                counter += 1
                pointer_two += 1

            elif n1 < n2:
                e1, e2 = e2, n1
                counter += 1
                pointer_one += 1

            else:
                e1, e2 = e2, n1
                counter += 1
                pointer_one += 1

                if not counter -1 == find:
                    e1, e2 = e2, n2
                    counter += 1
                    pointer_two += 1

            if counter - 1 == find:

                if parity == 1:
                    return e2

                else:
                    return (e1 + e2) / 2

if __name__=='__main__':

    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))