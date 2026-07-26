from collections import deque
from sortedcontainers import SortedSet

class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cnt0 = s.count('0')

        # Unvisited states (number of zeros), separated by parity
        states = [SortedSet(), SortedSet()]
        for i in range(n + 1):
            states[i % 2].add(i)

        states[cnt0 % 2].remove(cnt0)

        q = deque([cnt0])
        ans = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == 0:
                    return ans

                # Reachable range of zero-counts after one operation
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)

                st = states[l % 2]
                idx = st.bisect_left(l)

                while idx < len(st) and st[idx] <= r:
                    nxt = st[idx]
                    q.append(nxt)
                    st.remove(nxt)

            ans += 1

        return -1