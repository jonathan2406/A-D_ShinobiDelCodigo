#punto 1

def factorial(n):
    memo = [None] * (n + 1)
    
    memo[0] = 1
    
  
    for i in range(1, n + 1):
        memo[i] = i * memo[i - 1]
    return memo[n]


n = 8
print("Factorial de", n, "es", factorial(n))