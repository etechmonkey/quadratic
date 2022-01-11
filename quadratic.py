import math

def solve_quadratic(a,b,c):
    try:
        x_pos = (-b+ math.sqrt(b**2-4*a*c))/(2*a)
        x_neg = (-b- math.sqrt(b**2-4*a*c))/(2*a)
        if(x_pos != x_neg):
            return tuple([x_pos, x_neg])
        else:
            return x_pos
    except (IndexError, ValueError):
        return None