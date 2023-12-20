import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Path to original dataset
dataset_Path = "WorldHappiness_Corruption_2015_2020.csv"

#Selected countries for analysis
COUNTRY_NAMES = [
    "Burundi","Togo","Afghanistan","Finland","Norway","Switzerland","Luxembourg",
    "Ireland","Saudi Arabia", "Spain","Kyrgyzstan","Ghana","Tajikistan","Senegal"
]


#Fucntion to read dataset
def readDataSet(path):
    df = pd.read_csv(path)
    cleaned_df = df.dropna()
    return cleaned_df


cleaned_df = readDataSet(dataset_Path)
countries = cleaned_df[ (cleaned_df["Country"].isin(COUNTRY_NAMES)) & (cleaned_df["Year"]==2015)]

plt.bar(countries["Country"], countries["happiness_score"])
plt.xticks(rotation=45)
plt.show()
