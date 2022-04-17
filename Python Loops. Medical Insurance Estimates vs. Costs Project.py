names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
#Create a variable total_cost and initialize it to 0 then use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.
total_cost = 0
total_cost2 = 0
for cost in actual_insurance_costs:
  total_cost += cost
  print(total_cost)

#The same but with a while loop
length = len(actual_insurance_costs)
index = 0
while index < length:
  total_cost2 += actual_insurance_costs[index]
  index += 1
  #print(total_cost2)


#create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.
average_cost = total_cost/ len(actual_insurance_costs)

print(f'Average Insurance Cost: {average_cost} dollars.')

#Write a for loop with variable i that goes from 0 to len(names). Create a variable name, which stores names[i]. Create a variable insurance_cost, which stores actual_insurance_costs[i].Then inside of the for loop, use if, elif, else statements after the print statement to check whether the insurance cost is above, below, or equal to the average.
for i in range(0, len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  estimated_cost = estimated_insurance_costs[1]
  how_far = average_cost - estimated_cost
  print(f'The insurance cost for {name} is {insurance_cost} dollars.')
  if insurance_cost > average_cost:
    print(f'The insurance cost for {name} is above average for {how_far} dollars.')
  elif insurance_cost < average_cost:
    print(f'The insurance cost for {name} is below average for {how_far} dollars.')
  else:
    print(f'The insurance cost for {name} is equal to the average.')


#Using a list comprehension, create a new list called updated_estimated_costs, which has each element in estimated_insurance_costs multiplied by 11/10.
updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

print(updated_estimated_costs)








