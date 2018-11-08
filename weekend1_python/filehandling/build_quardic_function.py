# currying
def build_quardic_function_exam(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = build_quardic_function_exam(4,5,6)

print(f(0))
print(f(1))
print(build_quardic_function_exam(4,5,6)(0))