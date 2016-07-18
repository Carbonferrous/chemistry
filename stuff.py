from math import factorial
def ncr(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
c = [-1]
for i in  range(1, 10):
    c.append(2**(i*(i-1)//2) - sum(k*ncr(i,k)*2**((i-k)*(i-k-1)//2)*c[k] for k in range(1, i))//2)
print(c)
