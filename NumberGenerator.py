
def run_generator():
    M = 132
    k=3 
    while True:
        try:
            x0=int(input("Give the seed number: "))
            if check_x0(x0):
                break
        except ValueError:
            print("The seed number must be a prime number")
    returnx0(x0)
    algorithm_for_numbers(M,k,x0)
    return algorithm_for_numbers(M, k, x0)

    
def returnx0(x0):
    return x0

def check_x0(n):
    if n<1:
        print("The seed number must be a prime number")
        return False
    if n==1:
        print("The seed number cannot be 1")
        return False
    else:
        for i in range(2,n):
            if n % i ==0:
                print("The seed number must be a prime number")
                return False
    return True
            
def algorithm_for_numbers(M,k,x0):
    x00=x0
    numbers=[]
    for i in range(32):
        xn=(k*x0) % M
        numbers.append(xn)
        x0=xn
    Unumbers=[round(x/M,2) for x in numbers]
    return numbers , Unumbers, x00 



