# Importing All the Python Inbuit Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("World_Bankdata_Climate_change.xls",header=[3]) #Reading the world bank climate chaange excel file
print(df.head(5)) #Print first five row of the dataset
print(df.tail(5)) #Print last five row of the data set
df.drop(['Country Code','Indicator Code'],axis=1,inplace=True) #Droping the unnecessaary columns of data set.
print(df.columns) #Read the header

#Creating new dataframe by slicing/filtering the Indicatior column with urban Population Indicator
df1 = df[df['Indicator Name'].isin(['Urban population'])].reset_index(drop=True)
df1 = df1[df1['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df2 = df1.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df2 = df2.drop(df1.index[1]) #Droping the first Index
df2.reindex([1,0]) #Reindexing
df2.columns=df2.iloc[0] #Replcaing the header
df2.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df2 = df2.drop(df1.index[0]) #Droping the Index
df2 = df2.reset_index(drop=True) #Resetiing the index
df2[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df2[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric) #Converting the column in to numeric
df2 = df2[df2['Year']>= 2011]
df2 = df2.reset_index(drop=True)
#df2[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df2[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric)
print(df2.describe()) #Provide Statistical Overview
df2.to_excel('Urban_Population_Dataframe.xlsx') #Creating the excelfile of the dataset of Urban_Population Indicaator
print(df2) #Print Dataframe
df_mean = {'Countries':['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],'Mean of UrbanPopulation':[785302955.454545,440558444.090909,264098482.090909,20760276.3636364,177245447.181818,91065416.1818182,63321506.4545455,54270550]}
df_mean = pd.DataFrame(df_mean)
print(df_mean)
#Creating First Bar Graph of the Urban population of the countries
plt.figure(figsize=(25,10)) #To Create figure
df2.plot.bar(x ='Year',y = ['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],rot = '45',width = 0.8 ,figsize = [13,7],edgecolor = "black") # Plot the Line Grapgh
plt.xlabel("Year",fontsize=22) #Setting the X lable of the grap
plt.ylabel("Urban population",fontsize=22) #Setting the Y lable of the Gragh
plt.title("Urban population",size=25) #Setting the title of the Graph
plt.legend(bbox_to_anchor=(1.0,1.0),prop={'size': 18}) #For getting legend out side the graph
plt.xticks(fontsize=20) #Changin the xtick size
plt.yticks(fontsize=20) #Changin the xtick size
plt.grid(True) #To show grid in Plot
plt.savefig("Urban population.jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show() #To show the plot

#Creating new dataframe by slicing/filtering the Indicatior column with Co2 Emmission
df3 = df[df['Indicator Name'].isin(['CO2 emissions (kt)'])].reset_index(drop=True)
df3 = df3[df3['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df4 = df3.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df4 = df4.drop(df4.index[1]) #Droping the first Index
df4.reindex([1,0]) #Reindexing
df4.columns=df4.iloc[0] #Replcaing the header
df4.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df4 = df4.drop(df4.index[0]) # Droping the Index
df4 = df4.reset_index(drop=True) #Resetiing the index
print(df4.describe()) #Provide Statistical Overview
df4[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df4[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric) #Converting the column in to numeric
df4 = df4[df4['Year']>= 2011]
df4 = df4.reset_index(drop=True)
df4[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df4[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric)
print(df4.describe()) #Provide Statistical Overview
df4 = df4.fillna(df4.median()) #Filling Empty Data with median
print(df4) #Print Dataframe
df4.to_excel('CO2_Emmision_Dataframe.xlsx') #Creating the excelfile of the dataset of Co2 emmision
#Creating Second Bar Graph of the CO2 emissions (kt) Indicator
plt.figure(figsize=(25,10)) #To Create figure
df4.plot.bar(x ='Year',y = ['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],rot = '45',width = 0.8 ,figsize = [13,7],edgecolor = "black") # Plot the Line Grapgh
plt.xlabel("Year",fontsize=22) #Setting the X lable of the grap
plt.ylabel("CO2 emissions",fontsize=22) #Setting the Y lable of the gragh
plt.title("CO2 emissions (kt)",size=25) #Setting the title of the Graph
plt.legend(bbox_to_anchor=(1.0,1.0),prop={'size': 18}) #For getting legend out side the graph
plt.xticks(fontsize=20) #Changin the xtick size
plt.yticks(fontsize=20) #Changin the xtick size
#plt.rc('ytick',labelsize=15) #Changin the ytick size
plt.grid(True) #To show grid in Plot
plt.savefig("CO2 emissions (kt).jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show() #To show the plot

#Creating new dataframe by slicing/filtering the Indicatior column with selected Indicator
df5 = df[df['Indicator Name'].isin(['Urban population','CO2 emissions (kt)','Electric power consumption (kWh per capita)','Forest area (sq. km)','Agricultural land (sq. km)','Renewable energy consumption (% of total final energy consumption)','Community health workers (per 1,000 people)'])].reset_index(drop=True)
df5 = df5[df5['Country Name'].isin(['India'])].reset_index(drop=True) #Filtering the Country from Country Name Column
df6 = df5.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df6 = df6.drop(df6.index[1]) #Droping the first Index
df6.reindex([1,0]) #Reindexing
df6.columns=df6.iloc[0] #Replcaing the header
df6.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df6.columns = ['Year','Urban population','CO2 Emissions','Ele. power consumption','Forest area','Agricultural land','Renewable energy con.','Comm.health workers']
df6 = df6.drop(df6.index[0]) #Droping the Index
df6 = df6.reset_index(drop=True) #Resetiing the index
print(df6.describe()) # Provide Statistical Overview
df6['Year'] = pd.to_numeric(df6['Year']) #Converting the column in to numeric
df6 = df6[df6['Year']>= 2011] #Selecting the data from 2011
df6.drop(["Year"],axis=1,inplace=True)
df6 = df6.reset_index(drop=True) #Resetting the index
df6[['Urban population','CO2 Emissions','Ele. power consumption','Ele. power consumption','Forest area','Agricultural land','Renewable energy con.','Comm.health workers']]=np.float64(df6[['Urban population','CO2 Emissions','Ele. power consumption','Ele. power consumption','Forest area','Agricultural land','Renewable energy con.','Comm.health workers']])
df6.to_excel('India_Indicaators.xlsx') #Creating the excelfile of the dataset
print(df6.corr())
plt.figure(figsize=(30,20)) #To Create figure
plot = sns.heatmap(df6.corr(),vmin=-1, vmax=1, annot=True, linewidth=1, linecolor='black', annot_kws={"size":40}) #To Create Heatmap
plot.set_xticklabels(plot.get_xticklabels(), rotation=90, horizontalalignment='right',fontsize=45)
plot.set_yticklabels(plot.get_yticklabels(), rotation=0, horizontalalignment='right',fontsize=45)
plt.title('Heat MAP of India',size=50)
plt.savefig("Heat map.jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show()
