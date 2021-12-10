# Fibonacci Series : 0 1 1 2 3 5 8 13 21

# Recursive Approach
# def fibo(n):
#     if n==1:
#         return 0
#     elif n==2:
        # return 1
    # return fibo(n-1) + fibo(n-2)
# print(fibo(5))

# Iterative Approach
# def fibo(n):
#     a,b = 0, 1
#     for i in range(3, n+1):
#         a,b = b,a+b
#     return b
# print(fibo(5))