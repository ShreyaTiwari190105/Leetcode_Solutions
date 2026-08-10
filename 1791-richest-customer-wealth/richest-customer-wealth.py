class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for customer in accounts:
            customer_sum = 0

            for money in customer:
                customer_sum = customer_sum + money

            max_wealth = max(max_wealth, customer_sum)

        return max_wealth