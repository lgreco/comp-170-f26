# Data entry block
print("This program solves quadratic equations of the form ax^2 + bx + c = 0")
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Many programming languages have a built-in square root function,
# but Python does not. However, Python does have a built-in library
# called math that contains a square root function. Many languages
# have such libraries extending their built-in functionalities.
#
# To use the square root function in Python, we must first import
# the math library. The following line of code imports the math
# library and makes the square root function available to our program.
from math import sqrt

# Logic and output block
if a == 0:
    # If a is 0 then the equation could be linear;
    # This can be verified by checking if b = 0;
    if b == 0:
        # If b is also 0, then the equation is invalid.
        # It's ok to shake-our-head at the user!
        print("SMH... The equation is invalid.")
    else:
        # If b is not 0, then the equation is linear and can
        # be solved for x = -c/b
        print("Solution x =", -c / b)
else:
    # When a not zero, we have a quadratic equation. To determine if
    # we can solve it with real numbers we need first co computer and
    # evaluate its discriminant.
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        print("No real solutions exist.")
    else:
        # If the discriminant is non-negative, we can solve for the two
        # solutions using the quadratic formula.
        print("Solution x1 =", (-b - sqrt(discriminant)) / (2 * a))
        print("Solution x2 =", (-b + sqrt(discriminant)) / (2 * a))
