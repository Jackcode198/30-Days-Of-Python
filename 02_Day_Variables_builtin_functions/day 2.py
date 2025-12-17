# Day 2: 30 Days of python programming

#exercise level 1

#3-13
first_name = 'Jack'
last_name = 'Potter'
full_name = 'Jack Potter'
country = 'United Kingdom'
city = 'York'
age = 17
year = 2008
is_married = False
is_true = True
is_light_on = True
first_name, last_name,country, age, is_married = 'Jack', 'Potter', 'United Kingdom', 17, False

print('first name:', first_name)
print('last name:', last_name)
print('age:', age)
print('is light on:', is_light_on)

#exercise level 2
#1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2-3
print(len(first_name))
first_name, last_name = 'Jack' , 'Potter'
print(len(last_name))

#5-11
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(num_one)
print(num_two)
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#12
import math
user_radius = float(input('enter the radius of the circle: '))
area_from_input = user_radius**2*math.pi
print('area of the circle from user input:', area_from_input)
#13
user_first_name =str(input('first name:'))
user_last_name = str(input('last name:'))
user_country = str(input('country:'))
user_age = int(input('age:'))
print('first name:', user_first_name)
print('last name:', user_last_name)
print('country:', user_country)
print('age:', user_age)
#14
help('keywords')