# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = 'The estimated insurance cost for ' + name + ' is ' + str(estimated_cost) + ' dollars.'
  print(output_message)
  return estimated_cost, output_message

#Create a second function to calculate the difference between the insurance costs (given as inputs) of any two individuals
def calculate_difference(estimated_cost1, estimated_cost2):
  if estimated_cost2[0] > estimated_cost1[0]:
    difference = estimated_cost2[0]-estimated_cost1[0]
    print('The difference in insurance cost is ' + str(difference) + ' dollars.')
    return difference
  else:
    difference = estimated_cost1[0]-estimated_cost2[0]
    print('The difference in insurance cost is ' + str(difference) + ' dollars.')
    return difference

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, name ='Maria')

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35,1, 22.2, 0, 1, name='Omar')

#My own insurance cost
my_own_insurance_cost = calculate_insurance_cost(29,1, 20.3, 0, 0, name='Daniel')

#Proving difference functions
maria_omar_difference = calculate_difference(maria_insurance_cost, omar_insurance_cost)