from math import sqrt

def solve_quadratic(a:float, b:float, c:float) -> tuple:
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    
    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term
    
    Returns:
    tuple: A tuple containing the solutions. If there are no real solutions, returns an empty tuple.
           If there is one real solution, returns a tuple with one element.
           If there are two real solutions, returns a tuple with two elements.
    """

    # Initialize the solutions tuple to be empty. 
    # This will be returned if there are no real solutions or
    # if the equation is undefined.
    solutions: tuple = ()

    # Go down the decision tree to determine if the equation is linear or 
    # quadratic, and if it has real solutions.
    if a == 0:
        # Equation may be linear.
        if b != 0:
            # Equation is definitely linear and has one solution.
            solutions = (-c / b,)
    else:
        # Equation is definitely quadratic. Compute the discriminant
        # to determine if there are real solutions.
        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            # Real solutions exist. Compute the two solutions using the 
            # quadratic formula and assign them to the solutions tuple.
            root1 = (-b - sqrt(discriminant)) / (2 * a)
            root2 = (-b + sqrt(discriminant)) / (2 * a)
            solutions = (root1, root2) 
    # Done
    return solutions