import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#reading dataframe using pandas module
rdf=pd.read_csv("FuelConsumption (6).csv")
print(rdf.info())
#checking for any null values
rdf.isnull().any()
print(rdf)
#making a countplot
sns.set_style('whitegrid')
sns.set_context('talk')
sns.set_theme('notebook')
sns.countplot(rdf,x='FUELTYPE',color='blue',width=2)
plt.show()