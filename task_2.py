def fib(n):
    n1,n2= 0,1                                                           
    result,total = 0,0                                                           
    while total < n: 
        total = n1+ n2
        n1= n2
        n2= total 
        if n2 % 2 == 0: 
            result += n2
    return result


fib(4000000)