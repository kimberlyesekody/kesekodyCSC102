#!/usr/bin/env python
# coding: utf-8

# In[1]:


str = input("Enter your state of origin:")

print ("Your state of origin is: ",str)
print ("The first character is: ", str[0])
print ("The character starting from 3rd to 5th are: ", str[2:5])
print ("The string starting from 3rd character is:")


# In[3]:


# Input from user
m = float(input("Enter mass in Kilograms: "))

# Constant value for the speed of light in m/s
c = 299792458

# Calculate energy using Einstein's equation
energy = m * c ** 2

# Disp,aying the result
print (f"The energy equivalent to (m) kg of mass is {energy} joules.")


# In[6]:


list = [ 'Anaconda', 786 , 2.23, 'Jupiter', 70.2]
shortlist = [321, 'Python']

print(list)        '''Prints complete list '''
print(list[0])        # Prints first element of the list
print(list[1:3])      # Prints elements starting from second till 3rd
print(list[2:])      '''Prints elements starting from 3rd element '''
print(shortlist = 2)  #Prints list two times
      print(list + shortlist) # rints concatenated lists


# In[14]:


list = [ 'Anaconda', 786 , 2.23, 'Jupiter', 70.2]
shortlist = [321, 'Python']

print(list)        #Prints complete list
print(list[0])        # Prints first element of the list
print(list[1:3])      # Prints elements starting from second till 3rd
print(list[2:])      # Prints elements starting from 3rd element
print(shortlist * 2)  # Prints list two times
print(list + shortlist) # Prints concatenated lists


# In[16]:


tuple = ('Ekiti', 750, 'Oshogbo', 250, 'Akure', 500)
s_tuple = ('Abeokuta', 300, 'Ogbomoso')

# Prints the complete tuple
print (tuple)

#Prints last element of the tuple
print (tuple[-1])

# Prints element of the tuple starting frpm 2nd till 3rd
print (tuple[2:4])

#Prints elements of the tuple starting from 3rd element
print (tuple[3:])

#Prints the contents of the tuple twice
print (s_tuple * 3)

#Prints concatenated tuples
print (tuple + s_tuple)


# In[18]:


# Returns false as game_1 is not equal t game_2
game_1 = 2
game_2 = 4
print(bool(game_1 == game_2))
# Or
print(game_1 == game_2)

#Returns False as val is None
val = None
print(bool(val))

#Returns false as num is an empty sequence
num = ()
print(bool(val))

#Returns true asa ge is boolean
age = True
print(bool(age))


# In[19]:


# Convert to int

grade = int(79)        # grade will be 70
gpa = int(4.9)         # gpa will be 4.9
cgpa = int("4")        # cgpa will be 4

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[20]:


# Convert to float
grade = float(97)
gpa = float(5)
cgpa = float("4.7")

print(f"Grade = {grade}")
print(f"GPA = {gpa}")
print(f"CGPA = {cgpa}")


# In[ ]:




