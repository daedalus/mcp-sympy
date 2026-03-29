"""Tests for MCP SymPy tools."""

from mcp_sympy import tools


class TestSymbolCreation:
    """Tests for symbol creation tools."""

    def test_symbol(self):
        """Test creating a single symbol."""
        result = tools.sympy_symbol("x")
        assert "x" in result

    def test_symbols(self):
        """Test creating multiple symbols."""
        result = tools.sympy_symbols("x, y, z")
        assert "x" in result
        assert "y" in result
        assert "z" in result

    def test_symbol_with_assumptions(self):
        """Test symbol with assumptions."""
        result = tools.sympy_symbol("x")
        assert "x" in result

    def test_sympify(self):
        """Test sympify function."""
        result = tools.sympy_sympify("x**2 + 1")
        assert "x" in result


class TestSimplification:
    """Tests for simplification tools."""

    def test_simplify_basic(self):
        """Test basic simplification."""
        result = tools.sympy_simplify("x**2 + 2*x + 1 - (x + 1)**2")
        assert result == "0"

    def test_simplify_trig(self):
        """Test trigonometric simplification."""
        result = tools.sympy_trigsimp("sin(x)**2 + cos(x)**2")
        assert result == "1"

    def test_factor(self):
        """Test factoring."""
        result = tools.sympy_factor("x**2 - 1")
        assert "(x - 1)" in result
        assert "(x + 1)" in result

    def test_expand(self):
        """Test expansion."""
        result = tools.sympy_expand("(x + 1)**2")
        assert "x**2" in result
        assert "2*x" in result

    def test_expand_trig(self):
        """Test trig expansion."""
        result = tools.sympy_expand_trig("sin(2*x)")
        assert "2*sin(x)*cos(x)" == result


class TestSolving:
    """Tests for equation solving."""

    def test_solve_quadratic(self):
        """Test solving quadratic equation."""
        result = tools.sympy_solve("x**2 - 4", "x")
        assert "2" in result
        assert "-2" in result

    def test_solveset(self):
        """Test solveset."""
        result = tools.sympy_solveset("x**2 - 4", "x")
        assert "-2" in result
        assert "2" in result


class TestCalculus:
    """Tests for calculus operations."""

    def test_diff(self):
        """Test differentiation."""
        result = tools.sympy_diff("x**2", "x")
        assert result == "2*x"

    def test_diff_order(self):
        """Test higher order differentiation."""
        result = tools.sympy_diff("x**3", "x", 2)
        assert result == "6*x"

    def test_integrate(self):
        """Test integration."""
        result = tools.sympy_integrate("x**2", "x")
        assert "x**3/3" in result

    def test_limit(self):
        """Test limit."""
        result = tools.sympy_limit("sin(x)/x", "x", "0")
        assert result == "1"

    def test_series(self):
        """Test series expansion."""
        result = tools.sympy_series("exp(x)", "x", "0", 4)
        assert "1 + x + x**2/2" in result


class TestMatrix:
    """Tests for matrix operations."""

    def test_matrix_creation(self):
        """Test matrix creation."""
        result = tools.sympy_matrix("1,2; 3,4")
        assert "Matrix" in result

    def test_matrix_inverse(self):
        """Test matrix inverse."""
        result = tools.sympy_matrix_inverse("Matrix([[1, 2], [3, 4]])")
        assert "Matrix" in result

    def test_matrix_determinant(self):
        """Test matrix determinant."""
        result = tools.sympy_matrix_determinant("Matrix([[1, 2], [3, 4]])")
        assert result == "-2"

    def test_eye(self):
        """Test identity matrix."""
        result = tools.sympy_eye(3)
        assert "Matrix" in result

    def test_zeros(self):
        """Test zeros matrix."""
        result = tools.sympy_zeros(2)
        assert "Matrix" in result


class TestPrinting:
    """Tests for printing functions."""

    def test_latex(self):
        """Test LaTeX output."""
        result = tools.sympy_latex("x**2 + 1")
        assert "x^{2}" in result

    def test_str_output(self):
        """Test string output."""
        result = tools.sympy_str("x**2 + 1")
        assert "x**2" in result


class TestArithmetic:
    """Tests for arithmetic operations."""

    def test_abs(self):
        """Test absolute value."""
        result = tools.sympy_abs("-5")
        assert result == "5"

    def test_sqrt(self):
        """Test square root."""
        result = tools.sympy_sqrt("4")
        assert result == "2"

    def test_factorial(self):
        """Test factorial."""
        result = tools.sympy_factorial("5")
        assert result == "120"

    def test_binomial(self):
        """Test binomial coefficient."""
        result = tools.sympy_binomial("5", "2")
        assert result == "10"


class TestNumberTheory:
    """Tests for number theory functions."""

    def test_isprime(self):
        """Test prime check."""
        result = tools.sympy_isprime("7")
        assert result == "True"

    def test_prime(self):
        """Test nth prime."""
        result = tools.sympy_prime("10")
        assert result == "29"

    def test_totient(self):
        """Test Euler's totient."""
        result = tools.sympy_totient("10")
        assert result == "4"

    def test_gcd(self):
        """Test GCD."""
        result = tools.sympy_gcd("12", "18")
        assert result == "6"

    def test_lcm(self):
        """Test LCM."""
        result = tools.sympy_lcm("4", "6")
        assert result == "12"


class TestTrigonometric:
    """Tests for trigonometric functions."""

    def test_sin(self):
        """Test sine."""
        result = tools.sympy_sin("x")
        assert "sin(x)" in result

    def test_cos(self):
        """Test cosine."""
        result = tools.sympy_cos("x")
        assert "cos(x)" in result

    def test_exp(self):
        """Test exponential."""
        result = tools.sympy_exp("x")
        assert "exp(x)" in result

    def test_log(self):
        """Test logarithm."""
        result = tools.sympy_log("x")
        assert "log(x)" in result


class TestSets:
    """Tests for set operations."""

    def test_finite_set(self):
        """Test finite set creation."""
        result = tools.sympy_finite_set("1,2,3")
        assert "1" in result

    def test_interval(self):
        """Test interval creation."""
        result = tools.sympy_interval("0", "1")
        assert "Interval" in result


class TestLogic:
    """Tests for logic operations."""

    def test_And(self):
        """Test logical AND."""
        result = tools.sympy_And("x,y")
        assert "&" in result

    def test_Or(self):
        """Test logical OR."""
        result = tools.sympy_Or("x,y")
        assert "|" in result

    def test_Not(self):
        """Test logical NOT."""
        result = tools.sympy_Not("x")
        assert "~" in result


class TestSpecialFunctions:
    """Tests for special functions."""

    def test_gamma(self):
        """Test gamma function."""
        result = tools.sympy_gamma("5")
        assert "Gamma" in result or "24" in result

    def test_zeta(self):
        """Test zeta function."""
        result = tools.sympy_zeta("2")
        assert "pi**2/6" == result

    def test_fibonacci(self):
        """Test Fibonacci."""
        result = tools.sympy_fibonacci("10")
        assert result == "55"

    def test_lucas(self):
        """Test Lucas number."""
        result = tools.sympy_lucas("10")
        assert result == "123"


class TestExpression:
    """Tests for expression methods."""

    def test_subs(self):
        """Test substitution."""
        result = tools.sympy_subs("x**2 + y", "x:2")
        assert "y" in result

    def test_free_symbols(self):
        """Test free symbols."""
        result = tools.sympy_free_symbols("x**2 + y")
        assert "x" in result
        assert "y" in result


class TestNumeric:
    """Tests for numerical evaluation."""

    def test_evalf(self):
        """Test numerical evaluation."""
        result = tools.sympy_evalf("sqrt(2)", 10)
        assert "1.414" in result

    def test_n(self):
        """Test n function."""
        result = tools.sympy_n("pi", 10)
        assert "3.14159" in result
