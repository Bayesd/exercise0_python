def get_age_from_person(person):
    age = person["age"]
    return age


my_person = {
    "name": "Sarah",
    "age": 29
}

age = get_age_from_person(my_person)

print(age)
# The correct answer here should be `29`


#alternativt, om man vill kringgå metoden
print(my_person["age"])