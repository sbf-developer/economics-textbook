"""Numerical supply-demand example used in Chapter 3.

The model is deliberately linear. It is a teaching calculation, not a
claim that any real market has linear curves or a single stable equilibrium.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def equilibrium(a: float, b: float, c: float, d: float) -> tuple[float, float]:
    """Return price and quantity for Qd=a-bP and Qs=c+dP."""
    price = (a - c) / (b + d)
    quantity = a - b * price
    return price, quantity


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-plot", action="store_true")
    args = parser.parse_args()

    a, b, c, d = 120.0, 2.0, 20.0, 1.0
    price, quantity = equilibrium(a, b, c, d)
    consumer_surplus = 0.5 * quantity * (a / b - price)
    producer_surplus = 0.5 * quantity * (price - (-c / d))
    print(f"equilibrium_price={price:.2f}")
    print(f"equilibrium_quantity={quantity:.2f}")
    print(f"consumer_surplus={consumer_surplus:.2f}")
    print(f"producer_surplus={producer_surplus:.2f}")

    if not args.no_plot:
        import matplotlib.pyplot as plt
        import numpy as np

        output = Path("output/figures")
        output.mkdir(parents=True, exist_ok=True)
        q = np.linspace(0, 125, 300)
        demand_price = (a - q) / b
        supply_price = (q - c) / d
        fig, ax = plt.subplots(figsize=(6.2, 4.0))
        ax.plot(q, demand_price, label="Demand", color="#0f4c5c", linewidth=2.2)
        ax.plot(q, supply_price, label="Supply", color="#d1495b", linewidth=2.2)
        ax.scatter([quantity], [price], color="#1b1f24", zorder=3)
        ax.annotate("equilibrium", (quantity, price), xytext=(quantity + 8, price + 8),
                    arrowprops={"arrowstyle": "-", "color": "#1b1f24"})
        ax.set(xlabel="Quantity", ylabel="Price", title="A linear market model")
        ax.set_ylim(bottom=0)
        ax.grid(alpha=0.2)
        ax.legend(frameon=False)
        fig.tight_layout()
        fig.savefig(output / "supply_demand.png", dpi=180)
        plt.close(fig)


if __name__ == "__main__":
    main()
