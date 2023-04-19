#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Project I
g_names = ('Samantha','Jdad','Claire','Elizabeth','Mary','Susan','Waje','Taibat','Lilian')
g_age = (17, 16, 17, 18, 16, 18, 17, 20, 19, 17)
g_height = (5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5)
g_scores = (80,85,70,60,76,66,87,95,50,49)

b_names = ('Charles','Jude','James','Kelvin','Biodun','Wale','Kunle','Matthew','Tom','Kayode')
b_age = (19,16,18,17,20,19,16,18,17,19)
b_height = (5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7)
b_scores = (74,84,75,68,66,78,87,98,54,50)

print("Names | Age | Height | Scores")
print("\n")

for i in range(len(g_names)):
    print(g_names[i],g_age[i],g_height[i],g_scores[i])
        
print("\n")

for i in range(10):
    print (b_names[i],b_age[i],b_height[i],b_scores[i])


# In[21]:


# Project 2
for i in range(2500):
    years_of_experience = int(input("Years of Experience is: "))
    age = int(input("Your age is: "))
    if age >= 55& years_of_experience > 25:
        print("Your Annual Tax Revenue is N5,600,000")
    elif age >= 45 & years_of_experience > 20:
        print("Your Annual Tax Revenue is N4,480,000")
    elif age >= 35 & years_of_experience > 10:
        print("Your Annual Tax Revenue is N1,500,000")
    elif age > 35 & years_of_experience < 10:
        print("Your Annual Tax Revenue is N550,000,")
    else:
        print("Invalid")
        
        


# ## 

# In[ ]:




