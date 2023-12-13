# Add your code here
#Storing patient names and insurance costs

medical_costs = {}
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

#print(medical_costs)
medical_costs["Vinay"] = 3325.0
#print(medical_costs)

#calculate the average medical cost of each patient.
total_cost = 0
for value in medical_costs.values():
  total_cost += value

average_cost = total_cost/ len(medical_costs)

print(f"Average Insurance Cost: {average_cost}")

#List Comprehension to Dictionary
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {key:value for key, value in zipped_ages}

#print(names_to_ages)

#get the value of Marina’s age and store it 
marina_age = names_to_ages.get("Marina", None)
#print(f"Marina\'s age is {marina_age}")

#Using a Dictionary to create a medical database
medical_records = {}

medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}

medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}

medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

#print(medical_records)
c_ic = medical_records["Connie"]["Insurance_cost"]
#print(f"Connie\'s insurance cost is {c_ic} dollars.")
medical_records.pop("Vinay")

#Create a function called update_medical_records() that takes in the name of an individual as well as their medical data, and then updates the medical_records dictionary accordingly.
def update_medical_records(name, age, sex, bmi, children, smoker, insurance_cost):
  new_r = {}
  new_r.update({"Age": age, "Sex": sex, "BMI": bmi, "Children": children, "Smoker": smoker, "Insurance_cost": insurance_cost})
  medical_records[name] = new_r
  return medical_records

update_medical_records("Daniel", 30, "Male", 3000, 0, "Non-Smoker", 3000.0)

#Checking the code
for key, value in medical_records.items():
  Age = value["Age"]
  Sex = value["Sex"]
  BMI = value["BMI"]
  Smoker = value["Smoker"]
  Insurance_cost = value["Insurance_cost"]
  print(f"{key} is a {Age} year old {Sex} {Smoker} with a BMI of {BMI} and insurance cost of {Insurance_cost}")