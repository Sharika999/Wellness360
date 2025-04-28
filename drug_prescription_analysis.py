# drug_prescription_analysis.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Visualization Functions
def plot_per_column_distribution(df, nGraphShown=10, nGraphPerRow=5):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]]
    nCol = df.shape[1]
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) // nGraphPerRow

    plt.figure(figsize=(6 * nGraphPerRow, 8 * nGraphRow))
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if not np.issubdtype(type(columnDf.iloc[0]), np.number):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation=90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix(df, graphWidth=15):
    df = df.dropna(axis='columns')  # Drop columns with NaNs
    df = df.select_dtypes(include=[np.number])  # Keep only numeric columns

    if df.shape[1] < 2:
        print("Not enough numeric columns for correlation matrix.")
        return

    corr = df.corr()
    plt.figure(figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    cax = plt.matshow(corr, fignum=1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(cax)
    plt.title('Correlation Matrix', fontsize=15)
    plt.show()


def plot_scatter_matrix(df, plotSize=10, textSize=10):
    df = df.select_dtypes(include=[np.number]).dropna(axis='columns')
    df = df.loc[:, df.nunique() > 1]
    columnNames = df.columns[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=(plotSize, plotSize), diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*np.triu_indices_from(ax, k=1)):
        ax[i, j].annotate(f'Corr = {corrs[i,j]:.3f}', (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show()

# Main script
if __name__ == '__main__':
    # Change this to your actual file path if not running on Kaggle
    file_path = './final.csv'

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit()

    df = pd.read_csv(file_path, nrows=1000)
    print(f'There are {df.shape[0]} rows and {df.shape[1]} columns\n')
    print(df.head())

    print("\nPlotting Distribution Graphs...")
    plot_per_column_distribution(df)

    print("\nPlotting Correlation Matrix...")
    plot_correlation_matrix(df)

    print("\nPlotting Scatter Matrix...")
    plot_scatter_matrix(df)
