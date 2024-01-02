import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.colors import ListedColormap

# Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

# Selected countries for analysis
COUNTRY_NAMES = [
    "Togo", "Afghanistan", "Finland", "Norway", "Switzerland",
]

YEARS = [2018, 2019, 2020]
year = 2020
width = 0.10

# Fucntion to read dataset


def readDataSet(path):
    df = pd.read_csv(path)
    cleaned_df = df.dropna()
    return cleaned_df


cleaned_df = readDataSet(dataset_Path)
df_filtered = cleaned_df[cleaned_df['Country'].isin(COUNTRY_NAMES)]
filetred_df_Hindex = df_filtered[["Country", "happiness_score", "Year"]]
pivot_df_Hindex = filetred_df_Hindex.pivot(
    index='Year', columns='Country', values='happiness_score')
df_filtered_CPI = df_filtered[["Country", "cpi_score", "Year"]]
pivot_df_CPI = df_filtered_CPI.pivot(
    index='Year', columns='Country', values='cpi_score')
df_filtered_dystopia = df_filtered[df_filtered['Year'] == 2020][[
    "Country", "dystopia_residual"]]
df_filtered_Freedom = df_filtered[["Country", "freedom", "Year"]]
pivot_df_Freedom = df_filtered_Freedom.pivot(
    index='Year', columns='Country', values='freedom')


sns.set_style("whitegrid")
plt.figure(figsize=(12, 12))

# First subplot: Title space
plt.subplot(3, 2, 1)  # 6 rows, 2 columns, position 1
plt.text(0.7, 0.7, 'World Happiness Index 2015 - 2020', horizontalalignment='center',
         verticalalignment='center', fontsize=16, fontweight='bold')
plt.axis('off')

# Second subplot: Happiness Index Bar Graph
plt.subplot(3, 2, 3)
# Choose a colormap for better color contrast
pivot_df_Hindex.plot(kind='bar', width=0.8, ax=plt.gca(), colormap='viridis')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Happiness Index', fontsize=12)
plt.title('Happiness Index by Country for 2015 - 2020', fontsize=14)
plt.legend(title='Country', bbox_to_anchor=(
    1.05, 1), loc='upper left', fontsize=8)
# Third subplot: CPI Score Horizontal Bar Graph
plt.subplot(3, 2, 4)
# Adjust color for better contrast
pivot_df_CPI.plot(kind="barh", ax=plt.gca(), colormap='viridis')
plt.xlabel('CPI Score', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.title('CPI Score and Happiness Index', fontsize=14)
plt.legend(title='Country', bbox_to_anchor=(
    1.05, 1), loc='upper left', fontsize=8)

# Fourth subplot: Dystopia Residual Pie Chart
plt.subplot(3, 2, 5)
explode = [0.1 if i == 0 else 0 for i in range(
    len(df_filtered_dystopia["Country"]))]

# Create a 'viridis' colormap
colors = plt.cm.viridis(np.linspace(
    0, 1, len(df_filtered_dystopia["Country"])))

# Use the 'viridis' colors for the pie chart slices
plt.pie(
    df_filtered_dystopia["dystopia_residual"],
    labels=df_filtered_dystopia["Country"],
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    colors=colors,  # Set the colors based on 'viridis' colormap
    shadow=True,
)
plt.title('Dystopia Residual for 2020', fontsize=14)

# Fifth subplot: Freedom Line Plot
plt.subplot(3, 2, 6)
plt.title('Freedom and Happiness Index', fontsize=14)
# Choose a colormap for line plot
pivot_df_Freedom.plot(kind="line", ax=plt.gca(), colormap='Set2')
plt.legend(title='Country', bbox_to_anchor=(
    1.05, 1), loc='upper left', fontsize=8)

# Adjust layout and save the figure
plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(wspace=0.8, hspace=0.6)
plt.savefig('combined_plots.png', dpi=300)
# Show the plots
plt.show()
