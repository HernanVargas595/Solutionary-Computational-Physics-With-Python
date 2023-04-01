def root_bisection(f, a, b, tolerance=1.0e-6):
    """
    Uses the bisection method to find a value x between a and b
    for which f(x)=0 , to with in the tolerance given .
    Default tolerance is 1.0e-6, if no tolerenace is specified in
    the function call.
    """

    dx = abs(b-a)  #Inital value of dx

    ##Bisection method
    while dx>tolerance:
        x=(a+b)*0.5
        if(f(a)*f(x)<0):
            b=x
        else:
            a=x
        dx=abs(b-a)

        return x