class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]
        i = 0

        while i < n:
            j = i

            # Elements belong to the same group
            # if their difference is <= limit
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Get values and original indices
            values = [arr[k][0] for k in range(i, j + 1)]
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Smallest values go to smallest indices
            for k in range(len(indices)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans