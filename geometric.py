import math
def prob(n,p):
    return p* ((1-p) ** (n-1))

def infoMeasure(n,p):
    return -math.log(prob(n,p),2)

def sumProb(N,p):
    """nguồn sinh ra các symbol(tương ứng với các giá trị của i)độc lập
    với nhau, các symbol tạo thành một tập mẫu X nên tổng prob(n,p,i) với 
    i từ 1 đến N khi N -> infinity là xác suất của không gian mẫu X và bằng 1"""
    sum = 0
    
    for n in range(1,N+1):
        sum += prob(n,p)
    return sum

def approxEntropy(N,p):
    """Entropy của nguồn geometric tính bằng công thức :
    H(X_{geom}) = \sum_{x \in X_{geom}} p(x)*I(x) 
    với X_{geom} = {1,2,3,...\infty}
    p(x) = p{x} = prob(x,p)
    I(x) = -log_2(p(x)) =  infoMeasure(x,p)
    nên giá trị trung bình của lượng tin của các symbol từ 1 đến N
    I_{tb} = \sum_{x = 1}^{N}(prob(x,p)*infoMeasure(x,p))
    sẽ xấp xỉ giá trị entropy của nguồn geometric khi n đủ lớn  
    Khi n = 1/2 thì entropy của nguồn geometric :
    H(X_{geom}) = \sum_{x = 1}^{\infty}(x/2^x) = 2"""
    sum = 0.0
    for x in range(1,N+1):
        sum += infoMeasure(x,p) * prob(x,p)
    #now s is expected value 
    return sum

N = 10
p = 0.9
print(sumProb(N,p))
print(approxEntropy(N,p))
