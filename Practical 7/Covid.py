#import a few python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/wd/Downloads")# change the working directory to where your full_data.csv file is stored
print(os.getcwd())#print working directory
os.listdir()#list files in the directory

covid_data=pd.read_csv("full_data.csv")#use the pandas library to read the content of the .csv file into a dataframe object

#basic information
print(covid_data.head(5))#print out the first 5 rows of data in covid_data
covid_data.info()#know the type of the data points, name of the columns,number of rows in the data
print(covid_data.describe())#learn the count,mean,standard deviation,minimum,percentile,maximum of the data


#see specific values in the dataframe
print(covid_data.iloc[0,1])#shows you what’s in the first row, second column(iloc uses the row and column index to locate items)
print(covid_data.head(1))#checkout previous command
covid_data.iloc[2,0:5]#just show the data in row 2, column from 0 to 5
covid_data.iloc[0:2,:]#row from 0 to 2, print all the column
covid_data.iloc[0:10:2,0:5]#row:from 0 to 10, only print odd-numbered line，column：from 0 to 5
print(covid_data.iloc[0:1001:100,1])# show the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:3,[0,1,3]])# I wanted to see the first three rows, but only the first, second, and fourth column
my_columns = [True, True, False, True, False, False]
print(covid_data.iloc[0:3,my_columns])#use Boolean index to get the same outcome as just insert numbers

print(covid_data.loc[2:4,"date"])#print the date from row 2 to 4(loc uses column names to locate items)
print(covid_data.loc[0:81,"total_cases"])#print the total cases from row 0 to 81

#we can actually look for rows that interest us without having to know the row numbers.
Afghanistan= covid_data.loc[covid_data["location"]=="Afghanistan","total_cases"]#only extract the row with Afghanistan
print(Afghanistan)

# made an object called new_data to store only the data on new cases and deaths for 31 March
my_columns=[True, False, True, True, False, False]
new_data=covid_data.loc[covid_data["date"]=="2020-03-31",my_columns]
print(new_data)

#mean of new cases and new deaths in covid_data
num1=np.array(new_data.loc[:,"new_cases"])
num2=np.array(new_data.loc[:,"new_deaths"])
a=np.mean(num1,axis=0)
b=np.mean(num2,axis=0)
print(a)
print(b)
c=b/a
print('%.2f%%' % (c*100))#change c into percentage
cases=new_data.loc[:,"new_cases"]
deaths=new_data.loc[:,"new_deaths"]
plt.boxplot([cases,deaths],vert=True,whis=1.5,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=False,notch=False,labels=["new_cases","new_deaths"])
plt.title('new cases and new deaths on March 31st',color="gold")
plt.show()
#the graph of world new cases and new deaths
world_dates=covid_data.loc[covid_data["location"]=="World",'date']#extract date from "world" column
world_new_cases=covid_data.loc[covid_data["location"]=="World",'new_cases']#extract world new cases from covid_data
world_new_deaths=covid_data.loc[covid_data["location"]=="World",'new_deaths']#extract world new deaths from covid_data
plt.plot(world_dates,world_new_cases,'co')#plot the data of world new cases over time
plt.plot(world_dates,world_new_deaths,'b+')#plot the data of world new cases over time
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-60)#define the tags in x axis
plt.title('world new cases and new deaths',color="gold")#the style of its title
plt.show()
#the graph of the total number of deaths and cases in Austria
Austria_dates=covid_data.loc[covid_data["location"]=="Austria",'date']
Austria_total_cases=covid_data.loc[covid_data["location"]=="Austria",'total_cases']
Austria_total_deaths=covid_data.loc[covid_data["location"]=="Austria",'total_deaths']
plt.plot(Austria_dates,Austria_total_cases,'co')
plt.plot(Austria_dates,Austria_total_deaths,'+')
plt.title('the total number of deaths and cases in Austria')#the style of its title
plt.xticks(Austria_dates.iloc[0:len(Austria_dates):4],rotation=-60)
plt.show()
#the graph of How have new cases and total cases developed over time in China
China_dates=covid_data.loc[covid_data["location"]=="China",'date']#extract date from "China" column
China_new_cases=covid_data.loc[covid_data["location"]=="China",'new_cases']#extract China's new cases from covid_data
China_total_cases=covid_data.loc[covid_data["location"]=="China",'total_cases']#extract China's total cases from covid_data
plt.plot(China_dates,China_new_cases,'co')#plot the data of China_new_cases over time
plt.plot(China_dates,China_total_cases,'b+')#plot the data of China_total_cases over time
plt.xticks(China_dates.iloc[0:len(China_dates):4],rotation=-50)#define the tags in x axis
plt.title('How have new cases and total cases developed over time in China',color="gold")#the style of its title
plt.show()
