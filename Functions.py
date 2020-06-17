# Empty Function

def empty_fun():
    pass

# SUM OF NUMBERS IN THE LIST


a_list = [5, 10, 15, 20, 25]

sum_manual = 0
for elements in a_list:
    sum_manual += elements

print(sum_manual)
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
