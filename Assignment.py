# -*- coding: utf-8 -*-
"""
CO2 avoided emissions analysis by renewable energy source

Author: ekhram
Created: 2026-04-01
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


# -----------------------------
# Configuration
# -----------------------------
file_path = Path(r"C:/Vermeden_verbruik_fossiele_energie_en_CO_01042026_221330.csv")

Bron_selected = [
    "Windenergie op land",
    "Windenergie op zee",
    "Totaal zonne-energie",
    "Totaal aardwarmte en bodemenergie",
    "Bodemwarmte, totaal",
    "Totaal biomassa",
    "Totaal biogas",
    "Vloeibare biotransportbrandstof, totaal",
]

Bron_mapping = {
    "Windenergie op land": "Onshore Wind",
    "Windenergie op zee": "Offshore Wind",
    "Totaal zonne-energie": "Solar Energy (Total)",
    "Totaal aardwarmte en bodemenergie": "Geothermal and Ground Energy (Total)",
    "Bodemwarmte, totaal": "Ground Heat (Total)",
    "Totaal biomassa": "Biomass (Total)",
    "Totaal biogas": "Biogas (Total)",
    "Vloeibare biotransportbrandstof, totaal": "Liquid Biofuels (Transport, Total)",
}


# -----------------------------
# Data Loading & Cleaning
# -----------------------------
def load_and_clean_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep=";")

    # Drop unnecessary column
    df = df.drop(columns=["Energietoepassingen"], errors="ignore")

    # Rename columns
    df.columns = ["Source", "Year", "TJ", "kton"]

    # Clean Year column
    df["Year"] = (
        df["Year"]
        .astype(str)
        .str.replace("**", "", regex=False)
        .astype(int)
    )

    # Convert numeric columns
    df["TJ"] = pd.to_numeric(df["TJ"], errors="coerce")
    df["kton"] = pd.to_numeric(df["kton"], errors="coerce")

    return df


# -----------------------------
# Filtering & Transformation
# -----------------------------
def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["Source"].isin(Bron_selected)].copy()

    # Translate to English
    df["Source"] = df["Source"].replace(Bron_mapping)

    return df


# -----------------------------
# Plotting
# -----------------------------
def plot_stacked_bar(df: pd.DataFrame) -> None:

    sns.set_theme(style="whitegrid")
    
    df_pivot = (
        df.pivot_table(
            index="Year",
            columns="Source",
            values="kton",
            aggfunc="sum",
        )
        .fillna(0)
    )

    # Create figure with higher DPI
    fig, ax = plt.subplots(figsize=(10, 5), dpi=150)

    df_pivot.plot(
        kind="bar",
        stacked=True,
        ax=ax,
        colormap="rainbow",
        alpha=0.7
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Avoided CO$_2$ emissions (kton)")
    ax.set_title("CO$_2$ Emissions Avoided by Renewable Energy Source")
    
    # Rotate x-axis labels by 60 degrees
    plt.xticks(rotation=60)
    
    ax.legend(
        title="Energy source",
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )

    plt.tight_layout()
    plt.show()

# -----------------------------
# Main
# -----------------------------
def main():
    df = load_and_clean_data(file_path)
    df = prepare_data(df)
    plot_stacked_bar(df)


if __name__ == "__main__":
    main()










