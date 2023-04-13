T = int(input())

for i in range(T):
    
    n, k = map(int, input().split())
    
    print((n // k) + (n % k))