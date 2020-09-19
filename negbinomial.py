import math

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

def C(k,n):
    return factorial(n)/factorial(k)/factorial(n-k)

def prob(n,p,r):
    return C(r-1,n-1) * (p ** r) * ((1-p) ** (n-r)) 

def infoMeasure(n,p,r):
    return -math.log(prob(n,p,r),2)

def sumProb(N,p,r):
    """nguồn sinh ra các symbol(tương ứng với các giá trị của i)độc lập
    với nhau, các symbol tạo thành một tập mẫu X nên tổng prob(n,p,i) với 
    i từ r đến N khi N -> infinity là xác suất của không gian mẫu X và bằng 1"""
    sum = 0.0
    for n in range(r,N+1):
        sum += prob(n,p,r)

    return sum

def approxEntropy(N,p,r):
    """Entropy của nguồn negative binomial tính bằng công thức :
    H(X_{negbin}) = \sum_{x \in X_{negbin}} p(x)*I(x) 
    với X_{negbin} = {r,r+1,r+2,...\infty}
    p(x) = p{x} = prob(x,p,r)
    I(x) = -log_2(p(x)) =  infoMeasure(x,p,r)
    nên giá trị trung bình của lượng tin của các symbol từ r đến N
    I_{tb} = \sum_{x = 1}^{N}(prob(x,p,r)*infoMeasure(x,p,r))
    sẽ xấp xỉ giá trị entropy của nguồn negative binomial khi n đủ lớn  
    Khi n = 1/2 thì entropy của nguồn negative binomial :"""
    
    sum = 0.0
    for x in range(r,N+1):
        sum += prob(x,p,r) * infoMeasure(x,p,r)

    return sum

print(sumProb(100,0.2,2))
print(approxEntropy(10,0.2,2))

