# the `numbers` argument for this function will always be a list.
def find_largest(numbers):
    numbers.sort()
    largest_num = numbers[-1]
    return largest_num


some_numbers = [55, 34, 100, 32, 0, 88, 9]

largest = find_largest(some_numbers)

print(largest)
# the expected output here is: `100`
