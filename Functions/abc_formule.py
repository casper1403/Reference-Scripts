import cmath

print('Solve the quadratic equation: ax**2 + bx + c = 0')


"""Functions to solve the Quadratic formula """

def abc_formule(a,b,c):
    delta = (b**2) - (4*a*c)
    solution1 = (-b-cmath.sqrt(delta))/(2*a)
    solution2 = (-b+cmath.sqrt(delta))/(2*a)
    print('The solutions are {0} and {1}'.format(solution1,solution2))
    return [solution1, solution2

abc_formule(a,b,c)
