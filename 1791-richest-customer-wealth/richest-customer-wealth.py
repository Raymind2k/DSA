class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth=0
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[i])):
                total+=accounts[i][j]
            max_wealth=max(max_wealth,total)
        return max_wealth           