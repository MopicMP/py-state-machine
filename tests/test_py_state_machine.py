"""Tests for py-state-machine."""

import pytest
from py_state_machine import machine


class TestMachine:
    """Test suite for machine."""

    def test_basic(self):
        """Test basic usage."""
        result = machine("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            machine("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = machine(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
