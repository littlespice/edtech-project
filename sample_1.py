def fib(n) :
    # Input datatype checking
    if isinstance(n, int):
        if n <= 0:
            return 0
            
        # Iteratively add fibonacci nums
        fibo = (0 + 1) * [0]
        fibo[1]=1 
        s = fibo[1] + fibo[0]
        for i in range(2,n+1) :
            fibo[i] = fibo[i-2] + fibo[i-1]
            s += fibo[i]
        return s

