"""Simulate convergence in a simple Solow model with Cobb-Douglas production."""
from __future__ import annotations

import argparse
from pathlib import Path


def simulate(alpha: float = 0.33, saving: float = 0.22, depreciation: float = 0.06,
             population_growth: float = 0.02, periods: int = 80) -> list[float]:
    k = 0.5
    path = [k]
    for _ in range(periods):
        output = k ** alpha
        k = (saving * output + (1 - depreciation) * k) / (1 + population_growth)
        path.append(k)
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()
    path = simulate()
    alpha, saving, depreciation, population_growth = 0.33, 0.22, 0.06, 0.02
    steady_state = (saving / (depreciation + population_growth)) ** (1 / (1 - alpha))
    print(f"initial_capital_per_worker={path[0]:.3f}")
    print(f"final_capital_per_worker={path[-1]:.3f}")
    print(f"steady_state_capital_per_worker={steady_state:.3f}")
    if not args.no_plot:
        import matplotlib.pyplot as plt
        output = Path("output/figures")
        output.mkdir(parents=True, exist_ok=True)
        fig, ax = plt.subplots(figsize=(6.2, 4.0))
        ax.plot(path, color="#0f4c5c", linewidth=2.2)
        ax.axhline(steady_state, color="#d1495b", linestyle="--", label="steady state")
        ax.set(xlabel="Period", ylabel="Capital per worker", title="A Solow transition")
        ax.grid(alpha=0.2)
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(output / "solow_transition.png", dpi=180)
        plt.close(fig)


if __name__ == "__main__":
    main()
