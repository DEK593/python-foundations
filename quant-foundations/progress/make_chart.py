"""Build the progress chart from attempts.csv (first-try accuracy per study day)."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent

SURFACE = "#1a1a19"
INK = "#f0efec"
MUTED = "#898781"
GRID = "#2c2c2a"
AXIS = "#383835"
BAR = "#3987e5"


def main() -> None:
    df = pd.read_csv(HERE / "attempts.csv", parse_dates=["date"])
    daily = df.groupby("date").agg(
        attempts=("first_try", "size"),
        correct=("first_try", lambda s: (s == "correct").sum()),
    )
    daily["pct"] = daily["correct"] / daily["attempts"] * 100
    labels = daily.index.strftime("%d %b")

    fig, ax = plt.subplots(figsize=(8, 3.6), dpi=150)
    fig.patch.set_facecolor(SURFACE)
    ax.set_facecolor(SURFACE)

    bars = ax.bar(labels, daily["pct"], width=0.55, color=BAR, zorder=3)
    for bar, (_, row) in zip(bars, daily.iterrows()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
                f"{row.pct:.0f}%  ({int(row.correct)}/{int(row.attempts)})",
                ha="center", va="bottom", color=INK, fontsize=8)

    ax.set_ylim(0, 110)
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels([f"{t}%" for t in [0, 25, 50, 75, 100]])
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.tick_params(colors=MUTED, labelsize=8, length=0)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.set_title("First-try accuracy on spaced-repetition reviews",
                 color=INK, fontsize=10, loc="left", pad=12)

    fig.tight_layout()
    fig.savefig(HERE / "accuracy.png", facecolor=SURFACE)


if __name__ == "__main__":
    main()
