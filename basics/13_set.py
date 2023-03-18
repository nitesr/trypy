#
# list - square braces - []
# tuple - circle braces - ()
# set & dict - curly braces - {}
#

fruits_set = {"apple", "banana", "mango", "mango"}
print("type of set is", type(fruits_set))
print("(you might not get same order as set is unordered) fruits_set is", fruits_set)
print("there is only one mango in fruits_set --> ", fruits_set)
print("len of fruits_set is", len(fruits_set))
print("max element in fruits_set is", max(fruits_set))

if "mango" in fruits_set:
    print("there is a mango in fruits_set --> ", fruits_set)
else:
    print("there is no mango in fruits_set --> ", fruits_set)

# Error: can index into set
# print(fruits_set[0])

# add to a set
people_set = {"papa", "jon", "claire", "Claire"}
print("people_set", people_set)
people_set.add("John")
print("people_set after adding John", people_set)

# merge sets
companies_set = {"A", "Alibaba"}
more_companies_set = {"Meta", "Google", "A"}
more_companies_List = {"Amazon", "Meta"}
more_companies_tuple = ("Apple", "Amazon")
companies_set.update(more_companies_set)
companies_set.update(more_companies_List)
companies_set.update(more_companies_tuple)
print("companies_set", companies_set)

# remove an element
laptops_set = {"HP", "Chromebook", "Mac", "Intel", "Windows"}
laptops_set.remove("Windows")
print("laptops_set after removing Windows", laptops_set)

# Error can't remove non-existing element
# laptops_set.remove("OSX")
# print("laptops_set after removing OSX", laptops_set)

laptops_set.discard("OSX")
print("laptops_set after discarding OSX", laptops_set)

laptops_set.clear()
print("laptops_set after clearing it", laptops_set)

# set theory operations
odds_set = {1, 3, 5, 7, 9}
evens_set = {0, 2, 4, 6, 8, 10}
primes_set = {2, 3, 5, 7}
all_set = odds_set.union(evens_set)
print("union of odds and evens from 0-10", all_set)

even_primes_set = evens_set.intersection(primes_set)
print("intersection of primes and evens from 0-10", even_primes_set)

print("Are primes subset of odds? - ", primes_set.issubset(odds_set))
print("Are odds superset of primes? - ", odds_set.issuperset(primes_set))
print("Are evens are subset of all_set? - ", evens_set.issubset(all_set))





