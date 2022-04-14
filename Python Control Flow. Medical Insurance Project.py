# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print('To lower your cost, you should consider quitting smoking.')
  else:
    'Smoking is not an issue for you.'

def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print('Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI. To be in a healthy range you need to low your BMI beetween '+ str(round(bmi_value - 25, 2)) + ' and ' + str(round(bmi_value -18.5,2)) + '.')
  elif bmi_value >= 25 and bmi_value <= 30:
    print('Your BMI is in the overweight range. To lower your cost, you should lower your BMI. To be in a healthy range you need to low your BMI beetween '+ str(round(bmi_value - 25,2)) + ' and ' + str(round(bmi_value -18.5,2)) + '.')
  elif bmi_value >= 18.5 and bmi_value < 25:
    print('Your BMI is in a healthy range. Continue like this.')
  else:
    print('Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.To be in a healthy range you need to improve your BMI beetween '+ str(round(25 - bmi_value ,2)) + ' and ' + str(round(18.5- bmi_value,2)) + '.')

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  try:
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    analyze_bmi(bmi)
    return estimated_cost, name
  except:
    if not type(name) == str:
      print('The name only accepts letters, not numbers')
    if not type(age) == int:
      print('Please, use round numbers for your age')
    if not sex == 1 or sex == 0:
      print ('Please, on your sex, use 1 for male or 0 for female')
    if not (type(bmi) == float or type(bmi) == int):
      print('Please, use numbers for bmi')
    if not type(num_of_children) == int:
      print('Please, use round numbers')
    if not smoker == 1 or smoker == 0:
      print('Please, on your smoker status, use 0 for non-smoker or 1 for smoker')
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1)

daniel_insurance_cost = estimate_insurance_cost(name = 'Daniel', age = 29, sex = 1, bmi = 20.3, num_of_children = 0, smoker = 0)

#compare insurance cost
def comparison_insurance(i1, i2):
  try:
    if i1[0] > i2[0]:
      difference = i1[0] - i2[0]
      print('The insurance cost of ' + i1[1] + ' is ' + str(i1[0]) + '.' + ' The insurance cost of ' + str(i2[1]) + ' is ' + str(i2[0]) + '.' + ' The difference between both insurance cost is ' + str(difference) + '.')
      return difference
    if i2[0] > i1[0]:
      difference = i2[0] - i1[0]
      print('The insurance cost of ' + i1[1] + ' is ' + str(i1[0]) + '.' + ' The insurance cost of ' + str(i2[1]) + ' is ' + str(i2[0]) + '.' + ' The difference between both insurance cost is ' + str(difference) + '.')
      return difference
  except:
    print('There is a mistake on the estimated insurance cost. Please review your answers.')


comparison_insurance(keanu_insurance_cost, daniel_insurance_cost)

