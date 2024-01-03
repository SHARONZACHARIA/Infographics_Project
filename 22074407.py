import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

# Selected countries for analysis
COUNTRY_NAMES = [
    "Togo", "Afghanistan", "Finland", "Norway", "Switzerland",
]

ColorMap = {
    "Togo": "#58508d",
    "Afghanistan": "#ff6361",
    "Finland": "#bc5090",
    "Norway": "#ffa600",
    "Switzerland": "#003f5c"
}

YEARS = [2018, 2019, 2020]
year = 2020
width = 0.10

# Function to read dataset
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
fig = plt.figure(figsize=(12, 12))
plt.subplots(2,2, figsize=(18,13))
fig.set_facecolor('#fceee9')

# Function to get color for country
def get_country_color(country):
    return ColorMap.get(country, '#000000')  # Default to black if not found

# First subplot: Title space
plt.subplot(3, 2, 1)  # 6 rows, 2 columns, position 1
plt.text(0.7, 0.7, 'World Happiness Index 2015 - 2020', horizontalalignment='center',
         verticalalignment='center', fontsize=16, fontweight='bold')
plt.axis('off')


# Create a single legend and adjust its position using bbox_to_anchor
handles = [plt.Line2D([0], [0], color=get_country_color(country), marker='o',
                      markersize=12, linestyle='', label=country) for country in COUNTRY_NAMES]
legend = plt.figlegend(handles=handles, labels=COUNTRY_NAMES, loc='center', ncol=5,
                       fontsize=8, bbox_to_anchor=(0.5, 0.35), bbox_transform=plt.gcf().transFigure)


# Second subplot: Happiness Index Bar Graph
plt.subplot(3, 2, 3)
pivot_df_Hindex.plot(kind='bar', width=0.8, ax=plt.gca(), color=[
                     get_country_color(country) for country in pivot_df_Hindex.columns])
plt.xlabel('Year', fontsize=12)
plt.ylabel('Happiness Index', fontsize=12)
plt.title('Happiness Index by Country for 2015 - 2020', fontsize=14)
plt.legend().remove()  # Remove individual legend

# Third subplot: CPI Score Horizontal Bar Graph
plt.subplot(3, 2, 4)
pivot_df_CPI.plot(kind="barh", ax=plt.gca(), color=[
                  get_country_color(country) for country in pivot_df_CPI.columns])
plt.xlabel('CPI Score', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.title('CPI Score and Happiness Index', fontsize=14)
plt.legend().remove()  # Remove individual legend

# Fourth subplot: Dystopia Residual Pie Chart
plt.subplot(3, 2, 5)
explode = [0.1 if i == 0 else 0 for i in range(
    len(df_filtered_dystopia["Country"]))]

plt.pie(
    df_filtered_dystopia["dystopia_residual"],
    labels=df_filtered_dystopia["Country"],
    # autopct='%1.1f%%',
    startangle=140,
    colors=[get_country_color(country)
            for country in df_filtered_dystopia["Country"]],
    explode=explode,
    shadow=True,
    wedgeprops={'width': 0.4},  # Set the width to create a donut chart
)

plt.title('Dystopia Residual for 2020', fontsize=14)
plt.legend().remove() # Remove individual legend
 
# Fifth subplot: Freedom Line Plot
plt.subplot(3, 2, 6)
plt.title('Freedom and Happiness Index', fontsize=14)
pivot_df_Freedom.plot(kind="line", ax=plt.gca(), color=[
                      get_country_color(country) for country in pivot_df_Freedom.columns])
plt.legend().remove()  # Remove individual legend



# Adjust layout and save the figure
plt.tight_layout(pad=4.0, h_pad=6.0, w_pad=2.0)
plt.subplots_adjust(wspace=0.8, hspace=0.6)

# Save the plot
plt.savefig('combined_plots.png', dpi=300,
            bbox_extra_artists=(legend,), bbox_inches='tight')
# Show the plots
plt.show()
