# Variable = A container for a value (string, integer,float, boolean)
# A Variable behaves as it wthe value it contains

#Strings

first_name = "Ram"
food ="pizza"
email="sriram@gmail.com"

#Integers

age=18
quantity = 3
num_of_students=30

#float 

price= 10.99
gpa=9.2
distance=3.5

#boolean

is_student = True
for_sale=True
is_online=False

if is_student:
  print("You are a student")
else:
  print("You are not a student")

if for_sale:
  print("This product is for sale")
else:
  print("This product is not for sale")

if is_online:
  print("You are online")
else:
  print("You are offline")

print(f"Hello {first_name}")
print(f"You like {food}") 
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"Your class has{num_of_students} students")
print(f"The price is{price}")
print(f"Your gpa is{gpa}")
print(f"You ran {distance} kms")
print(f"Are you a student? :{is_student}")
