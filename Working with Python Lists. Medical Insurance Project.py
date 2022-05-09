names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
#Append a new individual "Priscilla" to names and append her insurance cost, 8320.0, to insurance_costs.
names.append("Priscilla")
print(names)
insurance_costs.append(8320.0)
print(insurance_costs)

#Create a new variable called medical_records that combines insurance_costs and names into a list using the zip() function.
medical_records = list(zip(insurance_costs, names))
print(medical_records)

#We want to see how many medical records we’re dealing with. Create a variable called num_medical_records that stores the length of medical_records. (I used f-strings to print the statement in a much easier way than using "+")
num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records ")

#Select the first medical record in medical_records, and save it to a variable called first_medical_record.
first_medical_record = medical_records[0]
print(f"Here is the first medical record{first_medical_record}")

#Sort medical_records so that the individuals with the lowest insurance costs appear at the start of the list.
medical_records.sort()
print(f"Here are the medical records sorted by insurance cost: {medical_records}")

#Slice the medical_records list, and store the three cheapest insurance costs in a list called cheapest_three.
cheapest_three = medical_records[:3]
print(f"Here are the three cheapest insurance costs in our medical record: {cheapest_three}")

#Slice the medical_records list, and store the three most expensive insurance costs in a list called priciest_three.
priciest_three = medical_records[-3:]
print(f"Here are the three pricest insurance costs in our medical record: {priciest_three}")

#Count the number of occurrences of “Paul” in the names list, and store the result in a variable called occurrences_paul.
ocurrances_paul = names.count("Paul")
print(f"There are {ocurrances_paul} individuals with the name Paul in our medical records")

#Sort the medical records alphabetically by name. You’ll have to create a new list using zip() to do this.
medical_records_by_name = list(zip(names, insurance_costs))
medical_records_by_name.sort()
print(f"Here is the medical records sorted by name: {medical_records_by_name}")

#Select the medical records starting at index 3 and ending at index 7 and save it in a variable called middle_five_records.
middle_five_records = medical_records_by_name[3:8]
print(f"Here are the middle five records: {middle_five_records}")


