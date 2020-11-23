def make_unique(names):
    names = set(names)
    return names


my_names = ["John", "Sarah", "Hannah", "Hannah", "Tom", "George", "Sarah"]

unique_names = make_unique(my_names)

print(unique_names)
# The correct answer here should be:
#   `['Sarah', 'Hannah', 'John', 'George', 'Tom']`
