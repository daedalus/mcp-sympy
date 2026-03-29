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
    """Expand trigonometric expressions.

    Args:
        expr: String trigonometric expression

    Returns:
        Expanded expression

    Example:
        >>> sympy_expand_trig("sin(2*x)")
        "2*sin(x)*cos(x)"
    """
    return str(expand_trig(_sympify(expr)))


@mcp.tool()
def sympy_expand_log(expr: str) -> str:
    """Expand logarithmic expressions.

    Args:
        expr: String logarithmic expression

    Returns:
        Expanded expression

    Example:
        >>> sympy_expand_log("log(x*y)")
        "log(x) + log(y)"
    """
    return str(expand_log(_sympify(expr)))


@mcp.tool()
def sympy_together(expr: str) -> str:
    """Combine terms into a single fraction.

    Args:
        expr: String expression

    Returns:
        Combined fraction

    Example:
        >>> sympy_together("1/x + 1/y")
        "(x + y)/(x*y)"
    """
    return str(sympy.together(_sympify(expr)))


@mcp.tool()
def sympy_apart(expr: str) -> str:
    """Perform partial fraction decomposition.

    Args:
        expr: String rational expression

    Returns:
        Partial fractions

    Example:
        >>> sympy_apart("1/(x**2 - 1)")
        "1/(2*(x - 1)) - 1/(2*(x + 1))"
    """
    return str(sympy.apart(_sympify(expr)))


@mcp.tool()
def sympy_cancel(expr: str) -> str:
    """Cancel common factors in rational expression.

    Args:
        expr: String rational expression

    Returns:
        Canceled expression

    Example:
        >>> sympy_cancel("(x**2 - 1)/(x - 1)")
        "x + 1"
    """
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

    Example:
        >>> sympy_sum("k**2", "k", "1", "5")
        "55"
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

    Example:
        >>> sympy_product("k", "k", "1", "5")
        "120"
    """
    var = sympy.Symbol(variable)
    result = product(_sympify(expr), (var, _sympify(lower), _sympify(upper)))
    return str(result)


@mcp.tool()
def sympy_summation(expr: str, variable: str, bounds: str) -> str:
    """Compute an unevaluated sum (Sum object).

    Args:
        expr: String expression
        variable: Summation variable
        bounds: Lower and upper bound as "lower,upper"

    Returns:
        Sum object as string

    Example:
        >>> sympy_summation("k**2", "k", "1,5")
        "Sum(k**2, (k, 1, 5))"
    """
    var = sympy.Symbol(variable)
    lower, upper = bounds.split(",")
    result = Sum(
        _sympify(expr), (var, _sympify(lower.strip()), _sympify(upper.strip()))
    )
    return str(result)


@mcp.tool()
def sympy_product_expr(expr: str, variable: str, bounds: str) -> str:
    """Compute an unevaluated product (Product object).

    Args:
        expr: String expression
        variable: Product variable
        bounds: Lower and upper bound as "lower,upper"

    Returns:
        Product object as string

    Example:
        >>> sympy_product_expr("k", "k", "1,5")
        "Product(k, (k, 1, 5))"
    """
    var = sympy.Symbol(variable)
    lower, upper = bounds.split(",")
    result = Product(
        _sympify(expr), (var, _sympify(lower.strip()), _sympify(upper.strip()))
    )
    return str(result)


@mcp.tool()
def sympy_derivative(expr: str, variable: str, order: int = 1) -> str:
    """Create a Derivative object (unevaluated).

    Args:
        expr: String expression
        variable: Variable to differentiate
        order: Order of derivative

    Returns:
        Derivative object as string

    Example:
        >>> sympy_derivative("x**2", "x")
        "Derivative(x**2, x)"
    """
    var = sympy.Symbol(variable)
    result = Derivative(_sympify(expr), var, order)
    return str(result)


@mcp.tool()
def sympy_integral(expr: str, variable: str) -> str:
    """Create an Integral object (unevaluated).

    Args:
        expr: String expression
        variable: Variable to integrate

    Returns:
        Integral object as string

    Example:
        >>> sympy_integral("x**2", "x")
        "Integral(x**2, x)"
    """
    var = sympy.Symbol(variable)
    result = Integral(_sympify(expr), var)
    return str(result)


@mcp.tool()
def sympy_matrix(rows: str) -> str:
    """Create a matrix from rows.

    Args:
        rows: Semicolon-separated rows, e.g., "1,2; 3,4"

    Returns:
        Matrix as string

    Example:
        >>> sympy_matrix("1,2; 3,4")
        "Matrix([[1, 2], [3, 4]])"
    """
    row_list = [r.split(",") for r in rows.split(";")]
    matrix_data = [[int(x.strip()) for x in row] for row in row_list]
    return str(Matrix(matrix_data))


@mcp.tool()
def sympy_matrix_add(matrix1: str, matrix2: str) -> str:
    """Add two matrices.

    Args:
        matrix1: First matrix string
        matrix2: Second matrix string

    Returns:
        Sum matrix as string

    Example:
        >>> sympy_matrix_add("Matrix([[1, 2], [3, 4]])", "Matrix([[5, 6], [7, 8]])")
        "Matrix([[6, 8], [10, 12]])"
    """
    m1 = _sympify(matrix1)
    m2 = _sympify(matrix2)
    return str(m1 + m2)


@mcp.tool()
def sympy_matrix_multiply(matrix1: str, matrix2: str) -> str:
    """Multiply two matrices.

    Args:
        matrix1: First matrix string
        matrix2: Second matrix string

    Returns:
        Product matrix as string

    Example:
        >>> sympy_matrix_multiply("Matrix([[1, 2], [3, 4]])", "Matrix([[5, 6], [7, 8]])")
        "Matrix([[19, 22], [43, 50]])"
    """
    m1 = _sympify(matrix1)
    m2 = _sympify(matrix2)
    return str(m1 * m2)


@mcp.tool()
def sympy_matrix_inverse(matrix: str) -> str:
    """Compute matrix inverse.

    Args:
        matrix: Matrix string

    Returns:
        Inverse matrix as string

    Example:
        >>> sympy_matrix_inverse("Matrix([[1, 2], [3, 4]])")
        "Matrix([[-2, 1], [1.5, -0.5]])"
    """
    m = _sympify(matrix)
    return str(m.inv())


@mcp.tool()
def sympy_matrix_determinant(matrix: str) -> str:
    """Compute matrix determinant.

    Args:
        matrix: A SymPy matrix string, e.g., "Matrix([[1, 2], [3, 4]])"

    Returns:
        The determinant as a string.

    Example:
        >>> sympy_matrix_determinant("Matrix([[1, 2], [3, 4]])")
        "-2"
    """
    m = _sympify(matrix)
    return str(m.det())


@mcp.tool()
def sympy_matrix_transpose(matrix: str) -> str:
    """Transpose a matrix.

    Args:
        matrix: Matrix string

    Returns:
        Transposed matrix as string

    Example:
        >>> sympy_matrix_transpose("Matrix([[1, 2], [3, 4]])")
        "Matrix([[1, 3], [2, 4]])"
    """
    m = _sympify(matrix)
    return str(m.T)


@mcp.tool()
def sympy_matrix_eigenvals(matrix: str) -> str:
    """Compute eigenvalues of a matrix.

    Args:
        matrix: Matrix string

    Returns:
        Eigenvalues as string

    Example:
        >>> sympy_matrix_eigenvals("Matrix([[1, 2], [2, 1]])")
        "{5: 1, -3: 1}"
    """
    m = _sympify(matrix)
    return str(m.eigenvals())


@mcp.tool()
def sympy_matrix_eigenvects(matrix: str) -> str:
    """Compute eigenvectors of a matrix.

    Args:
        matrix: Matrix string

    Returns:
        Eigenvectors as string

    Example:
        >>> sympy_matrix_eigenvects("Matrix([[1, 0], [0, 2]])")
        "(1, 1, [Matrix([[1], [0]]), Matrix([[0], [1]])])"
    """
    m = _sympify(matrix)
    return str(m.eigenvects())


@mcp.tool()
def sympy_eye(n: int) -> str:
    """Create an identity matrix.

    Args:
        n: Size of the matrix

    Returns:
        Identity matrix as string

    Example:
        >>> sympy_eye(3)
        "Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])"
    """
    return str(eye(n))


@mcp.tool()
def sympy_zeros(rows: int, cols: int = 0) -> str:
    """Create a zero matrix.

    Args:
        rows: Number of rows
        cols: Number of columns (default: same as rows)

    Returns:
        Zero matrix as string

    Example:
        >>> sympy_zeros(2, 3)
        "Matrix([[0, 0, 0], [0, 0, 0]])"
    """
    if cols == 0:
        cols = rows
    return str(zeros(rows, cols))


@mcp.tool()
def sympy_ones(rows: int, cols: int = 0) -> str:
    """Create a matrix of ones.

    Args:
        rows: Number of rows
        cols: Number of columns (default: same as rows)

    Returns:
        Matrix of ones as string

    Example:
        >>> sympy_ones(2, 3)
        "Matrix([[1, 1, 1], [1, 1, 1]])"
    """
    if cols == 0:
        cols = rows
    return str(ones(rows, cols))


@mcp.tool()
def sympy_diag(elements: str) -> str:
    """Create a diagonal matrix.

    Args:
        elements: Comma-separated diagonal elements

    Returns:
        Diagonal matrix as string

    Example:
        >>> sympy_diag("1,2,3")
        "Matrix([[1, 0, 0], [0, 2, 0], [0, 0, 3]])"
    """
    elems = [_sympify(e) for e in elements.split(",")]
    return str(diag(*elems))


@mcp.tool()
def sympy_latex(expr: str) -> str:
    """Convert expression to LaTeX.

    Args:
        expr: SymPy expression string

    Returns:
        LaTeX string

    Example:
        >>> sympy_latex("x**2 + sin(y)")
        "x^{2} + \\sin{\\left(y\\right)}"
    """
    return str(latex(_sympify(expr)))


@mcp.tool()
def sympy_python_code(expr: str) -> str:
    """Convert expression to Python code.

    Args:
        expr: SymPy expression string

    Returns:
        Python code string

    Example:
        >>> sympy_python_code("x**2 + 1")
        "x**2 + 1"
    """
    return str(sympy.python(_sympify(expr)))


@mcp.tool()
def sympy_mathml(expr: str) -> str:
    """Convert expression to MathML.

    Args:
        expr: SymPy expression string

    Returns:
        MathML string

    Example:
        >>> sympy_mathml("x**2")
        "<math><apply><power/><ci>x</ci><cn>2</cn></apply></math>"
    """
    return str(sympy.mathml(_sympify(expr)))


@mcp.tool()
def sympy_str(expr: str) -> str:
    """Convert expression to string.

    Args:
        expr: SymPy expression string

    Returns:
        String representation

    Example:
        >>> sympy_str("x**2 + 1")
        "x**2 + 1"
    """
    return str(_sympify(expr))


@mcp.tool()
def sympy_repr_expr(expr: str) -> str:
    """Get repr of expression.

    Args:
        expr: SymPy expression string

    Returns:
        repr string

    Example:
        >>> sympy_repr_expr("x**2")
        "Pow(Symbol('x'), Integer(2))"
    """
    return repr(_sympify(expr))


@mcp.tool()
def sympy_interval(
    start: str, end: str, left_open: bool = False, right_open: bool = False
) -> str:
    """Create an interval.

    Args:
        start: Start value
        end: End value
        left_open: Whether left is open
        right_open: Whether right is open

    Returns:
        Interval as string

    Example:
        >>> sympy_interval("0", "1", true, true)
        "(0, 1)"
    """
    result = Interval(_sympify(start), _sympify(end), left_open, right_open)
    return str(result)


@mcp.tool()
def sympy_finite_set(elements: str) -> str:
    """Create a finite set.

    Args:
        elements: Comma-separated elements

    Returns:
        Finite set as string

    Example:
        >>> sympy_finite_set("1,2,3,4,5")
        "{1, 2, 3, 4, 5}"
    """
    elems = [_sympify(e) for e in elements.split(",")]
    return str(FiniteSet(*elems))


@mcp.tool()
def sympy_union(set1: str, set2: str) -> str:
    """Compute union of two sets.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Union as string

    Example:
        >>> sympy_union("{1,2}", "{2,3}")
        "{1, 2, 3}"
    """
    s1 = _sympify(set1)
    s2 = _sympify(set2)
    return str(Union(s1, s2))


@mcp.tool()
def sympy_intersection(set1: str, set2: str) -> str:
    """Compute intersection of two sets.

    Args:
        set1: First set
        set2: Second set

    Returns:
        Intersection as string

    Example:
        >>> sympy_intersection("{1,2,3}", "{2,3,4}")
        "{2, 3}"
    """
    s1 = _sympify(set1)
    s2 = _sympify(set2)
    return str(Intersection(s1, s2))


@mcp.tool()
def sympy_complement(set1: str, set2: str) -> str:
    """Compute complement of set1 in set2.

    Args:
        set1: Subset
        set2: Universal set

    Returns:
        Complement as string

    Example:
        >>> sympy_complement("{1,2}", "{1,2,3,4}")
        "{3, 4}"
    """
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
    """Evaluate expression numerically.

    Args:
        expr: Expression to evaluate
        n: Number of digits

    Returns:
        Numerical result

    Example:
        >>> sympy_n("pi", 10)
        "3.141592654"
    """
    return str(_sympify(expr).n(n))


@mcp.tool()
def sympy_evalf(expr: str, n: int = 15) -> str:
    """Evaluate expression to floating point.

    Args:
        expr: Expression to evaluate
        n: Number of digits

    Returns:
        Float result

    Example:
        >>> sympy_evalf("sqrt(2)", 5)
        "1.4142"
    """
    return str(_sympify(expr).evalf(n))


@mcp.tool()
def sympy_exp(expr: str) -> str:
    """Exponential function.

    Args:
        expr: Expression

    Returns:
        exp(expr) as string

    Example:
        >>> sympy_exp("1")
        "E"
    """
    return str(exp(_sympify(expr)))


@mcp.tool()
def sympy_log(expr: str) -> str:
    """Natural logarithm.

    Args:
        expr: Expression

    Returns:
        log(expr) as string

    Example:
        >>> sympy_log("E")
        "1"
    """
    return str(log(_sympify(expr)))


@mcp.tool()
def sympy_log_base(expr: str, base: str) -> str:
    """Logarithm with specified base.

    Args:
        expr: Expression
        base: Logarithm base

    Returns:
        log_base(expr) as string

    Example:
        >>> sympy_log_base("100", "10")
        "2"
    """
    return str(log(_sympify(expr), _sympify(base)))


@mcp.tool()
def sympy_sin(expr: str) -> str:
    """Sine function.

    Args:
        expr: Expression (in radians)

    Returns:
        sin(expr) as string

    Example:
        >>> sympy_sin("pi/2")
        "1"
    """
    return str(sin(_sympify(expr)))


@mcp.tool()
def sympy_cos(expr: str) -> str:
    """Cosine function.

    Args:
        expr: Expression (in radians)

    Returns:
        cos(expr) as string

    Example:
        >>> sympy_cos("0")
        "1"
    """
    return str(cos(_sympify(expr)))


@mcp.tool()
def sympy_tan(expr: str) -> str:
    """Tangent function.

    Args:
        expr: Expression (in radians)

    Returns:
        tan(expr) as string

    Example:
        >>> sympy_tan("pi/4")
        "1"
    """
    return str(tan(_sympify(expr)))


@mcp.tool()
def sympy_sinh(expr: str) -> str:
    """Hyperbolic sine.

    Args:
        expr: Expression

    Returns:
        sinh(expr) as string

    Example:
        >>> sympy_sinh("0")
        "0"
    """
    return str(sinh(_sympify(expr)))


@mcp.tool()
def sympy_cosh(expr: str) -> str:
    """Hyperbolic cosine.

    Args:
        expr: Expression

    Returns:
        cosh(expr) as string

    Example:
        >>> sympy_cosh("0")
        "1"
    """
    return str(cosh(_sympify(expr)))


@mcp.tool()
def sympy_tanh(expr: str) -> str:
    """Hyperbolic tangent.

    Args:
        expr: Expression

    Returns:
        tanh(expr) as string

    Example:
        >>> sympy_tanh("0")
        "0"
    """
    return str(tanh(_sympify(expr)))


@mcp.tool()
def sympy_asin(expr: str) -> str:
    """Arc sine.

    Args:
        expr: Expression (between -1 and 1)

    Returns:
        asin(expr) as string

    Example:
        >>> sympy_asin("0")
        "0"
    """
    return str(asin(_sympify(expr)))


@mcp.tool()
def sympy_acos(expr: str) -> str:
    """Arc cosine.

    Args:
        expr: Expression (between -1 and 1)

    Returns:
        acos(expr) as string

    Example:
        >>> sympy_acos("1")
        "0"
    """
    return str(acos(_sympify(expr)))


@mcp.tool()
def sympy_atan(expr: str) -> str:
    """Arc tangent.

    Args:
        expr: Expression

    Returns:
        atan(expr) as string

    Example:
        >>> sympy_atan("1")
        "pi/4"
    """
    return str(atan(_sympify(expr)))


@mcp.tool()
def sympy_sqrt(expr: str) -> str:
    """Square root.

    Args:
        expr: Expression

    Returns:
        sqrt(expr) as string

    Example:
        >>> sympy_sqrt("4")
        "2"
    """
    return str(sqrt(_sympify(expr)))


@mcp.tool()
def sympy_cbrt(expr: str) -> str:
    """Cube root.

    Args:
        expr: Expression

    Returns:
        cbrt(expr) as string

    Example:
        >>> sympy_cbrt("8")
        "2"
    """
    return str(sympy.cbrt(_sympify(expr)))


@mcp.tool()
def sympy_root(expr: str, n: int = 2) -> str:
    """N-th root.

    Args:
        expr: Expression
        n: Root degree

    Returns:
        Root as string

    Example:
        >>> sympy_root("8", "3")
        "2"
    """
    return str(root(_sympify(expr), n))


@mcp.tool()
def sympy_floor(expr: str) -> str:
    """Floor function.

    Args:
        expr: Expression

    Returns:
        floor(expr) as string

    Example:
        >>> sympy_floor("3.7")
        "3"
    """
    return str(floor(_sympify(expr)))


@mcp.tool()
def sympy_ceiling(expr: str) -> str:
    """Ceiling function.

    Args:
        expr: Expression

    Returns:
        ceiling(expr) as string

    Example:
        >>> sympy_ceiling("3.2")
        "4"
    """
    return str(ceiling(_sympify(expr)))


@mcp.tool()
def sympy_abs(expr: str) -> str:
    """Absolute value.

    Args:
        expr: Expression

    Returns:
        abs(expr) as string

    Example:
        >>> sympy_abs("-5")
        "5"
    """
    return str(Abs(_sympify(expr)))


@mcp.tool()
def sympy_factorial(n: str) -> str:
    """Factorial.

    Args:
        n: Non-negative integer

    Returns:
        n! as string

    Example:
        >>> sympy_factorial("5")
        "120"
    """
    return str(factorial(int(n)))


@mcp.tool()
def sympy_binomial(n: str, k: str) -> str:
    """Binomial coefficient.

    Args:
        n: Non-negative integer
        k: Non-negative integer

    Returns:
        C(n,k) as string

    Example:
        >>> sympy_binomial("5", "2")
        "10"
    """
    return str(binomial(int(n), int(k)))


@mcp.tool()
def sympy_gamma(expr: str) -> str:
    """Gamma function.

    Args:
        expr: Expression

    Returns:
        Gamma(expr) as string

    Example:
        >>> sympy_gamma("5")
        "24"
    """
    return str(gamma(_sympify(expr)))


@mcp.tool()
def sympy_zeta(s: str) -> str:
    """Riemann zeta function.

    Args:
        s: Expression

    Returns:
        zeta(s) as string

    Example:
        >>> sympy_zeta("2")
        "pi**2/6"
    """
    return str(zeta(_sympify(s)))


@mcp.tool()
def sympy_erf(expr: str) -> str:
    """Error function.

    Args:
        expr: Expression

    Returns:
        erf(expr) as string

    Example:
        >>> sympy_erf("0")
        "0"
    """
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
    """Fibonacci number.

    Args:
        n: Non-negative integer

    Returns:
        F(n) as string

    Example:
        >>> sympy_fibonacci("10")
        "55"
    """
    return str(fibonacci(int(n)))


@mcp.tool()
def sympy_lucas(n: str) -> str:
    """Lucas number.

    Args:
        n: Non-negative integer

    Returns:
        L(n) as string

    Example:
        >>> sympy_lucas("10")
        "123"
    """
    return str(lucas(int(n)))


@mcp.tool()
def sympy_catalan(n: str) -> str:
    """Catalan number.

    Args:
        n: Non-negative integer

    Returns:
        C(n) as string

    Example:
        >>> sympy_catalan("5")
        "42"
    """
    return str(catalan(int(n)))


@mcp.tool()
def sympy_isprime(n: str) -> str:
    """Check if n is prime.

    Args:
        n: Integer

    Returns:
        "True" or "False"

    Example:
        >>> sympy_isprime("7")
        "True"
    """
    return str(isprime(int(n)))


@mcp.tool()
def sympy_prime(n: str) -> str:
    """Return the n-th prime.

    Args:
        n: Positive integer (1-indexed)

    Returns:
        n-th prime as string

    Example:
        >>> sympy_prime("10")
        "29"
    """
    return str(prime(int(n)))


@mcp.tool()
def sympy_nextprime(n: str) -> str:
    """Return the next prime after n.

    Args:
        n: Integer

    Returns:
        Next prime as string

    Example:
        >>> sympy_nextprime("10")
        "11"
    """
    return str(nextprime(int(n)))


@mcp.tool()
def sympy_prevprime(n: str) -> str:
    """Return the previous prime before n.

    Args:
        n: Integer > 2

    Returns:
        Previous prime as string

    Example:
        >>> sympy_prevprime("10")
        "7"
    """
    return str(prevprime(int(n)))


@mcp.tool()
def sympy_totient(n: str) -> str:
    """Euler's totient function.

    Args:
        n: Positive integer

    Returns:
        phi(n) as string

    Example:
        >>> sympy_totient("10")
        "4"
    """
    return str(totient(int(n)))


@mcp.tool()
def sympy_divisors(n: str) -> str:
    """Return divisors of n.

    Args:
        n: Positive integer

    Returns:
        List of divisors

    Example:
        >>> sympy_divisors("12")
        "[1, 2, 3, 4, 6, 12]"
    """
    return str(divisors(int(n)))


@mcp.tool()
def sympy_gcd(a: str, b: str) -> str:
    """Greatest common divisor.

    Args:
        a: Integer
        b: Integer

    Returns:
        gcd(a, b) as string

    Example:
        >>> sympy_gcd("48", "18")
        "6"
    """
    return str(sympy.gcd(int(a), int(b)))


@mcp.tool()
def sympy_lcm(a: str, b: str) -> str:
    """Least common multiple.

    Args:
        a: Integer
        b: Integer

    Returns:
        lcm(a, b) as string

    Example:
        >>> sympy_lcm("4", "6")
        "12"
    """
    return str(sympy.lcm(int(a), int(b)))


@mcp.tool()
def sympy_factorint(n: str) -> str:
    """Integer factorization.

    Args:
        n: Integer

    Returns:
        Prime factorization as string

    Example:
        >>> sympy_factorint("12")
        "{2: 2, 3: 1}"
    """
    return str(sympy.factorint(int(n)))


@mcp.tool()
def sympy_poly(expr: str, variable: str = "x") -> str:
    """Create a polynomial.

    Args:
        expr: Expression
        variable: Variable

    Returns:
        Polynomial as string

    Example:
        >>> sympy_poly("x**2 + 2*x + 1", "x")
        "x**2 + 2*x + 1"
    """
    return str(sympy.poly(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_degree(expr: str, variable: str = "x") -> str:
    """Degree of polynomial.

    Args:
        expr: Polynomial expression
        variable: Variable

    Returns:
        Degree as string

    Example:
        >>> sympy_degree("x**3 + x**2 + 1", "x")
        "3"
    """
    return str(sympy.degree(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_roots(expr: str, variable: str = "x") -> str:
    """Find roots of polynomial.

    Args:
        expr: Polynomial expression
        variable: Variable

    Returns:
        Roots as string

    Example:
        >>> sympy_roots("x**2 - 4", "x")
        "{2: 1, -2: 1}"
    """
    return str(sympy.roots(_sympify(expr), _sympify(variable)))


@mcp.tool()
def sympy_coeff(expr: str, x: str, n: int = 1) -> str:
    """Get coefficient.

    Args:
        expr: Expression
        x: Variable
        n: Power of x

    Returns:
        Coefficient as string

    Example:
        >>> sympy_coeff("3*x**2 + 2*x + 1", "x", 2)
        "3"
    """
    return str(_sympify(expr).coeff(_sympify(x), n))


@mcp.tool()
def sympy_subs(expr: str, old_new: str) -> str:
    """Substitute in expression.

    Args:
        expr: Expression
        old_new: Substitutions as "old:new,old2:new2"

    Returns:
        Substituted expression

    Example:
        >>> sympy_subs("x**2 + y", "x:2,y:3")
        "7"
    """
    substitutions = []
    for pair in old_new.split(","):
        old, new = pair.split(":")
        substitutions.append((_sympify(old.strip()), _sympify(new.strip())))
    return str(_sympify(expr).subs(substitutions))


@mcp.tool()
def sympy_atoms(expr: str) -> str:
    """Get atoms (atomic components) of expression.

    Args:
        expr: Expression

    Returns:
        Set of atoms

    Example:
        >>> sympy_atoms("x**2 + y")
        "{x, y}"
    """
    return str(_sympify(expr).atoms())


@mcp.tool()
def sympy_free_symbols(expr: str) -> str:
    """Get free symbols in expression.

    Args:
        expr: Expression

    Returns:
        Set of free symbols

    Example:
        >>> sympy_free_symbols("x**2 + y")
        "{x, y}"
    """
    return str(_sympify(expr).free_symbols)


@mcp.tool()
def sympy_args(expr: str) -> str:
    """Get arguments of expression.

    Args:
        expr: Expression

    Returns:
        Tuple of arguments

    Example:
        >>> sympy_args("x + y")
        "(x, y)"
    """
    return str(_sympify(expr).args)


@mcp.tool()
def sympy_func(expr: str) -> str:
    """Get head function of expression.

    Args:
        expr: Expression

    Returns:
        Function head

    Example:
        >>> sympy_func("x + y")
        "Add"
    """
    return str(_sympify(expr).func)


@mcp.tool()
def sympy_expr_type(expr: str) -> str:
    """Get type of expression.

    Args:
        expr: Expression

    Returns:
        Type as string

    Example:
        >>> sympy_expr_type("x + 1")
        "<class 'sympy.core.add.Add'>"
    """
    return str(type(_sympify(expr)))


@mcp.tool()
def sympy_eq(lhs: str, rhs: str) -> str:
    """Create equality.

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Equality as string

    Example:
        >>> sympy_eq("x", "y")
        "Eq(x, y)"
    """
    return str(Eq(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_ne(lhs: str, rhs: str) -> str:
    """Create inequality (not equal).

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Neq as string

    Example:
        >>> sympy_ne("x", "y")
        "Ne(x, y)"
    """
    return str(Ne(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_lt(lhs: str, rhs: str) -> str:
    """Create less than.

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Less than as string

    Example:
        >>> sympy_lt("x", "y")
        "x < y"
    """
    return str(Lt(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_le(lhs: str, rhs: str) -> str:
    """Create less than or equal.

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Less than or equal as string

    Example:
        >>> sympy_le("x", "y")
        "x <= y"
    """
    return str(Le(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_gt(lhs: str, rhs: str) -> str:
    """Create greater than.

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Greater than as string

    Example:
        >>> sympy_gt("x", "y")
        "x > y"
    """
    return str(Gt(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_ge(lhs: str, rhs: str) -> str:
    """Create greater than or equal.

    Args:
        lhs: Left-hand side
        rhs: Right-hand side

    Returns:
        Greater than or equal as string

    Example:
        >>> sympy_ge("x", "y")
        "x >= y"
    """
    return str(Ge(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_And(args: str) -> str:
    """Logical AND.

    Args:
        args: Comma-separated expressions

    Returns:
        And as string

    Example:
        >>> sympy_And("True, False")
        "False"
    """
    return str(And(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Or(args: str) -> str:
    """Logical OR.

    Args:
        args: Comma-separated expressions

    Returns:
        Or as string

    Example:
        >>> sympy_Or("True, False")
        "True"
    """
    return str(Or(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Not(expr: str) -> str:
    """Logical NOT.

    Args:
        expr: Boolean expression

    Returns:
        Not as string

    Example:
        >>> sympy_Not("True")
        "False"
    """
    return str(Not(_sympify(expr)))


@mcp.tool()
def sympy_Xor(args: str) -> str:
    """Logical XOR.

    Args:
        args: Comma-separated expressions

    Returns:
        Xor as string

    Example:
        >>> sympy_Xor("True, False")
        "True"
    """
    return str(Xor(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Nand(args: str) -> str:
    """Logical NAND.

    Args:
        args: Comma-separated expressions

    Returns:
        Nand as string

    Example:
        >>> sympy_Nand("True, True")
        "False"
    """
    return str(Nand(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Nor(args: str) -> str:
    """Logical NOR.

    Args:
        args: Comma-separated expressions

    Returns:
        Nor as string

    Example:
        >>> sympy_Nor("False, False")
        "True"
    """
    return str(Nor(*[_sympify(a) for a in args.split(",")]))


@mcp.tool()
def sympy_Implies(lhs: str, rhs: str) -> str:
    """Logical implication.

    Args:
        lhs: Antecedent
        rhs: Consequent

    Returns:
        Implies as string

    Example:
        >>> sympy_Implies("True", "False")
        "False"
    """
    return str(Implies(_sympify(lhs), _sympify(rhs)))


@mcp.tool()
def sympy_satisfiable(expr: str) -> str:
    """Check if expression is satisfiable.

    Args:
        expr: Boolean expression

    Returns:
        Solution or False

    Example:
        >>> sympy_satisfiable("x & y")
        "{x: True, y: True}"
    """
    return str(satisfiable(_sympify(expr)))


@mcp.tool()
def sympy_Point(x: str, y: str) -> str:
    """Create a 2D point.

    Args:
        x: x-coordinate
        y: y-coordinate

    Returns:
        Point as string

    Example:
        >>> sympy_Point("1", "2")
        "(1, 2)"
    """
    return str(Point(_sympify(x), _sympify(y)))


@mcp.tool()
def sympy_Point3D(x: str, y: str, z: str) -> str:
    """Create a 3D point.

    Args:
        x: x-coordinate
        y: y-coordinate
        z: z-coordinate

    Returns:
        Point3D as string

    Example:
        >>> sympy_Point3D("1", "2", "3")
        "(1, 2, 3)"
    """
    return str(Point3D(_sympify(x), _sympify(y), _sympify(z)))


@mcp.tool()
def sympy_Line(point1: str, point2: str) -> str:
    """Create a line through two points.

    Args:
        point1: First point
        point2: Second point

    Returns:
        Line as string

    Example:
        >>> sympy_Line("(0, 0)", "(1, 1)")
        "Line2D(Point2D(0, 0), Point2D(1, 1))"
    """
    p1 = _sympify(point1)
    p2 = _sympify(point2)
    return str(Line(p1, p2))


@mcp.tool()
def sympy_Circle(center: str, radius: str) -> str:
    """Create a circle.

    Args:
        center: Center point
        radius: Radius

    Returns:
        Circle as string

    Example:
        >>> sympy_Circle("(0, 0)", "1")
        "Circle(Point2D(0, 0), 1)"
    """
    return str(Circle(_sympify(center), _sympify(radius)))


@mcp.tool()
def sympy_Triangle(point1: str, point2: str, point3: str) -> str:
    """Create a triangle.

    Args:
        point1: First vertex
        point2: Second vertex
        point3: Third vertex

    Returns:
        Triangle as string

    Example:
        >>> sympy_Triangle("(0, 0)", "(1, 0)", "(0, 1)")
        "Triangle(Point2D(0, 0), Point2D(1, 0), Point2D(0, 1))"
    """
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
    """Solve a Diophantine equation.

    Args:
        expr: A SymPy expression equal to zero, e.g., "x**2 + y**2 - 25"
              (not "x**2 + y**2 = 25")

    Returns:
        Set of integer solutions as a string.

    Example:
        >>> sympy_diohyp("x**2 + y**2 - 25")
        "{(5, 0), (0, 5), (-5, 0), (0, -5), (3, 4), ...}"
    """
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
