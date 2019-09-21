#!/usr/bin/env python
# coding: utf-8

# In[37]:


name = "Julie"
age = "42"
sentence = "Hi my name is "+ name + " and I am " + age + "years old";
sentenceWithFormat = "Hi my name is {} and i am {} years old".format(name, age)
print(sentenceWithFormat)


# In[15]:


def checkCentury(year):
    if (year >= 2000 and year <= 2100):
        print("Welcome to the 21st century");
    else:
        print("You are before or after the 21st centruy");

checkCentury(1830)


# In[18]:


def tripleprint(text):
    multiplier = 3
    print(text*multiplier)

tripleprint("hello");


# In[ ]:


shoes = ["Spizikes", "Air Force 1", "Curry 2", "Melo 5"];


# In[20]:


numbers = [
    76, 83, 16, 69, 52, 78, 10, 77, 45, 52,
    32, 17, 58, 54, 79, 72, 55, 50, 81, 74,
    45, 33, 38, 10, 40, 44, 70, 81, 79, 28,
    83, 41, 14, 16, 27, 38, 20, 84, 24, 50,
    59, 71, 1, 13, 56, 91, 29, 54, 65, 23,
    60, 57, 13, 39, 58, 94, 94, 42, 46, 58,
    59, 29, 69, 60, 83, 9, 83, 5, 64, 70,
    55, 89, 67, 89, 70, 8, 90, 17, 48, 17,
    94, 18, 98, 72, 96, 26, 13, 7, 58, 67,
    38, 48, 43, 98, 65, 8, 74, 44, 92
]

for number in numbers: 
    if (number > 90):
        print(number)
        


# In[26]:


words = ["PoGo", "Spange", "Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}

for key, word in enumerate(words):
    cooldictionary[word] = definitions[key];

print(cooldictionary)


# In[36]:


class Car:
    
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def get_age(self):
        return 2019 - self.year

car = Car(2019, "honda","civic")
print(car.get_age())


# In[ ]:




