#definí clase Patient para almacenar la información de los pacientes
class Patient:
  def __init__(self, patient_info):
      self.name = patient_info[0][1]
      self.age = patient_info[1][1]
      self.sex = patient_info[2][1] 
      self.bmi = patient_info[3][1]
      self.num_children = patient_info[4][1]
      self.smoker = patient_info[5][1]

  #Calcular el estimated_insurance_cost
  def estimated_insurance_cost(self):
    #verificar que tanto smoker como sexo se registraran sólo con 0 o 1.
    try:
      if self.sex == 0 or self.sex == 1:
        if self.smoker == 0 or self.smoker == 1:
          estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_children + 24000 * self.smoker - 12500
          print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))
        else:
          print("You must register 0 for non-smoker or 1 for smoker.")
      elif self.smoker == 0 or self.smoker == 1:
        if self.sex == 0 or self.sex == 1:
          estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_children + 24000 * self.smoker - 12500
          print("{}'s estimated insurance costs is {} dollars.".format(self.name, estimated_cost))
        else:
          print("You must register 0 for male or 1 for female.")
      else:
        print("You must register 0 for male or 1 for female.")
        print("You must register 0 for non-smoker or 1 for smoker.")
    except:
      print("You must register the information with integers.")
  #función para permitir actualizar el nombre, el isinstance permite que se actualice solamente con str
  def correct_name(self, new_name):
    if isinstance(new_name, str):
      self.name = new_name
      print("The name has been corrected to {}.".format(self.name))
      self.estimated_insurance_cost()
    else:
      print("You can't change a name for a number.")
   #función para permitir actualizar la edad
  def update_age(self, new_age):
    self.age = new_age
    print("{} is now {} years old.".format(self.name, self.age))
    self.estimated_insurance_cost()
  #función para actualizar el número de hijos con opciones de un 1 hijo o más.
  def update_num_children(self, new_num_children):
    self.num_children = new_num_children
    if new_num_children == 1:
      print("{} has {} child.".format(self.name, self.num_children))
    else:
      print("{} has {} children.".format(self.name, self.num_children))
    self.estimated_insurance_cost()
  #función para actualizar el bmi
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{} has now a BMI of {}.".format(self.name, self.bmi))
    self.estimated_insurance_cost()
  #función para actualizar el status de fumador
  def update_smoking_status(self, new_status):
    self.smoker = new_status
    if new_status == 0:
      print("{} is non-smoker.".format(self.name))
    if new_status == 1:
      print("{} is smoker.".format(self.name))
    self.estimated_insurance_cost()
    if new_status > 1 or new_status < 0:
      pass
  #función para obtener la información del paciente en un diccionario
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Num of children"] = self.num_children
    patient_information["Smoker"] = self.smoker
    return patient_information
    
patient1 = Patient([("Name","John Doe"), ("Age",25), ("Sex", 0), ("BMI", 22.2), ("Num of children", 0), ( "Smoker", 0)])

#tests
print(patient1.name)
print(patient1.age)
print(patient1.sex)
print(patient1.bmi)
print(patient1.num_children)
print(patient1.smoker)

patient1.estimated_insurance_cost()
patient1.update_num_children(8)
patient1.update_smoking_status(1)
patient1.update_bmi(19)
patient1.correct_name("Odiseo")

print(patient1.patient_profile())