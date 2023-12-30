import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.gridspec as gridspec

#Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

#Selected countries for analysis
COUNTRY_NAMES = [
    "Togo","Afghanistan","Finland","Norway","Switzerland",
    ]

YEARS = [2018,2019,2020]
year = 2020
width = 0.10

#Fucntion to read dataset
def readDataSet(path):
    df = pd.read_csv(path)
    cleaned_df = df.dropna()
    return cleaned_df

cleaned_df = readDataSet(dataset_Path)
df_filtered = cleaned_df[cleaned_df['Country'].isin(COUNTRY_NAMES)]

filetred_df_Hindex = df_filtered[["Country","happiness_score","Year"]]
pivot_df_Hindex = filetred_df_Hindex.pivot(index='Year', columns='Country', values='happiness_score')

df_filtered_CPI = df_filtered[["Country","cpi_score","Year"]]
pivot_df_CPI = df_filtered_CPI.pivot(index='Year', columns='Country', values='cpi_score')

df_filtered_dystopia = df_filtered[df_filtered['Year'] == 2020][["Country", "dystopia_residual"]]

df_filtered_Freedom = df_filtered[["Country","freedom","Year"]]
pivot_df_Freedom = df_filtered_Freedom.pivot(index='Year', columns='Country', values='freedom')

plt.figure(figsize=(12, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1], height_ratios=[1, 2])

# First subplot: Title space
plt.subplot(3, 2, 1)  # 6 rows, 2 columns, position 1
plt.text(0.7, 0.7, 'World Happiness Index 2015 - 2020', horizontalalignment='center', verticalalignment='center', fontsize=16, fontweight='bold')
plt.text(0.5, 0.5, '', horizontalalignment='center', verticalalignment='center', fontsize=8)

plt.axis('off')

# Second subplot: Happiness Index Bar Graph
plt.subplot(3, 2, 2)
pivot_df_Hindex.plot(kind='bar', width=0.8, ax=plt.gca())
plt.xlabel('Year')
plt.ylabel('Happiness Index')
plt.title('Happiness Index by Country for 2015 - 2020')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Third subplot: CPI Score Horizontal Bar Graph
plt.subplot(3, 2, 3)
pivot_df_CPI.plot(kind="barh", ax=plt.gca())
plt.xlabel('CPI Score')
plt.ylabel('Year')
plt.title('CPI Score by Country for 2015 - 2020')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Fourth subplot: Dystopia Residual Pie Chart
plt.subplot(3, 2, 4)
plt.pie(df_filtered_dystopia["dystopia_residual"], labels=df_filtered_dystopia["Country"], autopct='%1.1f%%', startangle=140)
plt.title('Dystopia Residual for 2020')

# Fifth subplot: Freedom Line Plot
plt.subplot(3, 2, 5)
pivot_df_Freedom.plot(kind="line", ax=plt.gca())
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout and save the figure
plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(wspace=0.8, hspace=0.6) 
plt.savefig('combined_plots.png', dpi=300)  # Save as PNG file with higher resolution (dpi)

plt.show()
