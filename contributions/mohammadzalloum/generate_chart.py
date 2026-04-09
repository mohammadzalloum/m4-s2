from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns


def generate_chart():
    data = pd.DataFrame(
        {
            "Books": [5922, 1874, 3404, 2728, 2574, 2122],
            "Clothing": [6800, 2378, 2988, 1186, 2110, 1816],
            "Electronics": [7713, 1319, 3944, 2225, 1699, 2212],
            "Food & Beverage": [3589, 906, 947, 497, 903, 768],
            "Home & Garden": [4870, 1224, 1670, 1800, 796, 1904],
            "Sports": [2544, 634, 1548, 946, 872, 862],
        },
        index=["Amman", "Aqaba", "Irbid", "Madaba", "Salt", "Zarqa"]
    )

    sns.set_theme(style="white")
    sns.set_palette("colorblind")

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.heatmap(
        data,
        annot=True,
        fmt=".0f",
        cmap="viridis",
        cbar_kws={"label": "Revenue (JOD)"},
        ax=ax
    )

    ax.set_title(
        "Amman leads revenue across most categories, especially Electronics",
        pad=12,
        fontsize=14
    )
    ax.set_xlabel("Category")
    ax.set_ylabel("City")

    plt.tight_layout()

    output_path = Path(__file__).resolve().parent / "chart.png"
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Chart saved to: {output_path}")


if __name__ == "__main__":
    generate_chart()