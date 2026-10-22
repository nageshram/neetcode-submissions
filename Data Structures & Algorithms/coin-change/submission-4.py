class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        hashmap={}
        def backtracking(remaining):

            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')

            if remaining in hashmap:
                return hashmap[remaining]
            
            mini = float('inf')
            for coin in coins:
                res = backtracking(remaining - coin)

                if res != float('inf'):
                    mini = min(mini, res+1)
            
            hashmap[remaining]= mini
            return mini
        
        res = backtracking(amount)

        if res == float('inf'):
            return -1

        return res
