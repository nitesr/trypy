import pandas

people = {
    "first": ["Matt", "Joe", "John"],
    "last": ["Matty", "Joey", "Johnny"],
    "gender": ["M", "F", "M"]
}
people_df = pandas.DataFrame(people)
filer_by_joe = people_df['first'] == 'Joe'
print("filter by joe:", people_df[filer_by_joe], sep="\n", end="\n\n")
print("type after applying filter is:", type(people_df[filer_by_joe]), type(people_df[filer_by_joe]['last']), sep="\n", end="\n\n")

filer_by_male = people_df['gender'] == 'M'
print("male people are:", people_df[filer_by_male], sep="\n", end="\n\n")
print("first male person is:", people_df[filer_by_male].head(1), sep="\n", end="\n\n")

filter_by_first_startby_J = people_df['first'].str.startswith(('j', 'J'))
print("people name start wth j are:", people_df[filter_by_first_startby_J], sep="\n", end="\n\n")

print("=========================================")