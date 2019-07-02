import math

j = 1j

def model_c(w,C):
    Z = 1.0/(j*w*C)
    return Z

#
# Model the reactance of an RC parallel circuit.
#
def model_r_c_p(w, R, C):
    # Z2 is the straight parallel equation that python can handle
    Z2 = (1.0)/((1.0/R)+(1.0)/((1.0)/(j*w*C)))
    # Z is the equation easier to implement in C (just rearranged)
    # i.e. it has a real divisor
    Z = ((1.0/R)-j*w*C)/((1.0/R)**2 + (w*C)**2)
    #return Z2,Z for comparison return both and check they give the same results
    return Z#, Z2

# return magnitude of RC in parallel
# from https://www.translatorscafe.com/unit-converter/EN/calculator/parallel-rc-impedance/
#
def model_k(w, R, C):
    Z = 1.0/(math.sqrt((1.0/R)**2 + (w*C)**2))
    return Z

R = 220
C = 10E-6

for f in range (1,3000000, 20):
    print f
    w = 2 * 3.142 * f
    Z = model_r_c_p (w,R,C)
    #Z = model_c(w,C)
    #Z = model_k(w,R,C)
    #print "at freq", f, Z#, abs(Z)
    print "at freq", f, Z, abs(Z)
    #print Z


