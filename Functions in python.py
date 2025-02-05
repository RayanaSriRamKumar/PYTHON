#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()


# In[1]:


def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()


# In[ ]:





# In[2]:


# using return 
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())


# In[8]:


# calling function many times
def add_two_numbers (num1,num2):
    total = num1 + num2
    return total
print(add_two_numbers(3,8))
print(add_two_numbers(2,8))


# In[ ]:


# parsing input aguments to functio 
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10))


# In[ ]:


Declare a function add_two_numbers. 
   It takes two parameters and it returns a sum.


# In[2]:


# getting the values from external to the code 
def add_two_numbers(radius, Pi):
    return Pi*radius*radius

# Taking input from the user
radius = float(input("Enter the radius: "))  # Convert to float for decimal numbers
piiii = float(input("Enter the pi: "))  # Convert to float for decimal numbers

# Call the function and display the result
result = add_two_numbers(radius, piiii)
print(f"The Area of circle  is {result}")


# In[ ]:


1. Area of a circle is calculated as follows: area = π x r x r.
    Write a function that calculates _area_of_circle_.
    
2. Declare a function named print_list. 
It takes a list as a parameter and it prints out each element of the list.



2. Write a function called add_all_nums which takes arbitrary number 
   of arguments and sums all the arguments.
   Check if all the list items are number types. 
    If not do give a reasonable feedback.
    
3. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5)
    + 32. 
    Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
    
4. Write a function called check-season,
it takes a month parameter and returns the 
season: Autumn, Winter, Spring or Summer.
    
    
5. Write a function called calculate_slope which 
return the slope of a linear equation

6. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
    Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.

8. Declare a function named reverse_list.
It takes an array as a parameter and it returns the reverse of the 
array (use loops).


# In[ ]:


def area_circle (radius):
    

