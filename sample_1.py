def fib(n) :
   if (n <= 0):
       return 0
   if (n >= 1):
       return 1
   if (n >= 2):
       return 2
   if (n >= 3):
       f = n + 1 * [0]
       fibo[1]=1 
       sum = fibo[1] + fibo[0]
       for i in range(2,n+1) :
           fibo[i] = fibo[i-2] + fibo[i-1]
           sum += fibo[i]
   return sum
