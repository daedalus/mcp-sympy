"""Pytest configuration and fixtures."""

import pytest


@pytest.fixture
def sample_expression():
    """Sample expression for testing."""
    return "x**2 + 2*x + 1"


@pytest.fixture
def trig_expression():
    """Trigonometric expression."""
    return "sin(x)**2 + cos(x)**2"


@pytest.fixture
def matrix_string():
    """Sample matrix string."""
    return "Matrix([[1, 2], [3, 4]])"
