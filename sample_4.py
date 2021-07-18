class Solution:
    def fib(self, N: int) -> int:
        # iterative O(n) time O(1) space
        if N in [0, 1]:
            return N
        
        first = 0
        second = 1
        result = 0
        for n in range(2, N + 1):
            result = first + second
            second = first
            first = result
        return first + second
