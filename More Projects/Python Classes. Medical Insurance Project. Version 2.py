class Patient:
  def __init__(self, patient_info):
    self.name = patient_info[0][1]
    self.age = patient_info[1][1]
    # add more parameters here
    self.sex = patient_info[2][1]
    self.bmi = patient_info[3][1]
    self.num_of_children = patient_info[4][1]
    self.smoker = patient_info[5][1]
  #method to calculate the estimated_insurance_cost
  def estimated_insurance_cost(self):
    try:
#the isinstance protects the string, it allows only to pass str as names, no numbers.
      if isinstance(self.name, str):
        estimated_cost= 250 * self.age - 128 * self.sex  + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
      print(f"{self.name}'s estimated insurance cost is {estimated_cost} dollars.")
    except:
      if not isinstance(self.sex, int):
        print ("You must register you sex with 0 for male and 1 for female.")
      if not isinstance(self.smoker, int):
        print ("You must register your smoker status with 0 for non-smoker and 1 for smoker.")
      if not isinstance(self.name, str):
        print("You must register your name using just letters.")
      if not isinstance(self.num_of_children, int):
        print("You must register the number of children using numbers.")
      if not isinstance(self.age, int):
        print("You must your age using numbers.")
#Suposse that a patient was a John Doe, but now he/she has a name, we will need to update the name, so, i write this method
  def update_name(self, new_name):
    if isinstance(new_name, str):
      self.name = new_name
      self.estimated_insurance_cost()
    else:
      print("Please, update the name using just letters.")
#This method update the sex status, just in case…
  def update_sex(self, new_sex):
    if isinstance(new_sex, int) and new_sex == 0 or new_sex == 1 and isinstance(self.name, str):
      self.sex = new_sex
      self.estimated_insurance_cost()
    else:
      print("You must register you sex with 0 for male and 1 for female.")
#method to update the patient's age
  def update_age(self, new_age):
    try:
#the isinstance protects the string, it allows only to pass str as names, no int and int as age no str.
      if 0 < new_age <= 100 and isinstance(self.name, str) and isinstance(new_age, int):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")
        self.estimated_insurance_cost()
      if new_age > 100:
        print("It only allows an age's range from 1 to 100")
    except:
      print("You must register the new age using just numbers.")
#method to update_num_of children
  def update_num_of_children(self, new_num_children):
    self.num_of_children = new_num_children
    try:
#the isinstance protects the string, it allows only to pass str as names, no numbers (because 40 can't have children)
        if self.num_of_children == 1 and isinstance(self.name, str):
          print(f"{self.name} has {self.num_of_children} child.")
        elif self.num_of_children == 0 and isinstance(self.name, str):
          print(f"{self.name} has no children.")
        elif self.num_of_children > 1 and isinstance(self.name, str):
          print(f"{self.name} has {self.num_of_children} children.")
    except:
      print("Verify your data type")
    self.estimated_insurance_cost()
#method to update the smoker status, again the isinstance protects the string and allows only to pass str as names.
  def update_smoker_status(self, new_smoker_status):
    self.smoker = new_smoker_status
    try:
        if self.smoker == 1 and isinstance(self.name, str):
          print(f"{self.name} smokes")
        elif self.smoker == 0 and isinstance(self.name, str):
          print(f"{self.name} doesn't smoke.")
        elif self.smoker > 1 or self.smoker < 0 and isinstance(self.name, str):
          print("You must register your smoker status with 0 for non-smoker and 1 for smoker.")
    except:
      print("Verify your data type.")
    self.estimated_insurance_cost()
#method to update bmi
  def update_bmi(self, new_bmi):
    if isinstance(self.name, str) and isinstance(new_bmi, int) or isinstance(new_bmi, float):
      self.bmi = new_bmi
      print(f"{self.name}'s new BMI is: {self.bmi}")
    else:
      print("Register BMI using numbers")
#method to obtain patient's profle
  def patient_profile(self):
    try:
      if isinstance(self.name, str) and isinstance(self.age, int) and isinstance(self.sex, int) and isinstance(self.num_of_children, int) and isinstance(self.smoker, int):
        if 0 < self.age <= 100 and self.sex == 1 or self.sex == 0 and self.smoker == 0 or self.smoker == 1:
          patient_information = {}
          patient_information["Name"] = self.name
          patient_information["Age"] = self.age
          patient_information["Sex"] = self.sex
          patient_information["BMI"] = self.bmi
          patient_information["Children"] = self.num_of_children
          patient_information["Smoker"] = self.smoker
          return patient_information
        else:
          return "Please, verify that your data is in correct format. Otherwise, we can not access to patient information."
    except:
      return "Please, verify that your data is in correct format. Otherwise, we can not access to patient information."

#tests:

patient1 = Patient([("name", "John"), ("Age", 25), ("Sex", 0), ("BMI", 22.2), ("Num of children", 7), ("Smoker", 1)])
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_of_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_name("Carol")
patient1.update_age(100)
patient1.update_bmi(23.5)
patient1.update_num_of_children(2)
patient1.update_smoker_status(0)
patient1.update_sex(0)
print(patient1.patient_profile())
