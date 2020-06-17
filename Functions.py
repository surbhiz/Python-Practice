# Empty Function

def empty_fun():
    pass

# SUM OF NUMBERS IN THE LIST


a_list = [5, 10, 15, 20, 25]

sum_manual = 0
for elements in a_list:
    sum_manual += elements

print(sum_manual)
# using sum() function
print(sum(a_list))

# UPDATE THE VALUES IN CONTENT RATING DICTIONARY

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
print(content_ratings)

# Creating a own function to get square of a number


def square(a_num):
    square_number = a_num * a_num
    return square_number+10


print(square(10))
print(square(16))

# creating a function with arguments


def personal_details(name, branch="CSE"):
    return '{} is my name, {} is my branch'.format(name, branch)


print(personal_details("Surbhi"))

# creating a functions with arguments which can have default multiple values


def student_details(*args, **kwargs):
    print(args)
    print(kwargs)


student_details('CSE', 'UTA', 'Arlington',
                name="Surbhi", last="Zambad", age=26)

# creating a functions with arguments which can have multiple values

branch_uni_city = ['CSE', 'UTA', 'Arlington']
info = {'name': "Surbhi", 'last': "Zambad", 'age': 26}

student_details(*branch_uni_city, **info)

# creating a calender functionality which determines whether the year is leap or not and defines the days in month

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    '''returns true if the year is leap year and false if year is not leap year'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    '''returns number of days in that month and in that year'''

    if not 1 <= month <= 12:
        print("Invalid month")

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2017, 12))
