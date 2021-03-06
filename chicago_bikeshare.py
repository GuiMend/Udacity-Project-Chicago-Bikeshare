
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

for index in range(20):
    print(f'Row {index}: {data_list[index]}')

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for index, row in enumerate(data_list[:20]):
    print(f'Row {index+1} gender: {row[-2]}')

# Cool! We can get the rows(samples) iterating with a for and the columns
# (features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another
# list in the same order


def column_to_list(data, index):
    """
    This function recieves a table and return a list of one column of the table
    Args:
        data: list of rows containing a list of columns in each row.
        index: index of desired column.
    Returns:
        list with the desired column values from all rows
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by
    # index and append into a list
    for row in data:
        if row[index].isdigit():
            column_list.append(int(row[index]))
        else:
            column_list.append(row[index])

    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)
            ) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)
           ) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(
    data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and
# Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for gender in column_to_list(data_list, -2):
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15]
# means 10 Males, 15 Females)


def count_gender(data_list):
    """
    Recieves a table and return the male and female count in a list
    Args:
        data: list of rows containing a list of columns in each row.
    Returns:
        list with the count of males and females
    """
    male = 0
    female = 0
    for gender in column_to_list(data_list, -2):
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)
            ) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(
    data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the
# gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.


def most_popular_gender(data_list):
    """
    Recieves a table and returns a string containing the most popular 
    gender in the table
    Args:
        data: list of rows containing a list of columns in each row.
    Returns:
        str containing the most popular gender: Male, Female or Equal
    """
    answer = 'Equal'
    male, female = count_gender(data_list)
    if male > female:
        answer = 'Male'
    elif female > male:
        answer = 'Female'
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)
            ) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(
    data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")


def count_user_type(data_list):
    """
    Recieves a table and return in a list the count of user types
    Args:
        data: list of rows containing a list of columns in each row.
    Returns:
        list with the count of customers, subscribers and dependents
    """
    customer = 0
    subscriber = 0
    dependent = 0
    for gender in column_to_list(data_list, -3):
        if gender == 'Customer':
            customer += 1
        elif gender == 'Subscriber':
            subscriber += 1
        elif gender == 'Dependent':
            dependent += 1
    return [customer, subscriber, dependent]


types = ["Customer", "Subscriber", "Dependent"]
quantity = count_user_type(data_list)
print('quantity: ', quantity)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are rows without gender information"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.


def calculate_mean(trips):
    """
    Recieves a list of trips and return the mean of the duration
    Args:
        trips: list of numbers containing the duration of a trip.
    Returns:
        number with the mean trip duration
    """
    trip_duration_sum = 0
    for trip_duration in trips:
        trip_duration_sum += trip_duration
    return trip_duration_sum / len(trips)


def calculate_median(trips):
    """
    Recieves a list of trips and return the meadian of the list
    Args:
        trips: list of numbers containing the duration of a trip.
    Returns:
        number with the meadian of trips
    """
    if len(trips) % 2 == 0:
        lower_medium_index = len(trips) // 2
        return (trips[lower_medium_index] +
                trips[lower_medium_index + 1]) / 2

    return trips[(len(trips)+1)//2]


trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = calculate_mean(trip_duration_list)
median_trip = calculate_median(trip_duration_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip,
      "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about
# start_stations?
# How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = {row[3] for row in data_list}

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input,
# output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
    Example function with annotations.
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        List of X values
"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"


def count_items(column_list):
    """
    Recieves a list and returns a tuple with 2 lists, one containing the
    category and the other containing the total count in the received list
    Args:
        column_list: list of data.
    Returns:
        tuple with two lists, the types and the total count
    """
    item_types = {_ for _ in column_list}
    item_types = list(item_types)
    count_items = [0 for _ in item_types]

    for item in column_list:
        count_items[item_types.index(item)] += 1

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
