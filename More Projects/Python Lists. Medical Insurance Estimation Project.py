# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
#list called names and fill it with the names of the individuals you are estimating insurance costs
names = ["Maria", "Rohan", "Valentina"]

#list called insurance_costs with the actual amounts
insurance_costs = [4150.0, 5320.0, 35210.0]

#new empty list
estimated_insurance_data = []

#appending to the list the estimated_insurance_data
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))

#checking the code with Akira
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)
estimated_insurance_data.append(("Akira", maria_insurance_cost))

names.append("Akira")
insurance_costs.append(2930.0)

#zipping the lists
insurance_data = list(zip(names, insurance_costs))

#checking the lists
print("Here is the actual insurance cost data: "+ str(insurance_data))
print("Here is the estimated insurance cost data: "+ str(estimated_insurance_data))

#Here I created a function to calculate the difference beetween the actual insurance cost and the estimated cost, it store and return the results in a list called sustraction, this function will also work even when you add a new insuranced to the original lists.
def cost_difference(actual, estimated):
  sustraction = []
  for x in range(0,len(actual)):
    if actual[x][1] > estimated[x][1]:
      sus = actual[x][1] - estimated[x][1]
      sustraction.append((estimated[x][0], sus))
      print("The difference between the actual insurance cost (" + str(actual[x][1]) + ") and the estimated insurance cost (" + str(estimated[x][1]) + ") of " + actual[x][0] + " is: $" + str(sus) + " more.")
    if actual[x][1] < estimated[x][1]:
      sus = estimated[x][1] - actual[x][1]
      sustraction.append((estimated[x][0], sus))
      print("The difference between the actual insurance cost (" + str(actual[x][1]) + ") and the estimated insurance cost (" + str(estimated[x][1]) + ") of " + actual[x][0] + " is: $" + str(sus) + " less.")
  print ("Here is the difference insurance cost data: " + str(sustraction))
  return sustraction

insurance_cost_difference = cost_difference(insurance_data, estimated_insurance_data)



