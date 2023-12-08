import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""
When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each 
    list as columns of the DataFrame.
A DataFrame is a 2-dimensional data structure that can store data of different types 
    (including characters, integers, floating point values, categorical data and more) in columns
You can create a Series from scratch as well --> pd.Series([22, 35, 58], name="Age") --> It will create a new column with age


How do I read and write tabular data?
    pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
        pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
        each of them with the prefix read_*
    To know the data types used in the dataframes can be viewed by calling the dtypes. csvobj.dtypes.
    The data types in this DataFrame are integers (int64), floats (float64) and strings (object).
    from_* is used to read the data from the specific format and to_* is used to export the data to another format.
    To export the data into Excel
        Convert the csv or other type object to dataframe and from the dataframe object using to_excel can be converted to another format
    
    To know the technical summary of the dataframe we use info() method.
        csvobj.info()
    Getting data in to pandas from many different file formats or data sources is supported by read_* functions. 
    Exporting data out of pandas is provided by different to_*methods. 
    The head/tail/info methods and the dtypes attribute are convenient for a first check.

How do I select a subset of a DataFrame?
    To select a single column, use square brackets [] with the column name of the column of interest.
    Each column in a DataFrame is a Series. As a single column is selected, the returned object is a pandas Series. <class 'pandas.core.series.Series'>
    It is possible to select the multiple columns of the dataframe. titanic[['age','name']]
    A subset of both rows and columns is made in one go and just using selection brackets [] is not sufficient anymore. 
        The loc/iloc operators are required in front of the selection brackets []
        titanic.loc[titanic["Age"] > 35, "Name"]
    Remember
        When selecting subsets of data, square brackets [] are used. 
        Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon. 
        Select specific rows and/or columns using loc when using the row and column names. 
        Select specific rows and/or columns using iloc when using the positions in the table. 
        You can assign new values to a selection based on loc/iloc.
        

How do I create plots in pandas?
    With a DataFrame, pandas creates by default one line plot for each of the columns with numeric data.
    If the user want's to plot to a particular column it can be done using the csvobd['ColName'].plot()
    

How to create new columns derived from existing columns?
    To create a new column, use the [] brackets with the new column name at the left side of the assignment.
        air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
        air_quality.head()
    To rename the column name we can use rename() method
        air_quality_renamed = air_quality.rename( columns={ "station_antwerp": "BETR801", "station_paris": "FR04014", "station_london": "London Westminster", } )
    String built-in functions can also be used with the rename method.
        air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
    Create a new column by assigning the output to the DataFrame with a new column name in between the []. 
    Operations are element-wise, no need to loop over rows. 
    Use rename with a dictionary or function to rename row labels or column names.

How to Calculate the Summary Statistics?
    Different statistics are available and can be applied to columns with numerical data. 
    Operations in general exclude missing data and operate across rows by default.
    To find the mean of a series we use mean method
        titanic["Age"].mean()
    We can also find the multiple data series 
        titanic[["Age", "Fare"]].median()
    The aggregating statistic can be calculated for multiple columns at the same time.
        titanic[["Age", "Fare"]].describe()
        it will display the stats like Count, mean, std, min, max, 25%, 50%, 75%
    We can also group the columns based on the other column.
        titanic[["Sex", "Age"]].groupby("Sex").mean()
        Process:
            Split the data into groups 
            Apply a function to each group independently 
            Combine the results into a data structure
    If we are only interested in the average age for each gender, 
        the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well
        titanic.groupby("Sex")["Age"].mean()
                    PassengerId  Survived    Pclass  ...     SibSp     Parch       Fare
            Sex                                      ...                               
            female   431.028662  0.742038  2.159236  ...  0.694268  0.649682  44.479818
            male     454.147314  0.188908  2.389948  ...  0.429809  0.235702  25.523893
    
    If we are only interested in the average age for each gender, 
        the selection of columns (rectangular brackets [] as usual) is supported on the grouped data as well
            titanic.groupby("Sex")["Age"].mean()
    The value_counts() method counts the number of records for each category in a column.
        titanic["Pclass"].value_counts()
    The function is a shortcut, as it is actually a groupby operation in combination with counting of the number of records within each group
        titanic.groupby("Pclass")["Pclass"].count()
    Remember:
        Aggregation statistics can be calculated on entire columns or rows. 
        groupby provides the power of the split-apply-combine pattern. 
        value_counts is a convenient shortcut to count the number of entries in each category of a variable.

How to reshape the layout of tables?
    If we want to sort the table based on the particualr column that can be possible using the sort_values() method
        titanic.sort_values(by="Age").head()    
    Can also sort the table ascending and descending order using ascending=False attribute.
        titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
    

    
    
    



"""




'''
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

How do I read and write tabular data?
epiplexCsv = pd.read_csv("Inputdata/EpiplexCapture.csv")
print(epiplexCsv)
print(epiplexCsv.head(8))       #it will print first 8 rows of a Dataframe
print(epiplexCsv.dtypes)

    To Convert from one format to another format
epiplexCsv = pd.read_csv("Inputdata/EpiplexCapture.csv")
df=pd.DataFrame(epiplexCsv)
df.to_excel("Output/epiplex.xlsx",index=False,sheet_name="epiplexcsv_xlsx") #Index is the row number that will be printed.


    How do I select a subset of a DataFrame?
    
titanic = pd.read_csv("Inputdata/Titanic.csv")
print(titanic.info()) #to know the information about the csv file
print(titanic.head(5)) #to Print the first 5 dataframe
print(titanic.tail(5)) #to print the ;a=last 5 dataframe.
print(len(titanic["PassengerId"]))
print(titanic.shape)
print(titanic.size)
print(((titanic[["Age",'Fare']])))
print(titanic[titanic["Age"]>34])

age_not_na = titanic[titanic['Age'].notna()]
pd.DataFrame(age_not_na).to_excel("Output/age_not_na.xlsx","AgeNotNA",index=False)
adult_names = titanic.loc[titanic['Age']>28,"Name"]
print(adult_names.head(5))

    How do I create plots in pandas?
weatherReport = pd.read_csv("Inputdata/weather_report.csv")
print(weatherReport.head(5))
weatherReport.plot()
plt.show()

    How to Calculate the Summary Statistics?
titanicObj = pd.read_csv("Inputdata/Titanic.csv")
print(titanicObj[['PassengerId','Age']].mean())
print(titanicObj[['PassengerId','Age']].median())
print(titanicObj[['PassengerId','Age']].describe())
df = pd.DataFrame(titanicObj)
titanicObj.mod
seg = df.agg(
    {
        "Age":["min","max","median","mean"]
    }
)
print(seg)

    How to reshape the layout of tables?
airQuality = pd.read_csv("Inputdata/air_quality_long.csv")
no2Data = airQuality[airQuality['parameter']=='no2']
print(no2Data)
no2_subset = no2Data.sort_index().groupby(["location"]).head(2)
m=no2Data.pivot(columns="location", values="value").plot()


Excercise

'''
print("Pandas version is",pd.__version__)
# Creating a dataframe
df = pd.DataFrame({
    'x':[1,2,3,4],
    'a':['a','b','c','d'],
    's':['!','#','=','%']
})
print(df)
# Creating a Dataseries
s = pd.Series([1,2,3,4,5])
print(s)

# Random Number of 5*5
rand = pd.DataFrame(np.random.rand(5,5))
print(rand)

seriesList = [5,6,7,8,6]
s = pd.Series(seriesList)
print(s)

# Adding a date index for the existing dataframe
df.index = pd.date_range('2023/12/1',periods=df.shape[0])
print(df.index,df,sep="\n")

# Prints the first 7 datasets if the columns has only 5 data it will print only that.
print("The head is\n",df.head(7))

# Prints the last 7 datasets if the columns has only 5 data it will print only that.
print("The tail is\n",df.tail(7))

# It will print the shape of the dataset
print("The shape of the dataset is is\n",df.shape)

# Index, Datatype and Memory information
print("Index, Datatype and Memory information\n",df.info())

# Summary statistics for numerical columns
print("Summary statistics for numerical columns\n",df.describe())



















