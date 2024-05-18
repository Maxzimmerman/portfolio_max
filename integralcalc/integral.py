import sympy
from sympy import Add, symbols, solve, Eq, integrate, Mul


def normal(function: Add, limit=None) -> int:
    integral = integrate(function)
    x = symbols('x')
    area = 0
    if limit is None:
        zero_points = sorted(solve(Eq(function, 0)))
        for i in range(0, len(zero_points) - 1):
            area += (integral.subs(x, zero_points[i + 1]) - integral.subs(x, zero_points[i]))
            return area
    else:
        for i in range(0, len(limit) - 1):
            area += (integral.subs(x, limit[i + 1]) - integral.subs(x, limit[i]))
            return area


def between(function_one: Add, function_two: Add) -> int:
    x = symbols('x')
    differential = function_one - function_two
    zero_points = sorted(solve(Eq(differential, 0)))
    integral = integrate(differential)
    area = 0
    for i in range(0, len(zero_points) - 1):
        area += integral.subs(x, zero_points[i + 1]) - (integral.subs(x, zero_points[i]))
    return area


def with_one_interval_border(function: Add, first_limit: float, area: float) -> list:
    b, x = symbols('b x')
    integral = integrate(function)
    r = [x for x in solve(Eq(integral.subs(x, b) - (integral.subs(x, first_limit)), area)) if x.is_real]
    return r


def calc_c(function: Add, point: dict) -> Mul:
    c, x = symbols('c x')
    integral = integrate(function) + c
    result = solve(Eq(integral.subs(x, next(iter(point))), point[next(iter(point))]))
    return result
