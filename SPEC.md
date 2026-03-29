# SPEC.md — mcp-sympy

## Purpose

MCP server that exposes SymPy's complete symbolic mathematics API via the Model Context Protocol. Provides tools for symbolic computation including algebra, calculus, matrices, geometry, number theory, and more.

## Scope

- **In scope**: All SymPy modules and their public functions
- **Not in scope**: Interactive REPL features, graphical plotting output

## Public API / Interface

### MCP Tools

All SymPy public functions exposed as MCP tools with the following naming convention:
- Module prefix: `sympy_<module_name>_<function_name>`
- Tools accept string expressions and return string results
- Tools include comprehensive docstrings with examples

### Supported SymPy Modules

1. **core** - Basic objects (Symbol, Integer, Float, Rational, Add, Mul, Pow, etc.)
2. **functions** - Elementary (sin, cos, exp, log, etc.) and special functions
3. **simplify** - Simplification algorithms
4. **solve** - Equation solving
5. **integrals** - Integration
6. **derivatives** - Differentiation
7. **limits** - Limit computation
8. **series** - Series expansion
9. **matrices** - Matrix operations
10. **geometry** - Geometric entities
11. **sets** - Set operations
12. **logic** - Boolean logic
13. **concrete** - Products, sums, summations
14. **polynomials** - Polynomial algebra
15. **numeric** - Numeric evaluation
16. **printing** - Code generation (Python, LaTeX, MathML, etc.)
17. **stats** - Probability and statistics
18. **utilities** - Utility functions
19. **tensor** - Tensor operations
20. **parsing** - Expression parsing
21. **discrete** - Discrete transforms
22. **combinatorics** - Combinatorial functions
23. **liealgebras** - Lie algebras
24. **vector** - Vector calculus
25. **matrixutilities** - Matrix utilities
26. **galgebra** - Geometric algebra
27. **cryptography** - Cryptographic functions
28. **finance** - Financial functions
29. **mechanics** - Mechanics framework
30. **relativity** - Relativity framework
31. **printing** - Various printing backends

### Tool Categories

1. **Expression Creation**: symbols, sympify, Symbol, Integer, Float, Rational, Complex, I, E, oo, pi
2. **Arithmetic**: add, mul, pow, div, mod, abs
3. **Simplification**: simplify, trigsimp, ratsimp, powsimp, combsimplify, factor, expand
4. **Solving**: solve, solveset, nsolve, diophantine, dsolve
5. **Calculus**: diff, integrate, limit, series, Derivative, Integral
6. **Matrices**: Matrix, matrix operations, eigen values/vectors
7. **Functions**: All elementary and special functions
8. **Sets**: Interval, FiniteSet, Union, Intersection, Complement
9. **Geometry**: Point, Line, Circle, Triangle, Polygon
10. **Logic**: And, Or, Not, Xor, Nand, Nor
11. **Series/Products**: Sum, Product, summation, product
12. **Polynomials**: poly, factor, expand, gcd, lcm
13. **Printing**: latex, python, mathml, str, repr

### Data Formats

- Input: String expressions (e.g., "x**2 + 2*x + 1")
- Output: String representations (LaTeX by default)
- Options: Specify output format (latex, str, repr, python)

### Edge Cases

1. Invalid expressions raise SymPy errors with descriptive messages
2. Division by zero returns infinity (oo)
3. Unsolvable equations return empty set or condition
4. Complex expressions handled gracefully
5. Large expressions may timeout - provide timeout parameter

## Performance & Constraints

- Default timeout: 30 seconds per operation
- Max expression complexity: Configurable
- Use SymPy's evaluation flags (evaluate=True/False)
