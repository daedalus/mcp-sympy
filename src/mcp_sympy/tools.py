"""MCP tools that expose SymPy's symbolic mathematics functionality."""

import fastmcp
import sympy
from sympy import (
    Abs,
    Add,
    And,
    Circle,
    Complement,
    Derivative,
    EmptySet,
    Eq,
    FiniteSet,
    Float,
    Ge,
    Gt,
    Implies,
    Integer,
    Integral,
    Intersection,
    Interval,
    Le,
    Line,
    Lt,
    Matrix,
    Mul,
    Nand,
    Ne,
    Nor,
    Not,
    Or,
    Piecewise,
    Point,
    Point3D,
    Polygon,
    Pow,
    Product,
    Range,
    Rational,
    Sum,
    Symbol,
    Triangle,
    Union,
    UniversalSet,
    Wild,
    WildFunction,
    Xor,
    acos,
    asin,
    atan,
    binomial,
    catalan,
    ceiling,
    cos,
    cosh,
    diag,
    diff,
    diophantine,
    dirichlet_eta,
    divisors,
    dsolve,
    erf,
    exp,
    expand,
    expand_complex,
    expand_log,
    expand_trig,
    eye,
    factor,
    factorial,
    fibonacci,
    floor,
    fresnelc,
    fresnels,
    gamma,
    integrate,
    isprime,
    latex,
    limit,
    log,
    lucas,
    nextprime,
    nsolve,
    ones,
    perfect_power,
    polylog,
    powsimp,
    prevprime,
    prime,
    product,
    randMatrix,
    ratsimp,
    root,
    satisfiable,
    series,
    simplify,
    sin,
    sinh,
    solve,
    solveset,
    sqrt,
    summation,
    symbols,
    tan,
    tanh,
    totient,
    trigsimp,
    zeros,
    zeta,
)


def _sympify(expr: str) -> sympy.Basic:
    """Convert string expression to SymPy object."""
    return sympy.sympify(expr)


mcp = fastmcp.FastMCP("mcp-sympy")


@mcp.tool()
def sympy_symbols(names: str) -> str:
    """Create symbolic variables.

    Args:
        names: Comma-separated symbol names (e.g., "x, y, z")

    Returns:
        String representation of created symbols
    """
    result = sympy.symbols(names)
    if isinstance(result, tuple):
        return ", ".join(str(s) for s in result)
    return str(result)


@mcp.tool()
def sympy_symbol(name: str) -> str:
    """Create a single symbolic variable.

    Args:
        name: Symbol name

    Returns:
        String representation of the symbol
    """
    return str(Symbol(name))


@mcp.tool()
def sympy_sympify(expr: str) -> str:
    """Convert a string to a SymPy expression.

    Args:
        expr: String expression to convert

    Returns:
        SymPy expression as string
    """
    return str(sympy.sympify(expr))


@mcp.tool()
def sympy_simplify(expr: str) -> str:
    """Simplify an expression.

    Args:
        expr: String expression to simplify

    Returns:
        Simplified expression as string
    """
    return str(simplify(_sympify(expr)))


@mcp.tool()
def sympy_trigsimp(expr: str) -> str:
    """Simplify trigonometric expressions.

    Args:
        expr: String trigonometric expression

    Returns:
        Simplified expression
    """
    return str(trigsimp(_sympify(expr)))


@mcp.tool()
def sympy_ratsimp(expr: str) -> str:
    """Simplify rational expressions.

    Args:
        expr: String rational expression

    Returns:
        Simplified rational expression
    """
    return str(ratsimp(_sympify(expr)))


@mcp.tool()
def sympy_powsimp(expr: str) -> str:
    """Simplify powers in an expression.

    Args:
        expr: String expression with powers

    Returns:
        Simplified expression
    """
    return str(powsimp(_sympify(expr)))


@mcp.tool()
def sympy_factor(expr: str) -> str:
    """Factor an expression.

    Args:
        expr: String expression to factor

    Returns:
        Factored expression
    """
    return str(factor(_sympify(expr)))


@mcp.tool()
def sympy_expand(expr: str) -> str:
    """Expand an expression.

    Args:
        expr: String expression to expand

    Returns:
        Expanded expression
    """
    return str(expand(_sympify(expr)))


@mcp.tool()
def sympy_expand_trig(expr: str) -> str:
    """Expand trigonometric expressions."""
    return str(expand_trig(_sympify(expr)))


@mcp.tool()
def sympy_expand_log(expr: str) -> str:
    """Expand logarithmic expressions."""
    return str(expand_log(_sympify(expr)))


@mcp.tool()
def sympy_together(expr: str) -> str:
    """Combine terms into a single fraction."""
    return str(sympy.together(_sympify(expr)))


@mcp.tool()
def sympy_apart(expr: str) -> str:
    """Perform partial fraction decomposition."""
    return str(sympy.apart(_sympify(expr)))


@mcp.tool()
def sympy_cancel(expr: str) -> str:
    """Cancel common factors in rational expression."""
    return str(sympy.cancel(_sympify(expr)))


@mcp.tool()
def sympy_solve(equation: str, variables: str = "") -> str:
    """Solve an equation or system of equations.

    Args:
        equation: String equation
        variables: Comma-separated variables to solve for

    Returns:
        Solution(s) as string
    """
    eq = _sympify(equation)
    if variables:
        vars_list = [sympy.Symbol(v.strip()) for v in variables.split(",")]
        return str(solve(eq, *vars_list))
    return str(solve(eq))


@mcp.tool()
def sympy_solveset(equation: str, variable: str = "") -> str:
    """Solve an equation using solveset.

    Args:
        equation: String equation
        variable: Variable to solve for

    Returns:
        Solution set as string
    """
    var = sympy.Symbol(variable) if variable else sympy.Symbol("x")
    eq = _sympify(equation)
    return str(solveset(eq, var))


@mcp.tool()
def sympy_nsolve(equation: str, variables: str, guesses: str) -> str:
    """Numerically solve an equation.

    Args:
        equation: String equation
        variables: Comma-separated variables
        guesses: Comma-separated initial guesses

    Returns:
        Numerical solution
    """
    vars_list = [sympy.Symbol(v.strip()) for v in variables.split(",")]
    guesses_list = [float(g.strip()) for g in guesses.split(",")]
    eq = _sympify(equation)
    return str(nsolve(eq, vars_list, guesses_list))


@mcp.tool()
def sympy_diff(expr: str, variable: str = "x", order: int = 1) -> str:
    """Differentiate an expression.

    Args:
        expr: String expression to differentiate
        variable: Variable to differentiate with respect to
        order: Order of derivative

    Returns:
        Derivative as string
    """
    var = sympy.Symbol(variable)
    result = diff(_sympify(expr), var, order)
    return str(result)


@mcp.tool()
def sympy_integrate(expr: str, variable: str = "x") -> str:
    """Integrate an expression.

    Args:
        expr: String expression to integrate
        variable: Variable to integrate with respect to

    Returns:
        Integral as string
    """
    var = sympy.Symbol(variable)
    result = integrate(_sympify(expr), var)
    return str(result)


@mcp.tool()
def sympy_limit(expr: str, variable: str, point: str, direction: str = "+") -> str:
    """Compute a limit.

    Args:
        expr: String expression
        variable: Variable approaching the limit
        point: Point to approach
        direction: Direction ("+", "-")

    Returns:
        Limit as string
    """
    var = sympy.Symbol(variable)
    pt = _sympify(point)
    result = limit(_sympify(expr), var, pt, direction)
    return str(result)


@mcp.tool()
def sympy_series(
    expr: str, variable: str = "x", point: str = "0", order: int = 6
) -> str:
    """Compute series expansion.

    Args:
        expr: String expression
        variable: Variable to expand around
        point: Point to expand around
        order: Order of expansion

    Returns:
        Series expansion as string
    """
    var = sympy.Symbol(variable)
    pt = _sympify(point)
    result = series(_sympify(expr), var, pt, order)
    return str(result)


@mcp.tool()
def sympy_sum(expr: str, variable: str, lower: str, upper: str) -> str:
    """Compute a sum.

    Args:
        expr: String expression to sum
        variable: Summation variable
        lower: Lower bound
        upper: Upper bound

    Returns:
        Sum as string
    """
    var = sympy.Symbol(variable)
    result = summation(_sympify(expr), (var, _sympify(lower), _sympify(upper)))
    return str(result)


@mcp.tool()
def sympy_product(expr: str, variable: str, lower: str, upper: str) -> str:
    """Compute a product.

    Args:
        expr: String expression to multiply
        variable: Product variable
        lower: Lower bound
        upper: Upper bound

    Returns:
        Product as string
    """
    var = sympy.Symbol(variable)
    result = product(_sympify(expr), (var, _sympify(lower), _sympify(upper)))
    return str(result)


@mcp.tool()
def sympy_summation(expr: str, variable: str, bounds: str) -> str:
    """Compute an unevaluated sum (Sum object)."""
    var = sympy.Symbol(variable)
    lower, upper = bounds.split(",")
    result = Sum(
        _sympify(expr), (var, _sympify(lower.strip()), _sympify(upper.strip()))
    )
    return str(result)


@mcp.tool()
def sympy_product_expr(expr: str, variable: str, bounds: str) -> str:
    """Compute an unevaluated product (Product object)."""
    var = sympy.Symbol(variable)
    lower, upper = bounds.split(",")
    result = Product(
        _sympify(expr), (var, _sympify(lower.strip()), _sympify(upper.strip()))
    )
    return str(result)


@mcp.tool()
def sympy_derivative(expr: str, variable: str, order: int = 1) -> str:
    """Create a Derivative object (unevaluated)."""
    var = sympy.Symbol(variable)
    result = Derivative(_sympify(expr), var, order)
    return str(result)


@mcp.tool()
def sympy_integral(expr: str, variable: str) -> str:
    """Create an Integral object (unevaluated)."""
    var = sympy.Symbol(variable)
    result = Integral(_sympify(expr), var)
    return str(result)


@mcp.tool()
def sympy_matrix(rows: str) -> str:
    """Create a matrix from rows (e.g., "1,2; 3,4")."""
    row_list = [r.split(",") for r in rows.split(";")]
    matrix_data = [[int(x.strip()) for x in row] for row in row_list]
    return str(Matrix(matrix_data))


@mcp.tool()
def sympy_matrix_add(matrix1: str, matrix2: str) -> str:
    """Add two matrices."""
    m1 = _sympify(matrix1)
    m2 = _sympify(matrix2)
    return str(m1 + m2)


@mcp.tool()
def sympy_matrix_multiply(matrix1: str, matrix2: str) -> str:
    """Multiply two matrices."""
    m1 = _sympify(matrix1)
    m2 = _sympify(matrix2)
    return str(m1 * m2)


@mcp.tool()
def sympy_matrix_inverse(matrix: str) -> str:
    """Compute matrix inverse."""
    m = _sympify(matrix)
    return str(m.inv())


@mcp.tool()
def sympy_matrix_determinant(matrix: str) -> str:
    """Compute matrix determinant."""
    m = _sympify(matrix)
    return str(m.det())


@mcp.tool()
def sympy_matrix_transpose(matrix: str) -> str:
    """Transpose a matrix."""
    m = _sympify(matrix)
    return str(m.T)


@mcp.tool()
def sympy_matrix_eigenvals(matrix: str) -> str:
    """Compute eigenvalues of a matrix."""
    m = _sympify(matrix)
    return str(m.eigenvals())


@mcp.tool()
def sympy_matrix_eigenvects(matrix: str) -> str:
    """Compute eigenvectors of a matrix."""
    m = _sympify(matrix)
    return str(m.eigenvects())


@mcp.tool()
def sympy_eye(n: int) -> str:
    """Create an identity matrix."""
    return str(eye(n))


@mcp.tool()
def sympy_zeros(rows: int, cols: int = 0) -> str:
    """Create a zero matrix."""
    if cols == 0:
        cols = rows
    return str(zeros(rows, cols))


@mcp.tool()
def sympy_ones(rows: int, cols: int = 0) -> str:
    """Create a matrix of ones."""
    if cols == 0:
        cols = rows
    return str(ones(rows, cols))


@mcp.tool()
def sympy_diag(elements: str) -> str:
    """Create a diagonal matrix (comma-separated)."""
    elems = [_sympify(e) for e in elements.split(",")]
    return str(diag(*elems))


@mcp.tool()
def sympy_latex(expr: str) -> str:
    """Convert expression to LaTeX."""
    return str(latex(_sympify(expr)))


@mcp.tool()
def sympy_python_code(expr: str) -> str:
    """Convert expression to Python code."""
    return str(sympy.python(_sympify(expr)))


@mcp.tool()
def sympy_mathml(expr: str) -> str:
    """Convert expression to MathML."""
    return str(sympy.mathml(_sympify(expr)))


@mcp.tool()
def sympy_str(expr: str) -> str:
    """Convert expression to string."""
    return str(_sympify(expr))


@mcp.tool()
def sympy_repr_expr(expr: str) -> str:
    """Get repr of expression."""
    return repr(_sympify(expr))


@mcp.tool()
def sympy_interval(
    start: str, end: str, left_open: bool = False, right_open: bool = False
) -> str:
    """Create an interval."""
    result = Interval(_sympify(start), _sympify(end), left_open, right_open)
    return str(result)


@mcp.tool()
def sympy_finite_set(elements: str) -> str:
    """Create a finite set (comma-separated)."""
    elems = [_sympify(e) for e in elements.split(",")]
    return str(FiniteSet(*elems))


@mcp.tool()
def sympy_union(set1: str, set2: str) -> str:
    """Compute union of two sets."""
    s1 = _sympify(set1)
    s2 = _sympify(set2)
    return str(Union(s1, s2))


@mcp.tool()
def sympy_intersection(set1: str, set2: str) -> str:
    """Compute intersection of two sets."""
    s1 = _sympify(set1)
    s2 = _sympify(set2)
    return str(Intersection(s1, s2))


@mcp.tool()
def sympy_complement(set1: str, set2: str) -> str:
    """Compute complement of set1 in set2."""
    s1 = _sympify(set1)
    s2 = _sympify(set2)
    return str(Complement(s1, s2))


@mcp.tool()
def sympy_evaluate(flag: bool = True) -> str:
    """Toggle evaluation globally."""
    sympy.Basic.__eval__ = flag if flag else None
    return f"Evaluation {'enabled' if flag else 'disabled'}"


@mcp.tool()
def sympy_n(expr: str, n: int = 15) -> str:
    """Evaluate expression numerically."""
    return str(_sympify(expr).n(n))


@mcp.tool()
def sympy_evalf(expr: str, n: int = 15) -> str:
    """Evaluate expression to floating point."""
    return str(_sympify(expr).evalf(n))


@mcp.tool()
def sympy_exp(expr: str) -> str:
    """Exponential function."""
    return str(exp(_sympify(expr)))


@mcp.tool()
def sympy_log(expr: str) -> str:
    """Natural logarithm."""
    return str(log(_sympify(expr)))


@mcp.tool()
def sympy_log_base(expr: str, base: str) -> str:
    """Logarithm with specified base."""
    return str(log(_sympify(expr), _sympify(base)))


@mcp.tool()
def sympy_sin(expr: str) -> str:
    """Sine function."""
    return str(sin(_sympify(expr)))


@mcp.tool()
def sympy_cos(expr: str) -> str:
    """Cosine function."""
    return str(cos(_sympify(expr)))


@mcp.tool()
def sympy_tan(expr: str) -> str:
    """Tangent function."""
    return str(tan(_sympify(expr)))


@mcp.tool()
def sympy_sinh(expr: str) -> str:
    """Hyperbolic sine."""
    return str(sinh(_sympify(expr)))


@mcp.tool()
def sympy_cosh(expr: str) -> str:
    """Hyperbolic cosine."""
    return str(cosh(_sympify(expr)))


@mcp.tool()
def sympy_tanh(expr: str) -> str:
    """Hyperbolic tangent."""
    return str(tanh(_sympify(expr)))


@mcp.tool()
def sympy_asin(expr: str) -> str:
    """Arc sine."""
    return str(asin(_sympify(expr)))


@mcp.tool()
def sympy_acos(expr: str) -> str:
    """Arc cosine."""
    return str(acos(_sympify(expr)))


@mcp.tool()
def sympy_atan(expr: str) -> str:
    """Arc tangent."""
    return str(atan(_sympify(expr)))


@mcp.tool()
def sympy_sqrt(expr: str) -> str:
    """Square root."""
    return str(sqrt(_sympify(expr)))


@mcp.tool()
def sympy_cbrt(expr: str) -> str:
    """Cube root."""
    return str(sympy.cbrt(_sympify(expr)))


@mcp.tool()
def sympy_root(expr: str, n: int = 2) -> str:
    """N-th root."""
    return str(root(_sympify(expr), n))


@mcp.tool()
def sympy_floor(expr: str) -> str:
    """Floor function."""
    return str(floor(_sympify(expr)))


@mcp.tool()
def sympy_ceiling(expr: str) -> str:
    """Ceiling function."""
    return str(ceiling(_sympify(expr)))


@mcp.tool()
def sympy_abs(expr: str) -> str:
    """Absolute value."""
    return str(Abs(_sympify(expr)))


@mcp.tool()
def sympy_factorial(n: str) -> str:
    """Factorial."""
    return str(factorial(int(n)))


@mcp.tool()
def sympy_binomial(n: str, k: str) -> str:
    """Binomial coefficient."""
    return str(binomial(int(n), int(k)))


@mcp.tool()
def sympy_gamma(expr: str) -> str:
    """Gamma function."""
    return str(gamma(_sympify(expr)))


@mcp.tool()
def sympy_zeta(s: str) -> str:
    """Riemann zeta function."""
    return str(zeta(_sympify(s)))


@mcp.tool()
def sympy_erf(expr: str) -> str:
    """Error function."""
    return str(erf(_sympify(expr)))


@mcp.tool()
def sympy_dirichlet_eta(s: str) -> str:
    """Dirichlet eta function."""
    return str(dirichlet_eta(_sympify(s)))


@mcp.tool()
def sympy_polylog(s: str, z: str) -> str:
    """Polylogarithm."""
    return str(polylog(_sympify(s), _sympify(z)))


@mcp.tool()
def sympy_fibonacci(n: str) -> str:
    """Fibonacci number."""
    return str(fibonacci(int(n)))


@mcp.tool()
def sympy_lucas(n: str) -> str:
    """Lucas number."""
    return str(lucas(int(n)))


@mcp.tool()
def sympy_catalan(n: str) -> str:
    """Catalan number."""
    return str(catalan(int(n)))


@mcp.tool()
def sympy_isprime(n: str) -> str:
    """Check if n is prime."""
    return str(isprime(int(n)))


@mcp.tool()
def sympy_prime(n: str) -> str:
    """Return the n-th prime."""
    return str(prime(int(n)))


@mcp.tool()
def sympy_nextprime(n: str) -> str:
    """Return the next prime after n."""
    return str(nextprime(int(n)))


@mcp.tool()
def sympy_prevprime(n: str) -> str:
    """Return the previous prime before n."""
    return str(prevprime(int(n)))


@mcp.tool()
def sympy_totient(n: str) -> str:
    """Euler's totient function."""
    return str(totient(int(n)))


@mcp.tool()
def sympy_divisors(n: str) -> str:
    """Return divisors of n."""
    return str(divisors(int(n)))


@mcp.tool()
def sympy_gcd(a: str, b: str) -> str:
    """Greatest common divisor."""
    return str(sympy.gcd(int(a), int(b)))


@mcp.tool()
def sympy_lcm(a: str, b: str) -> str:
    """Least common multiple."""
    return str(sympy.lcm(int(a), int(b)))


@mcp.tool()
def sympy_factorint(n: str) -> str:
    """Integer factorization."""
    return str(sympy.factorint(int(n)))


@mcp.tool()
def sympy_poly(expr: str, variable: str = "x") -> str:
    """Create a polynomial."""
    return str(sympy.poly(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_degree(expr: str, variable: str = "x") -> str:
    """Degree of polynomial."""
    return str(sympy.degree(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_roots(expr: str, variable: str = "x") -> str:
    """Find roots of polynomial."""
    return str(sympy.roots(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_coeff(expr: str, x: str, n: int = 1) -> str:
    """Get coefficient."""
    return str(_sympify(expr).coeff(_sympify(x), n))


@mcp.tool()
def sympy_subs(expr: str, old_new: str) -> str:
    """Substitute in expression (format: "old:new,old2:new2")."""
    substitutions = []
    for pair in old_new.split(","):
        old, new = pair.split(":")
        substitutions.append((_sympify(old.strip()), _sympify(new.strip())))
    return str(_sympify(expr).subs(substitutions))


@mcp.tool()
def sympy_atoms(expr: str) -> str:
    """Get atoms (atomic components) of expression."""
    return str(_sympify(expr).atoms())


@mcp.tool()
def sympy_free_symbols(expr: str) -> str:
    """Get free symbols in expression."""
    return str(_sympify(expr).free_symbols)


@mcp.tool()
def sympy_args(expr: str) -> str:
    """Get arguments of expression."""
    return str(_sympify(expr).args)


@mcp.tool()
def sympy_func(expr: str) -> str:
    """Get head function of expression."""
    return str(_sympify(expr).func)


@mcp.tool()
def sympy_expr_type(expr: str) -> str:
    """Get type of expression."""
    return str(type(_sympify(expr)))


@mcp.tool()
def sympy_eq(lhs: str, rhs: str) -> str:
    """Create equality."""
    return str(Eq(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_ne(lhs: str, rhs: str) -> str:
    """Create inequality."""
    return str(Ne(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_lt(lhs: str, rhs: str) -> str:
    """Create less than."""
    return str(Lt(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_le(lhs: str, rhs: str) -> str:
    """Create less than or equal."""
    return str(Le(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_gt(lhs: str, rhs: str) -> str:
    """Create greater than."""
    return str(Gt(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_ge(lhs: str, rhs: str) -> str:
    """Create greater than or equal."""
    return str(Ge(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_And(args: str) -> str:
    """Logical AND (comma-separated)."""
    return str(And(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Or(args: str) -> str:
    """Logical OR (comma-separated)."""
    return str(Or(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Not(expr: str) -> str:
    """Logical NOT."""
    return str(Not(_sympify(expr)))


@mcp.tool()
def sympy_Xor(args: str) -> str:
    """Logical XOR (comma-separated)."""
    return str(Xor(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Nand(args: str) -> str:
    """Logical NAND (comma-separated)."""
    return str(Nand(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Nor(args: str) -> str:
    """Logical NOR (comma-separated)."""
    return str(Nor(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Implies(lhs: str, rhs: str) -> str:
    """Logical implication."""
    return str(Implies(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_satisfiable(expr: str) -> str:
    """Check if expression is satisfiable."""
    return str(satisfiable(_sympify(expr)))


@mcp.tool()
def sympy_Point(x: str, y: str) -> str:
    """Create a 2D point."""
    return str(Point(_sympify(x), _sympify(y)))


@mcp.tool()
def sympy_Point3D(x: str, y: str, z: str) -> str:
    """Create a 3D point."""
    return str(Point3D(_sympify(x), _sympify(y), _sympify(z)))


@mcp.tool()
def sympy_Line(point1: str, point2: str) -> str:
    """Create a line through two points."""
    p1 = _sympify(point1)
    p2 = _sympify(point2)
    return str(Line(p1, p2))


@mcp.tool()
def sympy_Circle(center: str, radius: str) -> str:
    """Create a circle."""
    return str(Circle(_sympify(center), _sympify(radius)))


@mcp.tool()
def sympy_Triangle(point1: str, point2: str, point3: str) -> str:
    """Create a triangle."""
    p1 = _sympify(point1)
    p2 = _sympify(point2)
    p3 = _sympify(point3)
    return str(Triangle(p1, p2, p3))


@mcp.tool()
def sympy_Polygon(points: str) -> str:
    """Create a polygon (comma-separated points)."""
    pts = [_sympify(p) for p in points.split(",")]
    return str(Polygon(*pts))


@mcp.tool()
def sympy_perfect_power(n: str) -> str:
    """Check if n is a perfect power."""
    return str(perfect_power(int(n)))


@mcp.tool()
def sympy_is_square(n: str) -> str:
    """Check if n is a perfect square."""
    return str(sympy.is_square(int(n)))


@mcp.tool()
def sympy_integer(n: str) -> str:
    """Create Integer."""
    return str(Integer(n))


@mcp.tool()
def sympy_float(n: str) -> str:
    """Create Float."""
    return str(Float(n))


@mcp.tool()
def sympy_rational(num: str, den: str) -> str:
    """Create Rational."""
    return str(Rational(num, den))


@mcp.tool()
def sympy_conjugate(expr: str) -> str:
    """Complex conjugate."""
    return str(sympy.conjugate(_sympify(expr)))


@mcp.tool()
def sympy_im(expr: str) -> str:
    """Imaginary part."""
    return str(sympy.im(_sympify(expr)))


@mcp.tool()
def sympy_re(expr: str) -> str:
    """Real part."""
    return str(sympy.re(_sympify(expr)))


@mcp.tool()
def sympy_arg(expr: str) -> str:
    """Argument of complex number."""
    return str(sympy.arg(_sympify(expr)))


@mcp.tool()
def sympy_piecewise(pairs: str) -> str:
    """Create piecewise function (format: "expr,condition; expr2,condition2")."""
    pieces = []
    for pair in pairs.split(";"):
        expr_str, cond = pair.split(",")
        pieces.append((_sympify(expr_str.strip()), _sympify(cond.strip())))
    return str(Piecewise(*pieces))


@mcp.tool()
def sympy_fresnelc(expr: str) -> str:
    """Fresnel C."""
    return str(fresnelc(_sympify(expr)))


@mcp.tool()
def sympy_fresnels(expr: str) -> str:
    """Fresnel S."""
    return str(fresnels(_sympify(expr)))


@mcp.tool()
def sympy_diohyp(expr: str) -> str:
    """Diophantine equation solver."""
    return str(diophantine(_sympify(expr)))


@mcp.tool()
def sympy_dsolve(eq: str, func: str) -> str:
    """Solve ordinary differential equation."""
    return str(dsolve(_sympify(eq), _sympify(func)))


@mcp.tool()
def sympy_checkodesol(eq: str, sol: str) -> str:
    """Check ODE solution."""
    return str(sympy.checkodesol(_sympify(eq), _sympify(sol)))


@mcp.tool()
def sympy_classify_ode(eq: str, func: str) -> str:
    """Classify ODE."""
    return str(sympy.classify_ode(_sympify(eq), _sympify(func)))


@mcp.tool()
def sympy_complexes() -> str:
    """The set of complex numbers."""
    return str(sympy.S.Complexes)


@mcp.tool()
def sympy_reals() -> str:
    """The set of real numbers."""
    return str(sympy.S.Reals)


@mcp.tool()
def sympy_integers() -> str:
    """The set of integers."""
    return str(sympy.S.Integers)


@mcp.tool()
def sympy_naturals() -> str:
    """The set of natural numbers."""
    return str(sympy.S.Naturals)


@mcp.tool()
def sympy_naturals0() -> str:
    """The set of natural numbers (including 0)."""
    return str(sympy.S.Naturals0)


@mcp.tool()
def sympy_emptyset() -> str:
    """Empty set."""
    return str(EmptySet())


@mcp.tool()
def sympy_universalset() -> str:
    """Universal set."""
    return str(UniversalSet())


@mcp.tool()
def sympy_randMatrix(n: int) -> str:
    """Random matrix."""
    return str(randMatrix(n))


@mcp.tool()
def sympy_Wild(pattern: str) -> str:
    """Create Wild pattern."""
    return str(Wild(pattern))


@mcp.tool()
def sympy_WildFunction(name: str) -> str:
    """Create Wild function."""
    return str(WildFunction(name))


@mcp.tool()
def sympy_match(expr: str, pattern: str) -> str:
    """Match expression to pattern."""
    return str(_sympify(expr).match(_sympify(pattern)))


@mcp.tool()
def sympy_replace(expr: str, old_new: str) -> str:
    """Replace in expression (format: "old,new")."""
    parts = old_new.split(",")
    old = _sympify(parts[0].strip())
    new = _sympify(parts[1].strip())
    return str(_sympify(expr).replace(old, new))


@mcp.tool()
def sympy_xreplace(expr: str, mapping: str) -> str:
    """Exact replacement without simplification."""
    d = {}
    for pair in mapping.split(","):
        k, v = pair.split(":")
        d[_sympify(k.strip())] = _sympify(v.strip())
    return str(_sympify(expr).xreplace(d))


@mcp.tool()
def sympy_nsimplify(expr: str) -> str:
    """Numerical simplification."""
    return str(sympy.nsimplify(_sympify(expr)))


@mcp.tool()
def sympy_radsimp(expr: str) -> str:
    """Simplify radicals."""
    return str(sympy.radsimp(_sympify(expr)))


@mcp.tool()
def sympy_rationalize(expr: str) -> str:
    """Rationalize denominator."""
    return str(sympy.rationalize(_sympify(expr)))


@mcp.tool()
def sympy_count_ops(expr: str) -> str:
    """Count operations."""
    return str(sympy.count_ops(_sympify(expr)))


@mcp.tool()
def sympy_symbols_create(names: str) -> str:
    """Create multiple symbols."""
    return str(symbols(names))


@mcp.tool()
def sympy_Range(start: str, stop: str = "") -> str:
    """Range."""
    if stop:
        return str(Range(_sympify(start), _sympify(stop)))
    return str(Range(_sympify(start)))


@mcp.tool()
def sympy_Identity(n: int) -> str:
    """Identity matrix."""
    return str(sympy.Identity(n))


@mcp.tool()
def sympy_matrix_rank(matrix: str) -> str:
    """Matrix rank."""
    return str(_sympify(matrix).rank())


@mcp.tool()
def sympy_matrix_nullspace(matrix: str) -> str:
    """Nullspace."""
    return str(_sympify(matrix).nullspace())


@mcp.tool()
def sympy_matrix_LU(matrix: str) -> str:
    """LU decomposition."""
    return str(_sympify(matrix).LU())


@mcp.tool()
def sympy_expand_complex(expr: str) -> str:
    """Expand complex."""
    return str(expand_complex(_sympify(expr)))


@mcp.tool()
def sympy_as_real_imag(expr: str) -> str:
    """As real and imaginary parts."""
    return str(_sympify(expr).as_real_imag())


@mcp.tool()
def sympy_as_numer_denom(expr: str) -> str:
    """As numerator and denominator."""
    return str(_sympify(expr).as_numer_denom())


@mcp.tool()
def sympy_groebner(exprs: str, variable: str = "x") -> str:
    """Groebner basis."""
    expr_list = [_sympify(e) for e in exprs.split(",")]
    return str(sympy.groebner(expr_list, _sympify(variable)))


@mcp.tool()
def sympy_horner(expr: str, variable: str = "x") -> str:
    """Horner form."""
    return str(sympy.horner(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_divisor_sigma(k: str, n: str) -> str:
    """Divisor function."""
    return str(sympy.divisor_sigma(int(k), int(n)))


@mcp.tool()
def sympy_primepi(n: str) -> str:
    """Prime counting function."""
    return str(sympy.primepi(int(n)))


@mcp.tool()
def sympy_symbolic_power(expr: str, n: str) -> str:
    """Symbolic power."""
    return str(Pow(_sympify(expr), _sympify(n), evaluate=False))


@mcp.tool()
def sympy_symbolic_mul(factors: str) -> str:
    """Symbolic multiplication (comma-separated)."""
    return str(Mul(*[_sympify(f) for f in factors.split(",")], evaluate=False))


@mcp.tool()
def sympy_symbolic_add(terms: str) -> str:
    """Symbolic addition (comma-separated)."""
    return str(Add(*[_sympify(t) for t in terms.split(",")], evaluate=False))


@mcp.tool()
def sympy_finiteset(elements: str) -> str:
    """Create finite set (comma-separated)."""
    elems = [_sympify(e) for e in elements.split(",")]
    return str(FiniteSet(*elems))


@mcp.tool()
def sympy_product_set(sets: str) -> str:
    """Product of sets (comma-separated)."""
    s = [_sympify(s_) for s_ in sets.split(",")]
    return str(sympy.ProductSet(*s))


@mcp.tool()
def sympy_image_set(expr: str, variable: str) -> str:
    """Image set."""
    var = sympy.Symbol(variable)
    return str(sympy.ImageSet(_sympify(expr), var))
