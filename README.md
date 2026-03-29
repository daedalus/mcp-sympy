# mcp-sympy

> MCP server that exposes SymPy's symbolic mathematics functionality

[![PyPI](https://img.shields.io/pypi/v/mcp-sympy.svg)](https://pypi.org/project/mcp-sympy/)
[![Python](https://img.shields.io/pypi/pyversions/mcp-sympy.svg)](https://pypi.org/project/mcp-sympy/)
[![Coverage](https://codecov.io/gh/daedalus/mcp-sympy/branch/main/graph/badge.svg)](https://codecov.io/gh/daedalus/mcp-sympy)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Install

```bash
pip install mcp-sympy
```

## MCP Server

mcp-name: io.github.daedalus/mcp-sympy

## Usage

### As MCP Server

Configure in your MCP client:

```json
{
  "mcpServers": {
    "mcp-sympy": {
      "command": "mcp-sympy",
      "env": {}
    }
  }
}
```

### Python API

```python
from mcp_sympy import tools

# Simplify expressions
result = tools.sympy_simplify("sin(x)**2 + cos(x)**2")
print(result)  # "1"

# Solve equations
result = tools.sympy_solve("x**2 - 4", "x")
print(result)  # "[2, -2]"

# Differentiate
result = tools.sympy_diff("x**2", "x")
print(result)  # "2*x"

# Integrate
result = tools.sympy_integrate("x**2", "x")
print(result)  # "x**3/3"

# Create matrices
result = tools.sympy_matrix("1,2; 3,4")
print(result)  # "Matrix([[1, 2], [3, 4]])"

# Number theory
result = tools.sympy_isprime("7")
print(result)  # "True"
```

## Available Tools

The MCP server exposes comprehensive SymPy functionality including:

- **Symbolic Expressions**: symbols, sympify, simplify, expand, factor
- **Calculus**: diff, integrate, limit, series, Derivative, Integral
- **Solving**: solve, solveset, nsolve, diophantine, dsolve
- **Matrices**: Matrix operations, inverse, determinant, eigenvalues
- **Trigonometry**: sin, cos, tan, and their inverses
- **Special Functions**: gamma, zeta, erf, fibonacci, etc.
- **Number Theory**: isprime, prime, gcd, lcm, totient
- **Sets**: FiniteSet, Interval, Union, Intersection
- **Logic**: And, Or, Not, Xor
- **Printing**: LaTeX, MathML, Python code

## Development

```bash
git clone https://github.com/daedalus/mcp-sympy.git
cd mcp-sympy
pip install -e ".[test]"

# run tests
pytest

# format
ruff format src/ tests/

# lint
ruff check src/ tests/

# type check
mypy src/
```

## License

MIT License - see LICENSE file.
