#Import Dependencies
from faker import Faker
import pandas as pd

#For generating fake ID 
import random

#Great Britain fake data (why not?)
fake = Faker('en_GB') 

    # dictionary 
dict_data = {
    "name":[],
    "address":[],
    "dob":[],
    "gender":[],
    "phone_number":[],
    "imei":[]
} 

#Loop through fake data    
for x in range(100):  
    dict_data["name"].append(fake.name())
    dict_data["address"].append(fake.address()) 
    dict_data["dob"].append(fake.date_of_birth()) 
    dict_data["gender"].append(fake.random.choice(['male', 'female']))
    dict_data["phone_number"].append(fake.phone_number()) 
    dict_data["imei"].append(fake.random_number(15)) 
 
# using pandas to create a data frame makes it into a more presentable format
output_data = pd.DataFrame(dict_data)
 
output_data.to_csv("fake_data.csv", header=["name", "address", "dob", "gender", "phone_number", "imei"], index=False)