# Importing All the Python Inbuit Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Read(file): #Define the function to read the excel file
    dataframe=pd.read_excel(file,header=[3]) #To read the excel file with coustomise header
    print(dataframe) #Print the dataframe
    return dataframe #Return the function

df_wb = Read("World_Bankdata_Climate_change.xls") #Calling the function with argument to read file

df_wb.drop(['Country Code','Indicator Code'],axis=1,inplace=True) #Droping the unnecessaary columns of data set.
print(df_wb.columns) #Read the header
country = ['China','India','United States','Australia','Brazil','Nigeria',
           'Germany','United Kingdom'] #define country variable
#Creating new dataframe by slicing/filtering the Indicatior column with urban Population Indicator
df1 = df_wb[df_wb['Indicator Name'].isin(['Urban population'])].reset_index(drop=True)
df1 = df1[df1['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany',
                                   'United Kingdom'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df2 = df1.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df2 = df2.drop(df1.index[1]) #Droping the first Index
df2.reindex([1,0]) #Reindexing
df2 = df2.rename(columns=df2.iloc[0]) #Rename the index
df2.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Rename the column Name
df2 = df2.drop(df1.index[0]).reset_index(drop=True) #Droping the Index
df2 = df2.astype(int) #Convert data into float
df2 = df2[df2['Year']>= 2011].reset_index(drop=True) #Selecting the year 2011 and above
print(df2) #Print Dataframe
print(df2.describe()) #Provide Statistical Overview
print(df2.iloc[:, 1:9].mean()) #Finding mean of all column
df2.to_excel('Urban_Population_Dataframe.xlsx') #Creating the excelfile of the dataset of Urban_Population Indicaator
#Creating new dataframe by slicing/filtering the Indicatior column with Co2 Emmission
df3 = df_wb[df_wb['Indicator Name'].isin(['CO2 emissions (kt)'])].reset_index(drop=True)
df3 = df3[df3['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany',
                                    'United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df4 = df3.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df4 = df4.drop(df4.index[1]) #Droping the first Index
df4.reindex([1,0]) #Reindexing
df4 = df4.rename(columns=df4.iloc[0]) #Rename the index
df4.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df4 = df4.drop(df4.index[0]).reset_index(drop=True) # Droping the Index
print(df4.describe()) #Provide Statistical Overview
df4 = df4.fillna(df4.median()) #Filling Empty Data with median
df4 = df4.astype(float) #Converting data in to float
df4 = df4[(df4['Year']>= 2011) & (df4['Year']<= 2019)].reset_index(drop=True) #Selecting the year between 2011 and 2019
print(df4.describe()) #Provide Statistical Overview
print(df4) #Print Dataframe
df4.to_excel('CO2_Emmision_Dataframe.xlsx') #Creating the excelfile of the dataset of Co2 emmision

def barplot(df,types,values, xlabel, ylabel, title): #Define a function to create bargraph
    #plt.figure(figsize=(25,10)) #To create figure size
    df.plot(kind=types,x=values,rot='45',width=0.8,figsize=[13,7],edgecolor="black",grid=1) #to Plot the graph
    plt.title(title,size=25) #To give the title 
    plt.xlabel(xlabel,fontsize=22) #To provide x label
    plt.ylabel(ylabel,fontsize=22) #To provide y label
    plt.legend(bbox_to_anchor=(1.0,1.0),prop={'size': 18}) #To set the legend 
    plt.xticks(fontsize=20) #Changin the xtick size
    plt.yticks(fontsize=20) #Changin the xtick size
    plt.show()
    
barplot(df2,"bar","Year","Year","Urban population", "Urban population") #calling the function with arguments    
barplot(df4,"bar","Year","Year","CO2 emissions", "CO2 emissions (kt)") #calling the function with arguments

#Creating new dataframe by slicing/filtering the Indicatior column with selected Indicator
df5 = df_wb[df_wb['Indicator Name'].isin(['Urban population','CO2 emissions (kt)','Electric power consumption (kWh per capita)',
                                    'Forest area (sq. km)','Agricultural land (sq. km)',
                                    'Renewable energy consumption (% of total final energy consumption)'])].reset_index(drop=True)
df5 = df5[df5['Country Name'].isin(['India'])].reset_index(drop=True) #Filtering the Country from Country Name Column
df6 = df5.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df6 = df6.drop(df6.index[1]) #Droping the first Index
df6.reindex([1,0]) #Reindexing
df6 = df6.rename(columns=df6.iloc[0]) #Rename the index
df6.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df6.columns = ['Year','Urban population','CO2 Emissions','Ele. power consumption','Forest area','Agricultural land',
               'Renewable energy con.']
df6 = df6.drop(df6.index[0]).reset_index(drop=True) #Droping the Index
print(df6.describe()) # Provide Statistical Overview
df6['Year'] = pd.to_numeric(df6['Year']) #Converting the column in to numeric
df6 = df6[df6['Year']>= 2011].reset_index(drop=True) #Selecting the data from 2011
df6.drop(["Year"],axis=1,inplace=True) #droping the column
df6 = df6.astype(float) # Convert data in float
df6.to_excel('India_Indicators.xlsx') #Creating the excelfile of the dataset
print(df6.corr())

def Heatmap(): #Define function to creat Heatmap
    plt.figure(figsize=(30,20)) #To Create figure
    plot = sns.heatmap(df6.corr(),vmin=-1, vmax=1, annot=True, linewidth=1, linecolor='black', annot_kws={"size":40}) #To Create Heatmap
    plot.set_xticklabels(plot.get_xticklabels(), rotation=90, horizontalalignment='right',fontsize=45)
    plot.set_yticklabels(plot.get_yticklabels(), rotation=0, horizontalalignment='right',fontsize=45)
    plt.title('Heat MAP of India',size=50) #To provide the title to heatmap
    plt.show()
Heatmap() #calling the function

# Creating new dataframe by slicing/filtering the Indicatior column with Electric power consumption
df7 = df_wb[df_wb['Indicator Name'].isin(['Electric power consumption (kWh per capita)'])].reset_index(drop=True)
df8 = df7[df7['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany',
                                    'United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df9 = df8.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df9 = df9.drop(df9.index[1]) #Droping the first Index
df9.reindex([1,0]) #Reindexing
df9 = df9.rename(columns=df9.iloc[0]) #Rename the index
df9.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df9 = df9.drop(df9.index[0]).reset_index(drop=True) #Droping the Index
df9['Year'] = pd.to_numeric(df9['Year']) #Converting the column in to numeric
df9 = df9[df9['Year']>= 2000].reset_index(drop=True)
df9 = df9.astype(float) #Convert data into float
print(df9.describe()) #Provide Statistical Overview
print(df9) #To print the data
df9.to_excel('Electric power consumption (kWh per capita).xlsx') #Creating the excelfile of the dataset
# Creating new dataframe by slicing/filtering the Indicatior column with Renewable energy consumption (% of total final energy consumption
df10 = df_wb[df_wb['Indicator Name'].isin(['Renewable energy consumption (% of total final energy consumption)'])].reset_index(drop=True)
df11 = df10[df10['Country Name'].isin(['China','India','United States','Australia','Brazil','Nigeria','Germany',
                                       'United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df12 = df11.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df12 = df12.drop(df12.index[1]) #Droping the first Index
df12.reindex([1,0]) #Reindexing
df12 = df12.rename(columns=df12.iloc[0]) #Rename the index
df12.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df12 = df12.drop(df12.index[0]).reset_index(drop=True) #Droping the Index
df12 = df12.astype(float) #Convert data into float
df12 = df12[df12['Year']>= 2000].reset_index(drop=True) #index reset
print(df12.describe()) #Provide Statistical Overview
df12 = df12.dropna() #Drop Na Value
print(df12) #Printing the dataset
df12.to_excel('Renewable energy consumption.xlsx') #Creating the excelfile of the dataset

def lineplot(df,types,values, xlabel, ylabel, title): #Define a function to create linegraph
    #plt.figure(figsize=(11,10)) #To create figure size
    df.plot(kind=types,x=values,rot='45',figsize=[13,7],grid=1) #to Plot the graph
    plt.title(title,size=25) #To give the title
    plt.xlabel(xlabel,fontsize=20) #To provide the xlabel
    plt.ylabel(ylabel,fontsize=20) #To provide the ylabel
    plt.legend(bbox_to_anchor=(1.0,1.0),loc='upper left',prop={'size': 18}) #To create legend
    plt.xticks(fontsize=20) #Changin the xtick size
    plt.yticks(fontsize=20) #Changin the xtick size
    plt.xlim(2000,2014) #limit the x values
    plt.show() #To show the plot
    
lineplot(df9,"line","Year","Year","Electric power consumption (kWh per capita)","Electric power consumption") #Calling the function with argument   
lineplot(df12,"line","Year","Year","Renewable energy consumption(%)","Renewable energy consumption")#Calling the function with argument

#Creating new dataframe by slicing/filtering the Indicatior column with Required indicator
df13 = df_wb[df_wb['Indicator Name'].isin(['Forest area (sq. km)',
                                     'Agricultural land (sq. km)'])].reset_index(drop=True)
df14 = df13[df13['Country Name'].isin(['India'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df15 = df14.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df15 = df15.drop(df15.index[1]) #Droping the first Index
df15.reindex([1,0]) #Reindexing
df15 = df15.rename(columns=df15.iloc[0]) #Rename the index
df15.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Rename the column Name
df15.columns = ['Year','Forest area','Agricultural land']
df15 = df15.drop(df15.index[0]).reset_index(drop=True) #Droping the Index
print(df15.describe()) # Provide Statistical Overview
df15 = df15.astype(float) # Convert the data in to float
df15 = df15[df15['Year']>= 2011].reset_index(drop=True) #Selecting the data from 2011
df15 = df15.reset_index(drop=True) #Resetting the index
print(df15) #Print the dataset
df15.to_excel('India_Dataframe.xlsx') #Creating the excelfile of the dataset
#Creating new dataframe by filtering the Indicatior column with Required indicator
df16 = df_wb[df_wb['Indicator Name'].isin(['Forest area (sq. km)',
                                     'Agricultural land (sq. km)'])].reset_index(drop=True)
df17 = df16[df16['Country Name'].isin(['Brazil'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df18 = df17.T.reset_index(drop=False) #Creating a Transpose of Data Frame
df18 = df18.drop(df18.index[1]) #Droping the first Index
df18.reindex([1,0]) #Reindexing
df18 = df18.rename(columns=df18.iloc[0]) #Rename the index
df18.rename(columns = {'Country Name' : 'Year'}, inplace = True) #Remane the column Name
df18.columns = ['Year','Forest area','Agricultural land']
df18 = df18.drop(df18.index[0]).reset_index(drop=True) #Droping the Index
print(df18.describe()) # Provide Statistical Overview
df18 = df18.astype(float) #To convert the data in to float
df18 = df18[df18['Year']>= 2011].reset_index(drop=True) #Selecting the data from 2011
print(df18)
df18.to_excel('Brazil_Dataframe.xlsx') #Creating the excelfile of the dataset
plt.figure(figsize=(35,26)) #To creat the data
plt.suptitle("Forest area Vs Agricultural Land in India and Brazil", fontsize=50) #To generate the subplot title
plt.subplot(2,2,1) #To create first plot of subplot
plt.plot(df15["Year"], df15["Forest area"],color='red', label="Forest area",)
plt.xlabel("Year",fontsize=35) #To create x label
plt.ylabel("Forest area (sq. km)",fontsize=45) #To create y label
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.grid(True) #To create grid
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
plt.xlabel("Year",fontsize=35) #To provide xlabel
plt.ylabel("Forest area (sq. km)",fontsize=45) #To create y label
plt.grid(True) #To create grid
plt.title("Forest area-Brazil",fontsize=45) #To provide the title to first plot
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.legend(prop={'size': 45}) #To provide the legend
plt.subplot(2,2,4) #To create second plot of subplot.
plt.plot(df18["Year"], df18["Agricultural land"],color='green', label="Agricultural Land")
plt.xlabel("Year",fontsize=35) #To provide xlabel  
plt.ylabel("Agricultural land (sq. km)",fontsize=35) #To create y label
plt.grid(True) #To show the grid
plt.title("Agricultiral land-Brazil",fontsize=45) #To provide the title to second plot
plt.xticks(fontsize=40) #Changin the xtick size
plt.yticks(fontsize=40) #Changin the xtick size
plt.legend(prop={'size': 45})
plt.show() #To show the plot
#Creating new dataframe by slicing/filtering the Indicatior column with Urban population growth (annual%)
df19 = df_wb[df_wb['Indicator Name'].isin(['Urban population growth (annual %)'])].reset_index(drop=True)
df20 = df19[df19['Country Name'].isin(['China','India','United States',
                                       'Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True)#Filtering the Countries from Country Name Column
df20["Average"] = df20.iloc[:,53:63].mean(axis=1)#Making a new column
df20.to_excel('Urban population growth (annual %).xlsx')#Save data into excel file
print(df20)
#Creating new dataframe by slicing/filtering the Indicatior column with Urban population growth (annual%)
df21 = df_wb[df_wb['Indicator Name'].isin(['Mortality rate, under-5 (per 1,000 live births)'])].reset_index(drop=True)
df22 = df21[df21['Country Name'].isin(['China','India','United States',
                                       'Australia','Brazil','Nigeria','Germany','United Kingdom'])].reset_index(drop=True) #Filtering the Countries from Country Name Column
df22["Average"] = df22.iloc[:,53:63].mean(axis=1) #Making a new column
df22.to_excel('Mortality rate, under-5.xlsx') #Save data into excel file
print(df22)
plt.figure(figsize=(28,12)) #Creating the figure
plt.suptitle("Urban population growth (annual %) VS Mortality rate, under-5 (per 1,000 live births)", fontsize=32) #To generate the subplot title
plt.subplot(1,2,1) #To create first plot of subplot
plt.pie(df20['Average'],labels=df20['Country Name'],rotatelabels=False,autopct='%1.0f%%',shadow=False,labeldistance=1.02,radius=1.2,pctdistance=0.7,textprops = {"fontsize":28}) #Generating the first pie chart
plt.title("Urban population growth",loc="center",fontsize=30) #To provide the title 
plt.subplot(1,2,2) #To create first plot of subplot
plt.pie(df22['Average'],labels=df22['Country Name'],rotatelabels=False,autopct='%1.0f%%',shadow=False,labeldistance=1.01,radius=1.2,pctdistance=0.7,textprops = {"fontsize":28}) #Generating the second pie chart
plt.title("Mortality rate,under-5",loc="center",fontsize=30) #To provide the title to the plot
plt.show() #To show the plot
