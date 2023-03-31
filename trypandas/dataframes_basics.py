import numpy
import pandas
from pandas import NA

df = pandas.DataFrame({
        'a': ['a1', 'a2'],
        'b': ['b1', 'b2']
    }, index=['one', 'two'])
print(type(df), end="\n\n")
print(df, end="\n\n")
# prints the shape (rows x cols)
print(df.shape, end="\n\n")
# prints the datastructure
print("dataframe info:", df.info, sep="\n", end="\n\n")
print("are both records equal?", df.loc['one'], df.iloc[0], df.loc['one'] is df.iloc[0], end="\n\n")
# print both the records
print(df.loc['one':'two'], end="\n\n")

print("1st row 2nd col value is", df.loc['one', 'b'], end="\n\n")
print("1st row 2nd col value is", df.iloc[0, 1], end="\n\n")
df.iloc[0, 1] = 'b is changed to bb'
print("1st row 2nd col value is", df.loc['one', 'b'], end="\n\n")

df['c'] = ['c1', 'c2']
print("after adding 3rd column, the shape is", df.shape, end="\n\n")

df.drop('c', axis=1, inplace=True)
print("after dropping 3rd column, the shape is", df.shape, end="\n\n")

print("=========================================")

some_data = {
    'col1': ['a', NA, None, 'NA'],
    'col2': [10, None, 'number1', numpy.NaN]
}
some_data_pf = pandas.DataFrame(some_data)
print(some_data_pf.iloc[1][1], some_data_pf.iloc[2][1], end="\n\n")
print("isna data: ", some_data_pf.isna(), sep="\n", end="\n\n")
print("isnull data: ", some_data_pf.isnull(), sep="\n", end="\n\n")

# drop na rows df.dropna(axis=0) and columns df.dropna(axis=1)
# fill na cells df.fillna(0)
print("=========================================")

employees = {
    'name': [ "Joe John", "Matt Demon", "Anil Kapoor", "PT Usha", "Nivedita Roy"],
    'age': [10, 50, 20, 60, 30],
    'gender': ["M", "M", "M", "F", "F"]
}
employees_df = pandas.DataFrame(employees)
print("top 3 youngest employees are:", employees_df.sort_values(by="age").head(3), sep="\n", end="\n\n")
print("youngest female employee is:", employees_df.sort_values(by=["gender", "age"]).head(1), sep="\n", end="\n\n")
print("by gender counts", employees_df["gender"].value_counts(), sep="\n", end="\n\n")

print("=========================================")
survey_results_df = pandas.read_csv("survey_results_public.csv")
print(survey_results_df.info())
filter_by_indians = survey_results_df['Country'] == 'India'
print("python developers from india", survey_results_df.loc[filter_by_indians]['LanguageHaveWorkedWith'].str.contains('Python').sum(), end="\n\n")
