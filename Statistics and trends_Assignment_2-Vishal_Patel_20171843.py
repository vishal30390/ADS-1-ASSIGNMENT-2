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

# Creating new dataframe by slicing/filtering the Indicatior column with Electric power consumption
df7 = df[df['Indicator Name'].isin(['Electric power consumption (kWh per capita)'])].reset_index(drop=True)
df8 = df7[df7['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df9 = df8.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df9 = df9.drop(df9.index[1]) #Droping the first Index
df9.reindex([1,0]) #Reindexing
df9.columns=df9.iloc[0] #Replcaing the header
df9.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df9 = df9.drop(df9.index[0]) #Droping the Index
df9 = df9.reset_index(drop=True) #Resetiing the index
df9['Year'] = pd.to_numeric(df9['Year']) #Converting the column in to numeric
df9 = df9[df9['Year']>= 2000]
df9 = df9.reset_index(drop=True)
df9[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df9[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric)
print(df9.describe()) #Provide Statistical Overview
df9.to_excel('Electric power consumption (kWh per capita).xlsx') #Creating the excelfile of the dataset
#Creating First Line Graph of the Electric Power Consuption of the countries
plt.figure(figsize=(11,10)) #To Create figure
df9.plot(x ='Year',y = ['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],rot = '45',figsize = [13,7],) # Plot the Line Grapgh
plt.xlabel("Year",fontsize=20) #Setting the X lable of the grap
plt.ylabel("Electric power consumption (kWh per capita)",fontsize=20) #Setting the Y lable of the Gragh
plt.title("Electric power consumption",size=25) #Setting the title of the Graph
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size': 18}) #For getting legend out side the graph
plt.grid(True) #To show grid in Plot
plt.xticks(fontsize=20) #Changin the xtick size
plt.yticks(fontsize=20) #Changin the xtick size
plt.xlim(2000,2014) #limit the x values
plt.savefig("Electric_Power_consuption.jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show() #To show the plot

# Creating new dataframe by slicing/filtering the Indicatior column with Renewable energy consumption (% of total final energy consumption
df10 = df[df['Indicator Name'].isin(['Renewable energy consumption (% of total final energy consumption)'])].reset_index(drop=True)
df11 = df10[df10['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df12 = df11.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df12 = df12.drop(df12.index[1]) #Droping the first Index
df12.reindex([1,0]) #Reindexing
df12.columns=df12.iloc[0] #Replcaing the header
df12.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df12 = df12.drop(df12.index[0]) #Droping the Index
df12 = df12.reset_index(drop=True) #Resetiing the index
df12[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df12[["Year","China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric) #Converting the column in to numeric #Converting the column in to numeric
df12 = df12[df12['Year']>= 2000]
df12 = df12.reset_index(drop=True)
#df12[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df12[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric)
print(df12.describe()) #Provide Statistical Overview
df12 = df12.dropna() #Drop Na Value
df12.to_excel('Renewable energy consumption (% of total final energy consumption).xlsx') #Creating the excelfile of the dataset
#Creating Second Line Graph of the Electric Power Consuption of the countries
plt.figure(figsize=(11,10)) #To Create figure
df12.plot(x ='Year',y = ['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],rot = '45',figsize = [13,7]) # Plot the Line Grapgh
plt.xlabel("Year",fontsize=20) #Setting the X lable of the grap
plt.ylabel("Renewable energy consumption(%)",fontsize=20) #Setting the Y lable of the Gragh
plt.title("Renewable energy consumption",size=25) #Setting the title of the Graph
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left',prop={'size': 18}) #For getting legend out side the graph
plt.grid(True) #To show grid in Plot
plt.xticks(fontsize=20) #Changin the xtick size
plt.yticks(fontsize=20) #Changin the xtick size
plt.xlim(2000,2014) #limit the x values
plt.savefig("Renewable energy consumption.jpeg",dpi=300) #Save the plot Image in JPEG formate
plt.show() #To show the plot

#Creating new dataframe by slicing/filtering the Indicatior column with Required indicator
df13 = df[df['Indicator Name'].isin(['Forest area (sq. km)','Agricultural land (sq. km)'])].reset_index(drop=True)
df14 = df13[df13['Country Name'].isin(['India'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df15 = df14.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df15 = df15.drop(df15.index[1]) #Droping the first Index
df15.reindex([1,0]) #Reindexing
df15.columns=df15.iloc[0] #Replcaing the header
df15.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Rename the column Name
df15.columns = ['Year','Forest area','Agricultural land']
df15 = df15.drop(df15.index[0]) #Droping the Index
df15 = df15.reset_index(drop=True) #Resetiing the index
print(df15.describe()) # Provide Statistical Overview
df15[["Year","Forest area","Agricultural land"]] = df15[["Year","Forest area","Agricultural land"]].apply(pd.to_numeric) #Converting the column in to numeric
df15 = df15[df15['Year']>= 2011] #Selecting the data from 2011
#df15.drop(["Year"],axis=1,inplace=True)
df15 = df15.reset_index(drop=True) #Resetting the index
df15[["Forest area","Agricultural land"]] = df15[["Forest area","Agricultural land"]].apply(pd.to_numeric)
df15.to_excel('India_Dataframe.xlsx') #Creating the excelfile of the dataset
#Creating new dataframe by filtering the Indicatior column with Required indicator
df16 = df[df['Indicator Name'].isin(['Forest area (sq. km)','Agricultural land (sq. km)'])].reset_index(drop=True)
df17 = df16[df16['Country Name'].isin(['Brazil'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df18 = df17.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df18 = df18.drop(df18.index[1]) #Droping the first Index
df18.reindex([1,0]) #Reindexing
df18.columns=df18.iloc[0] #Replcaing the header
df18.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df18.columns = ['Year','Forest area','Agricultural land']
df18 = df18.drop(df18.index[0]) #Droping the Index
df18 = df18.reset_index(drop=True) #Resetiing the index
print(df18.describe()) # Provide Statistical Overview
df18[["Year","Forest area","Agricultural land"]] = df18[["Year","Forest area","Agricultural land"]].apply(pd.to_numeric) #Converting the column in to numeric
df18 = df18[df18['Year']>= 2011] #Selecting the data from 2011
#df15.drop(["Year"],axis=1,inplace=True)
df18 = df18.reset_index(drop=True) #Resetting the index
df18[["Forest area","Agricultural land"]] = df18[["Forest area","Agricultural land"]].apply(pd.to_numeric)
df18.to_excel('Aus_Dataframe.xlsx') #Creating the excelfile of the dataset
# Ploting the subplots 
plt.figure(figsize=(35,26)) 
plt.suptitle("Forest area Vs Agricultural Land in India and Brazil", fontsize=50) #To generate the subplot title
plt.subplot(2,2,1) #To create first plot of subplot
plt.plot(df15["Year"], df15["Forest area"],color='red', label="Forest area")
plt.xlabel("Year",fontsize=35) #To create x label
plt.ylabel("Forest area (sq. km)",fontsize=45) #To create y label
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.grid(True)
plt.title("Forest Area-India",fontsize=45) #To provide the title to first plot
plt.legend(prop={'size': 45}) #To create first plot of subplot
plt.subplot(2,2,2) #To create second plot of subplot.
plt.plot(df15["Year"], df15["Agricultural land"],color='green', label="Agricultural Land")
plt.xlabel("Year",fontsize=35) #To create x label  
plt.ylabel("Agricultural land (sq. km)",fontsize=35) #To create y label
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.grid(True) #To create grid
plt.title("Agricultural land-Indai",fontsize=45) #To provide the title to second plot
plt.legend(prop={'size': 45}) #To create legend
plt.subplot(2,2,3) #To create first plot of subplot
plt.plot(df18["Year"], df18["Forest area"],color='red', label="Forest area")
plt.xlabel("Year",fontsize=35)
plt.ylabel("Forest area (sq. km)",fontsize=45)
plt.grid(True)#To create grid
plt.title("Forest area-Brazil",fontsize=45) #To provide the title to first plot
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.legend(prop={'size': 45})
plt.subplot(2,2,4) #To create second plot of subplot.
plt.plot(df18["Year"], df18["Agricultural land"],color='green', label="Agricultural Land")
plt.xlabel("Year",fontsize=35)  
plt.ylabel("Agricultural land (sq. km)",fontsize=35)
plt.grid(True)
plt.title("Agricultiral land-Brazil",fontsize=45) #To provide the title to second plot
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.legend(prop={'size': 45})
plt.show() #To show the plot

#Creating new dataframe by slicing/filtering the Indicatior column with Community health workers
df19 = df[df['Indicator Name'].isin(['Community health workers (per 1,000 people)'])].reset_index(drop=True)
df20 = df19[df19['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df21 = df20.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df21 = df21.drop(df21.index[1]) #Droping the first Index
df21.reindex([1,0]) #Reindexing
df21.columns=df21.iloc[0] #Replcaing the header
df21.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df21 = df21.drop(df21.index[0]) #Droping the Index
df21 = df21.reset_index(drop=True) #Resetiing the index
df21['Year'] = pd.to_numeric(df21['Year']) #Converting the column in to numeric
df21 = df21[df21['Year']>= 2011]
df21 = df21.reset_index(drop=True)
df21[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]] = df2[["China","India","United States","Australia","Brazil","Nigeria","Germany","United Kingdom"]].apply(pd.to_numeric)
print(df21.describe()) #Provide Statistical Overview
df21.to_excel('Community health workers (per 1,000 people).xlsx') #Creating the excelfile of the dataset
df22 = df21.sum()# Sum of All Column and Print
print(df22)
column_Name = {'Countries':['China','India','United States','Australia','Brazil','Nigeria','Germany','United Kingdom'],'Community health workers':[2.283630e+08,1.949700e+09,8.638333e+09,6.965366e+08,5.969760e+08,4.846143e+09,1.001720e+09,2.905083e+09]}
df23 = pd.DataFrame(column_Name)
print(df23)
# Ploting the subplots 
plt.figure(figsize=(23,9)) #Creating the figure
plt.suptitle("Urban Population VS Community health workers (per 1,000 people)", fontsize=32) #To generate the subplot title
plt.subplot(1,2,1) #To create first plot of subplot
plt.pie(df_mean['Mean of UrbanPopulation'],labels=df_mean['Countries'],rotatelabels=False,autopct='%1.0f%%',shadow=False,labeldistance=1.01,radius=1.2,pctdistance=0.7,textprops = {"fontsize":25}) #Generating the first pie chart
plt.title("Urban Population",loc="center",fontsize=30) #To provide the title 
plt.subplot(1,2,2) #To create first plot of subplot
plt.pie(df23['Community health workers'],labels=df23['Countries'],rotatelabels=False,autopct='%1.0f%%',shadow=False,labeldistance=1.01,radius=1.2,pctdistance=0.7,textprops = {"fontsize":25}) #Generating the second pie chart
plt.title("Community health workers",loc="center",fontsize=30) #To provide the title to first plot
#plt.legend(prop={'size': 25}) #To show the legend
plt.show() #To show the plot
