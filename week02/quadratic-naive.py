from math import sqrt 

#Problem solving strategy for the quadratic equation ax^2 + bx + c = 0

a = 0 
b = 10
c = 4 
#
#If a is 0 then the equation is linear;

if a == 0: 

#  In this case, check if b = 0; if not solve for x = -b/c

    if b == 0:

        print("SMH")

    else:

        print(-c/b)
#                                else, SMH
#If a is not 0 then compute the discriminant, delta = b*b - 4*a*c

else:

    delta = b*b-4*a*c

#If delta is negative, report no real solutions exist

    if delta < 0:
        print("No real solutions")

#  else solve for (-b +- sqrt(delta)) /(2*a)

    else:
        print((-b-sqrt(delta))/(2*a))
        print((-b+sqrt(delta))/(2*a))

