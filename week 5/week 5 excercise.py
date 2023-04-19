#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Pythons program to swap two cities

# To take inputs from the user
city_1 = input('Enter name of City 1: ')
city_2 = input('Enetr name od City 2: ')

# create a temporary variable and swap the cities
temp = city_1
city_1 = city_2
city_2 = temp

print(f"The name of City 1 after swapping is {city_1}")
print(f"The name of City 2 after swapping is {city_2}")


# In[2]:


# Program to check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))
if num > 0:
    print("Poditive number")
    elif num == 0:
        print("Zero")
        else:
            print("Negative number")
            


# In[3]:


# Program to check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))
if num > 0:
    print("Poditive number")
elif num = 0:
    print("Zero")
else:
    print("Negative number")


# In[4]:


# Program to check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))
if num > 0:
    print("Poditive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[5]:


# COUPE DE ESCRIVA 2023: FOOTBALL PICKS

print("Welcome to the COUPE DE ESCRIVA 2023: FOOTBALL PICKS \n")

captain = {'Madiba: ': 'Chubby Obiora-Okafo','Blue-Jays: ': 'Christopher Uweh','Cirok: ': 'Alexander', 'TSG Walkers: ': 'Ikechukwu'}

goalkeepers = {'Madiba: ': 'Chubby Obiora-Okafo',
              'Blue-Jays: ': 'Oladimeji Abaniwondea/Jeffery Awagu','Cirok: ': 'Timileyin Pearse/Izuako Jeremy',
              'TSG Walkers: ': 'Ayomide Ojikutu'}

for pick in captain:
    print(pick, captain[pick])
    
    print("\n")
    
    for pick in goalkeepers:
        print(pick, goalkeepers[pick])
        


# In[ ]:




