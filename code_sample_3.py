class Solution:
    @lru_cache
    def fib(self, n: int) -> int:
        return self.fib(n-1)+self.fib(n-2) if n>1 else n

