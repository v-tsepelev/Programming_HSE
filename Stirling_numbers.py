# Calculate Stirling numbers of the second kind.

s = input().split()
n = int(s[0])
k = int(s[1])

def factorial(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f

def binomial(n,k):
    return (factorial(n))/(factorial(k)*factorial(n-k))

def Stirling_number(n,k):
    if k == 0 and n != 0:
        return 0
    else:
        result = 1
        for j in range(1,k+1):
            result += ((-1)**(k-j))*binomial(k,j)*(j**n)
        result = (1/factorial(k))*result
    return int(result)

print(Stirling_number(n,k))
