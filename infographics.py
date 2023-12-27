import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import numpy as np

#Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

#Selected countries for analysis
COUNTRY_NAMES = [
    "Togo","Afghanistan","Finland","Norway","Switzerland",
    ]

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


#Happiness Score Bar-graph for the years 2015 - 2020 

def barGraph(pivot_df):
	plt.figure(figsize=(10, 6))
	pivot_df.plot(kind='bar', width=0.8,  ax=plt.gca())
	plt.xlabel('Year')
	plt.ylabel('Happiness Index')
	plt.title('Happiness Index by Country for 2015 - 2020')
	plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
	plt.tight_layout()
	plt.show()
      

df_filtered_CPI = df_filtered[["Country","cpi_score","Year"]]
pivot_df_CPI = df_filtered_CPI.pivot(index='Year', columns='Country', values='cpi_score')

#CPI score for the years 2015 - 2020
def Hbar(pivot_df):
	pivot_df.plot(kind="barh")
	plt.xlabel('CPI Score')
	plt.ylabel('Year')
	plt.title('CPI Score by Country for 2015 - 2020')
	plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
	plt.show()


df_filtered_dystopia = df_filtered[["Country","dystopia_residual"]]

def PlotPie(pivot_df):
	plt.pie(pivot_df["dystopia_residual"],labels = pivot_df["Country"],autopct='%1.1f%%', startangle=140)
	plt.show()
	

df_filtered_Freedom = df_filtered[["Country","freedom","Year"]]
pivot_df_Freedom = df_filtered_Freedom.pivot(index='Year', columns='Country', values='freedom')


def plotLine(pivot_df):
	pivot_df.plot(kind="line")
	plt.show()

  	
barGraph(pivot_df_Hindex)
Hbar(pivot_df_CPI)
PlotPie(df_filtered_dystopia)
plotLine(pivot_df_Freedom)

