import math

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

def C(k,n):
    return factorial(n)/factorial(k)/factorial(n-k)

def prob(n,p,k):
    return C(k,n)*(p ** k) * ((1-p) ** (n-k)) 


def infoMeasure(n,p,k):
    return -math.log(prob(n,p,k),2)

def sumProb(N,p):
    """nguồn sinh ra các symbol(tương ứng với các giá trị của i)độc lập
     với nhau, các symbol tạo thành một tập mẫu X nên tổng prob(n,p,i) với
      i từ 0 đến N là xác suất của không gian mẫu X và bằng 1"""
    s = 0.0
    for i in range(0,N+1):
        s += prob(N,p,i)

    return s

def approxEntropy(N,p):
    """Entropy của nguồn binomial tính bằng công thức :
    H(X_{bin}) = \sum_{x \in X_{bin}} p(x)*I(x) 
    với X_{bin} = {0,1,2,...N}
    p(x) = prob(N,p,x)
    I(x) = -log_2(p(x)) =  infoMeasure(N,p,x)
    nên giá trị trung bình của lượng tin của các symbol từ 1 đến N
    I_{tb} = \sum\limits_{x = 1}^{N}(prob(x,p)*infoMeasure(x,p)) và cũng bằng 
    entropy của nguồn binomial
    Khi p = 1/2 thì entropy của nguồn binomial:
    H(X_{bin}) = -\sum\limits_{x =0}^{N}C_{N}^{x} * 0.5 ^ N * log_2(C_{N}^{x} * 0.5 ^ N)
    """
    s = 0
    for i in range(0,N+1):
        s += infoMeasure(N,p,i) * prob(N,p,i)

    return s


print(sumProb(10,0.8))
print(approxEntropy(10,0.5))
