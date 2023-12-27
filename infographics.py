import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import numpy as np

#Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

#Selected countries for analysis
COUNTRY_NAMES = [
    "Burundi","Togo","Afghanistan","Finland","Norway","Switzerland","Luxembourg",
    "Ireland","Saudi Arabia", "Spain","Kyrgyzstan","Ghana","Tajikistan","Senegal"
    ]

year = 2020
width = 0.10

#Fucntion to read dataset
def readDataSet(path):
    df = pd.read_csv(path)
    cleaned_df = df.dropna()
    return cleaned_df


cleaned_df = readDataSet(dataset_Path)

countries_2020 =  cleaned_df[["Country","happiness_score"]][cleaned_df["Year"]==2020].head(5)
countries_2019 =  cleaned_df[["Country","happiness_score"]][cleaned_df["Year"]==2019].head(5)
countries_2018 =  cleaned_df[["Country","happiness_score"]][cleaned_df["Year"]==2018].head(5)

print(countries_2020)

#Happiness score Bar graph for the year 2020
def barGraph(c2020,c2019,c2018):
    x = np.arange(5)
    width = 0.2
    plt.bar(x - 0.2,c2020, width, color = 'cyan')
    plt.bar(x,c2019, width, color='green')
    plt.bar(x + 0.2 ,c2018,width, color='orange')
    plt.show()
  
barGraph(countries_2020,countries_2019,countries_2018)


