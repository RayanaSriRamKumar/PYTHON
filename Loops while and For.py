#!/usr/bin/env python
# coding: utf-8

# In[5]:


count = 0
while count < 5:
    print(count)
    count = count + 1


# In[6]:


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break


# In[1]:


count=0
while count < 5:
    print(count)
    count = count + 1
    if count==2 :
        count=10
    else:
        print(count)
    


# In[7]:


numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


# In[9]:


language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])


# In[10]:


# for with tuples
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


# In[11]:


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


# In[2]:


for i in range(5,20,2):
       print(i)


# In[3]:


for i in range(1,10,1):
       print(i , "\n*")


# In[ ]:





# In[4]:


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break


# In[12]:


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


# In[ ]:


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')


# In[ ]:


#Exercises:
1. Iterate 0 to 10 using for loop, do the same using while loop.

2. Iterate 10 to 0 using for loop, do the same using while loop.

3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######
4. Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
5. Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100

6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

7.Use for loop to iterate from 0 to 100 and print only even numbers

8.Use for loop to iterate from 0 to 100 and print only odd numbers

#Exercises: level-2
    
1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.

1.Use for loop to iterate from 0 to 100 and print the sum of all evens and
the sum of all odds.


