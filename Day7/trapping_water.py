#Trapping Rainwater Leetcode
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         ans = 0
#         n = len(height)
#         if (n == 0 or n == 1):
#             return 0
#         l = [0] * n
#         l[0] = height[0]
#         for i in range(1, n):
#             l[i] = max(l[i - 1], height[i])
#         r = [0] * n
#         r[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             r[i] = max(r[i + 1], height[i])
#         for i in range(n):
#             ans += min(l[i], r[i]) - height[i]
#
#         return ans

#2pointer soln
def trap(arr):
    result = 0

    # maximum element on left and right
    left_max = 0
    right_max = 0
    #n = len(a)
    # indices to traverse the array
    lo = 0
    hi = len(arr) - 1

    while (lo <= hi):

        if (arr[lo] < arr[hi]):

            if (arr[lo] > left_max):

                # update max in left
                left_max = arr[lo]
            else:

                # water on curr element = max - curr
                result += left_max - arr[lo]
            lo += 1

        else:

            if (arr[hi] > right_max):
                # update right maximum
                right_max = arr[hi]
            else:
                result += right_max - arr[hi]
            hi -= 1

    return result




print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))