import sympy
from sympy import symbols
from sympy.solvers import solve
x1=symbols('x1')

eq=x1**2 - 4
print("x1= ",solve(eq,x1))

## Limits approaching, from right or left

x2=2
h=0.0001
y_right=(3*(x2+h)**2)/((x2+h)**2-4)
y_left=(3*(x2-h)**2)/((x2-h)**2-4)
print("y_right: ",y_right)
print("y_left: ",y_left)

if round(y_right)!=round(y_left):
    print("Limit does not exist at x2=",x2)