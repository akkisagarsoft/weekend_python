import cmath
def squareRoot(num):
    sqrt_of_num = num ** 0.5
    return sqrt_of_num

# for real and complex numbers using cmath
def sqaureRootComplex(num):
    sqrt_of_compl = cmath.sqrt(num)
    return sqrt_of_compl

if __name__ == '__main__':
    
    squareroot = squareRoot(9)
    print(squareroot)
    # complex number
    num = 1 +2j
    complex_no_root = sqaureRootComplex(num)
    print("sqaure root of {0} is {1:0.3f}+{2:0.3f}j".format(num,complex_no_root.real,complex_no_root.imag))