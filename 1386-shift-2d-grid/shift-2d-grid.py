class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        # Flatten grid
        arr = []
        for row in grid:
            arr.extend(row)

        # Effective shifts
        k = k % (m * n)

        # Rotate right
        arr = arr[-k:] + arr[:-k] if k else arr

        # Convert back to 2D
        ans = []
        idx = 0

        for i in range(m):
            ans.append(arr[idx:idx+n])
            idx += n

        return ans