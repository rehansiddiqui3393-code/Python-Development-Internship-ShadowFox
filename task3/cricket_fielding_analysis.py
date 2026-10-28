"""
Task 3 (Advanced) - Cricket Fielding Analysis

Reads ball-by-ball fielding data (fielding_data.csv), calculates each player's
Performance Score (PS) using the formula given in the task, draws charts and
writes a short analysis report.

PS = (CP*WCP) + (GT*WGT) + (C*WC) + (DC*WDC) + (ST*WST) + (RO*WRO)
     + (MRO*WMRO) + (DH*WDH) + RS

Run:  python cricket_fielding_analysis.py
Needs: pip install pandas matplotlib
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "fielding_data.csv"
CHART_DIR = "charts"
REPORT_FILE = "analysis_report.md"

# ---------------------------------------------------------------- weights
WEIGHTS = {
    "CP": 1,    # Clean Picks
    "GT": 1,    # Good Throws
    "C": 3,     # Catches
    "DC": -3,   # Dropped Catches
    "ST": 3,    # Stumpings
    "RO": 3,    # Run Outs
    "MRO": -2,  # Missed Run Outs
    "DH": 2,    # Direct Hits
}
LABELS = {
    "CP": "Clean Picks", "GT": "Good Throws", "C": "Catches",
    "DC": "Dropped Catches", "ST": "Stumpings", "RO": "Run Outs",
    "MRO": "Missed Run Outs", "DH": "Direct Hits", "RS": "Runs Saved",
}


# ---------------------------------------------------------------- load
def load_data(path):
    df = pd.read_csv(path)
    df["Pick"] = df["Pick"].fillna("")
    df["Throw"] = df["Throw"].fillna("")
    df["Overcount"] = df["Overcount"].astype(int)
    return df


# ---------------------------------------------------------------- metrics
def build_matrix(df):
    """Count each action per player and compute the Performance Score."""
    rows = []
    for player, g in df.groupby("Player Name", sort=False):
        rec = {
            "Player": player,
            "CP": (g["Pick"] == "Clean Pick").sum(),
            "GT": (g["Throw"] == "Good Throw").sum(),
            "C": (g["Pick"] == "Catch").sum(),
            "DC": (g["Pick"] == "Dropped Catch").sum(),
            "ST": (g["Throw"] == "Stumping").sum(),
            "RO": (g["Throw"] == "Run Out").sum(),
            "MRO": (g["Throw"] == "Missed Run Out").sum(),
            "DH": (g["Throw"] == "Direct Hit").sum(),
            "RS": g["Runs"].sum(),
            "Fumbles": (g["Pick"] == "Fumble").sum(),
            "Bad Throws": (g["Throw"] == "Bad Throw").sum(),
        }
        rec["PS"] = sum(rec[k] * w for k, w in WEIGHTS.items()) + rec["RS"]
        rows.append(rec)
    return pd.DataFrame(rows).set_index("Player")


# ---------------------------------------------------------------- charts
def chart_scores(matrix):
    ordered = matrix.sort_values("PS", ascending=False)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    bars = ax.bar(ordered.index, ordered["PS"], color=["#4B2E83", "#7B5CC4", "#B79FE8"][: len(ordered)])
    ax.bar_label(bars, padding=3, fontweight="bold")
    ax.set_title("Fielding Performance Score by Player")
    ax.set_ylabel("Performance Score (PS)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{CHART_DIR}/1_performance_score.png", dpi=150)
    plt.close(fig)


def chart_breakdown(matrix):
    comp = pd.DataFrame({LABELS[k]: matrix[k] * w for k, w in WEIGHTS.items()})
    comp["Runs Saved"] = matrix["RS"]
    comp = comp.loc[:, (comp != 0).any()]
    fig, ax = plt.subplots(figsize=(9, 5))
    comp.plot(kind="bar", stacked=True, ax=ax, colormap="tab20", width=0.6)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Points Contributed by Each Fielding Action")
    ax.set_ylabel("Points")
    ax.set_xlabel("")
    plt.setp(ax.get_xticklabels(), rotation=0)
    ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{CHART_DIR}/2_points_breakdown.png", dpi=150)
    plt.close(fig)


def chart_runs_by_over(df):
    by_over = df.pivot_table(index="Overcount", columns="Player Name", values="Runs", aggfunc="sum", fill_value=0)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    by_over.plot(kind="bar", ax=ax, width=0.8)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("Runs Saved (+) / Conceded (-) by Over")
    ax.set_xlabel("Over")
    ax.set_ylabel("Runs")
    plt.setp(ax.get_xticklabels(), rotation=0)
    ax.legend(title="Player", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{CHART_DIR}/3_runs_by_over.png", dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------- report
def player_comments(row):
    strengths, improve = [], []
    if row["C"] > 0: strengths.append(f"{row['C']} catch(es) taken")
    for key, name in (("RO", "run out(s)"), ("ST", "stumping(s)"), ("DH", "direct hit(s)")):
        if row[key] > 0:
            strengths.append(f"{row[key]} {name}")
    if row["RS"] > 0: strengths.append(f"saved {row['RS']} net run(s)")
    if row["CP"] >= 5: strengths.append(f"{row['CP']} clean pick-ups (reliable ground fielding)")
    if row["DC"] > 0: improve.append(f"dropped {row['DC']} catch(es), each costing 3 points")
    if row["MRO"] > 0: improve.append(f"missed {row['MRO']} run-out chance(s)")
    if row["Fumbles"] > 0: improve.append(f"{row['Fumbles']} fumble(s) at the ball")
    if row["Bad Throws"] > 0: improve.append(f"{row['Bad Throws']} bad throw(s)")
    if row["RS"] < 0: improve.append(f"conceded {abs(row['RS'])} net run(s)")
    return strengths or ["no standout actions"], improve or ["no major weaknesses recorded"]


def write_report(df, matrix):
    ranked = matrix.sort_values("PS", ascending=False)
    match = df["Match No."].iloc[0]
    venue = df["Venue"].iloc[0]
    team = df["Team"].iloc[0]
    total_saved = int(df.loc[df["Runs"] > 0, "Runs"].sum())
    total_conceded = int(-df.loc[df["Runs"] < 0, "Runs"].sum())
    best_over = df.groupby("Overcount")["Runs"].sum().idxmax()
    worst_over = df.groupby("Overcount")["Runs"].sum().idxmin()

    L = []
    L.append("# Cricket Fielding Analysis Report\n")
    L.append(f"**Match:** {match}  |  **Fielding team:** {team}  |  **Venue:** {venue}  |  "
             f"**Fielding actions recorded:** {len(df)}\n")
    L.append("## 1. Performance Matrix\n")
    L.append("| Player | CP | GT | C | DC | ST | RO | MRO | DH | RS | **PS** |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for p, r in matrix.iterrows():
        L.append(f"| {p} | {r.CP} | {r.GT} | {r.C} | {r.DC} | {r.ST} | {r.RO} | {r.MRO} | {r.DH} | {r.RS} | **{r.PS}** |")
    L.append("\nWeights: CP +1, GT +1, C +3, DC -3, ST +3, RO +3, MRO -2, DH +2, RS added as it is.\n")
    L.append("## 2. Ranking\n")
    for i, (p, r) in enumerate(ranked.iterrows(), 1):
        L.append(f"{i}. **{p}** - {r.PS} points")
    L.append("\n![Performance Score](charts/1_performance_score.png)\n")
    L.append("## 3. Player-wise Analysis\n")
    for p, r in ranked.iterrows():
        s, i = player_comments(r)
        L.append(f"### {p} (PS = {r.PS})")
        L.append("- **Strengths:** " + "; ".join(s))
        L.append("- **Areas to improve:** " + "; ".join(i) + "\n")
    L.append("![Points breakdown](charts/2_points_breakdown.png)\n")
    L.append("## 4. Team Impact\n")
    L.append(f"- Runs saved through good fielding: **{total_saved}**")
    L.append(f"- Runs conceded through poor fielding: **{total_conceded}**")
    L.append(f"- Net effect on the team: **{total_saved - total_conceded:+d} runs**")
    L.append(f"- Best fielding over: **over {best_over}**; weakest over: **over {worst_over}**\n")
    L.append("![Runs by over](charts/3_runs_by_over.png)\n")
    L.append("## 5. Conclusion\n")
    best, worst = ranked.index[0], ranked.index[-1]
    L.append(f"{best} made the biggest contribution to the team's fielding, while {worst} scored lowest "
             f"and has the most room to improve. Cutting dropped catches and missed run-outs gives the "
             f"largest gain, because those actions carry the heaviest penalties (-3 and -2).\n")
    L.append("> Note: the rows in `fielding_data.csv` are sample entries. Replace them with real match "
             "data and re-run the script to update every chart and number.\n")
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


# ---------------------------------------------------------------- main
if __name__ == "__main__":
    os.makedirs(CHART_DIR, exist_ok=True)
    data = load_data(DATA_FILE)
    matrix = build_matrix(data)
    print("Performance Matrix")
    print(matrix[["CP", "GT", "C", "DC", "ST", "RO", "MRO", "DH", "RS", "PS"]])
    chart_scores(matrix)
    chart_breakdown(matrix)
    chart_runs_by_over(data)
    write_report(data, matrix)
    matrix.to_csv("performance_matrix.csv")
    print("\nCharts saved in 'charts/', report saved as", REPORT_FILE)
