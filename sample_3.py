class Solution:
    def fib(self, n: int) -> int:
        if isinstance(n, int):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                return self.fib(n-1)+self.fib(n-2) if n>1 else n
        else:
            print('Input n should be of Integer type')