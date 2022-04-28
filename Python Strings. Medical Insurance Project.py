#uncomment the print statements to obtain the results of the exercises. The code, for now, will only print the final task: write a for loop that outputs a string for each individual 

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#Replace all instances of # in medical_data with $. Store the result in a variable called updated_medical_data.
updated_medical_data = medical_data.replace("#","$")
#print(updated_medical_data)


#To calculate the number of medical records in our data. 1. Create a variable called num_records and initialize it at 0.
num_records = 0

#2.write a for loop to iterate through the updated_medical_data string. Inside of the loop, add 1 to num_records when the current character is equal to $.
for record in updated_medical_data:
  if "$" in record:
    num_records += 1
#print(f"There are {num_records} medical records in the data.")

#Splitting Strings
#1.Splitting the updated_medical_data string into a list of each medical record.
medical_data_split = updated_medical_data.split(';')
#print(medical_data_split)

#2.Split each medical record into its own list.
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(','))
#print(medical_records)

#Cleaning Data
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

#print(medical_records_clean)

#Analyzing the Data
#to print out the names of each of the ten individuals in uppercase
#for record in medical_records_clean:
  #print(record[0].upper())

#Store each name, age, BMI, and insurance cost in separate lists.
names = [record[0] for record in medical_records_clean]
ages = [record[1] for record in medical_records_clean]
bmis = [record[2] for record in medical_records_clean]
insurance_costs = [record[3] for record in medical_records_clean]

#print(f"Names:{names}")
#print(f"Ages: {ages}")
#print(f"BMI: {bmis}")
#print(f"Insurance Costs: {insurance_costs}")

#Calculate the average BMI in our dataset
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
average_bmi = total_bmi/len(bmis)
#print(f'Average BMI: {average_bmi}')

#Calculate the average insurance cost in insurance_costs. 
#remove the $ in order to calculate the average cost
updated_insurance_costs = [cost.replace('$'," ").strip() for cost in insurance_costs]
#print(updated_insurance_costs)

#calculate the average insurance cost
total_cost = 0
for cost in updated_insurance_costs:
  total_cost += float(cost)
average_cost = total_cost/len(updated_insurance_costs)
#print(f'Average insurance cost: {average_cost}')

for n in names:
  l = names.index(n)
  print(f'{names[l]} is {ages[l]} years old with a {bmis[l]} and an insurance cost of ${updated_insurance_costs[l]}.')

