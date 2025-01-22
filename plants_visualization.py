"""
Description:
    This file will read the Plants.csv data set and generate visualizations.
    It is the homework 2 of class DS-5110.
Author: Ruobing Wang
Date: 01/22/2025
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_PATH = os.path.abspath('./data/') # file path, use abs path
FILENAME = 'Plants.csv' # file name
df = pd.read_csv(os.path.join(BASE_PATH, FILENAME))

IMAGE_DIR = os.path.abspath('./images/')
os.makedirs(IMAGE_DIR, exist_ok=True)

# 1. Histograms for each subset and combined data
plt.figure(figsize=(12, 12))
plt.suptitle("Leaf Dimensions", fontsize=16)

# Combined histogram for Leaf Length
plt.subplot(2, 2, 1)
sns.histplot(df, x="Leaf-Length (cm)", kde=False, bins=10, color='steelblue')
plt.title("All - Leaf Length")
plt.xlabel("Leaf Length (cm)")
plt.ylabel("Count")

# Histograms for each plant leaf legnth:
plants = df["Plant Name"].unique()

for i, plant in enumerate(plants, start=2):
    plt.subplot(2, 2, i)
    sns.histplot(df[df["Plant Name"] == plant], 
                 x="Leaf-Length (cm)", kde=False, bins=10, color='steelblue')
    plt.title(plant)
    plt.xlabel("Leaf Length (cm)")
    plt.ylabel("Count")

histogram_leaf_length_path = os.path.join(IMAGE_DIR, "leaf_dimensions_histograms_leaf_length.png")
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(histogram_leaf_length_path)
plt.close()

# Histograms for each plant leaf width:
# Combined histogram for Leaf Width
plt.figure(figsize=(12, 12))
plt.suptitle("Leaf Dimensions", fontsize=16)
plt.subplot(2, 2, 1)
sns.histplot(df, x="Leaf-Width (cm)", kde=False, bins=10, color='steelblue')
plt.title("All - Leaf Width")
plt.xlabel("Leaf Width (cm)")
plt.ylabel("Count")
for i, plant in enumerate(plants, start=2):
    plt.subplot(2, 2, i)
    sns.histplot(df[df["Plant Name"] == plant],
                 x="Leaf-Width (cm)", kde=False, bins=10, color='steelblue')
    plt.title(plant)
    plt.xlabel("Leaf Width (cm)")
    plt.ylabel("Count")

histogram_leaf_width_path = os.path.join(IMAGE_DIR, "leaf_dimensions_histograms_leaf_width.png")
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(histogram_leaf_width_path)
plt.close()

# 2 Boxplots
# 2.1 Boxplots for Leaf Length by Plant
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Plant Name", y="Leaf-Length (cm)", hue="Plant Name", palette="Set3")
plt.title("Boxplot of Leaf Length")
plt.xlabel("Plant Name")
plt.ylabel("Leaf Length (cm)")
boxplot_leaf_length_path = os.path.join(IMAGE_DIR, "leaf_length_boxplot.png")
plt.savefig(boxplot_leaf_length_path)
plt.close()

# 2.2 Boxplots for Leaf Width by Plant
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x="Plant Name", y="Leaf-Width (cm)", hue="Plant Name", palette="Set3")
plt.title("Boxplot of Leaf Width")
plt.xlabel("Plant Name")
plt.ylabel("Leaf Width (cm)")
boxplot_leaf_width_path = os.path.join(IMAGE_DIR, "leaf_width_boxplot.png")
plt.savefig(boxplot_leaf_width_path)
plt.close()

# 3. Scatter Plot for Leaf Width vs Leaf Length
plt.figure(figsize=(8, 6))

sns.scatterplot(data=df, x="Leaf-Width (cm)", 
                y="Leaf-Length (cm)", hue="Plant Name", style="Plant Name", s=100, palette="Set2")
plt.title("Scatter Plot: Leaf Width vs Length")
plt.xlabel("Leaf Width (cm)")
plt.ylabel("Leaf Length (cm)")
plt.legend(title="Plant Name")
scatter_plot = os.path.join(IMAGE_DIR, "scatter_plot.png")
plt.savefig(scatter_plot)
plt.close()
