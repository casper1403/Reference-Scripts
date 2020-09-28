import pandas as pd

# Change width notebook
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


#Import data into dataframe
def import_data():
    df = pd.read_csv("csv_name.csv",na_values=['-999',  sep='\t', 'value for na'])
    df = pd.read_excel("excel_name.xlsx")


#To loop over rows of dataframe containing 2 rows  Row1 will often be the index
for row1, row2 in df.iterrow():
    print(row1,row2)

#Generate dates with pandas
dates = pd.date_range('1/1/2001', periods=500, freq="M")


"""View data"""

# SHow top and bottom of
df.head
df.tail
df.shape

# to select columns and view them in a list:
list(df.columns)


"""Selection"""

#select one Column
df['column']

#Select two column double list
df[['column1', 'column2']]

#Filter rows with a specific values with logical expression
df[df['column'] > 10]

# Filter rows with value boolean value
df[df['column'].isin(['value1 from column', 'value2 from column'])]
df[(df['column'] == 'values' )| (df['column'] == 'other value') ]

# Select if value is known
df[df['column'].notna()]




"""The loc operator
makes you select a values based on a two conditions seperated by a comma. The left size before the comma are the rows you want and after the comma the columns
For both the part before and after the comma, you can use a single label, a list of labels, a slice of labels, a conditional expression or a colon. Using a colon specificies you want to select all rows or columns."""

df.loc[df['row' > 'value', "Column name"]]


# Select the rows where value is met
df.loc[df['Column'] == 'Some value']



"""plotting the data"""
#plot entire frame
df.plot()

# plot single column
df['column'].plot()

# create a scatter plot
df.plot.scatter(x='xvalues' y='yvalues')

#create a box plot
df.plot.box()

# if you want the columns to be in different plots set subplot = Tre
df.plot.area(subplots=True)

# Plot multiple y line
df.plot(x="some column", y=['column2','columns3'])


"""Create columns based on existing columns"""

# create a new column with a value multiplied ( YOU DONT NEED A LOOP TO ITERATE OVER THE ROWSho)
df['new column'] = df['old column'] * 'Some operation'



"""Modify data"""
# Replace a with b
df = df.replace('a','b')

# Set the columns
df = df.set_axis(['a',' b' , 'c', 'd', 'e', 'f', 'g', ], axis=1, inplace=False)


# It is possible to apply a function to the dataframe with the apply function
df = df.apply(lambda x : x * 10)


"""Grouping data"""

# THis will take column and and 2 and greate a group of the values based on column1. Then calculte the average over these groups.
df[['column1','column2']].groupby('column1').mean()

# if you want to do further operations on the grouped data:
df[['column1','column2']].groupby('column1', as_index = False).mean()

# if you want to return to a datafrme
df[['column1', 'column2']].groupby('column1').mean().reset_index()

# group data without heirarchical indexing
df[['column1', 'column2']].groupby('column1').mean().unstack()



"""Statistical operations"""

# Count the number of records by category
df['column'].value_counts()

# Return mean of Column
df[].mean()

# Return Median
df[].median()

# Return Mode
df[].mode()

# Return Skew of distribution
df[].skew()

# Return Kurt of distribution
df[].kurt()

#Show values at quartiles
df[].df[].quantile([0.25 ,0.5, 0.75])

# Return Variance
df[].var()

# Return Standard Deviation
df[].std()

# Return the Count, mean, std, quantiles
df[].describe()

# Return Correlation of two differnt factors
df[].cor(df[])
