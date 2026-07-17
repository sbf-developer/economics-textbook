"""A transparent difference-in-differences demonstration.

The data are simulated. The script illustrates the estimator and does not
establish that a real policy has a causal effect.
"""
from __future__ import annotations

import numpy as np


def ols_two_regressor(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Return OLS coefficients for a matrix that already includes a constant."""
    return np.linalg.solve(x.T @ x, x.T @ y)


def main() -> None:
    rng = np.random.default_rng(7)
    n_per_group = 80
    treated = np.repeat([0, 1], n_per_group)
    post = np.tile(np.repeat([0, 1], n_per_group // 2), 2)
    # A common time change, a group difference, and a treatment effect of 4.
    noise = rng.normal(0, 1, treated.size)
    outcome = 50 + 2 * treated + 3 * post + 4 * treated * post + noise
    x = np.column_stack([np.ones(treated.size), treated, post, treated * post])
    beta = ols_two_regressor(outcome, x)
    did = beta[3]
    print("coefficients: intercept treated post treated_x_post")
    print(" ".join(f"{value:.3f}" for value in beta))
    print(f"difference_in_differences={did:.3f}")
    print("Interpretation: under parallel trends and the other design assumptions,"
          " the interaction estimates the average treatment effect for the treated group.")


if __name__ == "__main__":
    main()
