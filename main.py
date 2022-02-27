class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        account_sums = []
        for account in accounts:
            account_sums.append(sum(account))

        account_sums.sort()
        result = account_sums[-1]
        return result
