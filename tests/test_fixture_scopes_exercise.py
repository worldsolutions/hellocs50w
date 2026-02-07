"""Mini exercise: practicing pytest fixture scopes.

Run:
    pytest -q tests/test_fixture_scopes_exercise.py -s

What to try:
1) Change `fresh_cart` scope to "module" and observe how one test affects another.
2) Keep `app_config` as module scope and avoid mutating it.
3) Compare setup counts to see why broader scopes can speed up tests.
"""

from __future__ import annotations

import pytest


setup_counts = {"function": 0, "module": 0, "session": 0}


@pytest.fixture(scope="function")
def fresh_cart() -> list[str]:
    """Fast, isolated fixture: new object for every test."""
    setup_counts["function"] += 1
    return []


@pytest.fixture(scope="module")
def app_config() -> dict[str, str]:
    """Shared fixture for this module: safe if treated as read-only."""
    setup_counts["module"] += 1
    return {"currency": "USD", "timezone": "UTC"}


@pytest.fixture(scope="session")
def session_token() -> str:
    """Very expensive setup in real life (auth, service boot, etc.)."""
    setup_counts["session"] += 1
    return "demo-token"


def test_cart_starts_empty(fresh_cart: list[str], app_config: dict[str, str], session_token: str) -> None:
    assert fresh_cart == []
    assert app_config["currency"] == "USD"
    assert session_token.startswith("demo")


def test_cart_is_isolated_per_test(fresh_cart: list[str]) -> None:
    fresh_cart.append("book")
    assert fresh_cart == ["book"]


def test_another_test_gets_new_cart(fresh_cart: list[str]) -> None:
    # This proves function scope isolation.
    assert fresh_cart == []


def test_setup_counts() -> None:
    # There are 3 tests above that request `fresh_cart`.
    assert setup_counts["function"] == 3
    # `app_config` and `session_token` are each created only once here.
    assert setup_counts["module"] == 1
    assert setup_counts["session"] == 1
