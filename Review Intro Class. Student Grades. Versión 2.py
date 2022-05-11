#Import datetime and date from datetime to do the attendance method
from datetime import datetime
from datetime import date

#Define a class Student
class Student():
#Add a constructor for Student. Have the constructor take in two parameters: a name and a year
  def __init__(self, name, year):
    self.name = name
    self.year = year
#In the body of the constructor for Student, declare self.grades as an empty list.
    self.grades = []
#Add an instance variable to Student that is a dictionary called .attendance
    self.attendance = {}
#Add an .add_grade() method to Student that takes a parameter, grade.
  def add_grade(self, grade):
    if isinstance (grade, Grade):
      #Verify that grade is of type Grade and if so, add it to the Student‘s .grades.
      self.grades.append(grade)
    else:
      #If grade isn’t an instance of Grade then .add_grade() should do nothing.
      pass
  def get_average(self):
    #Write a Student method get_average() that returns the student’s average score.
    sum = 0
    for grade in self.grades:
      sum += grade.score
    return sum/len(self.grades)
#set_attendance method to fill self.attendance dictionary with dates as keys and booleans as values that indicate whether the student attended school that day.
  def set_attendance(self, day, value):
    fecha_dt = datetime.strptime(day, '%d/%m/%Y')
    new_date = date(fecha_dt.year, fecha_dt.month, fecha_dt.day).isoformat()
    if value == 1:
      self.attendance.update({new_date: True})
    if value == 0:
      self.attendance.update({new_date: False})
    return self.attendance

#Create three instances of the Student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8) 

#Create Grade class, with minimum_passing as an attribute set to 65.
class Grade():
  minimum_passing = 65
#Give Grade a constructor. Take in a parameter score and assign it to self.score
  def __init__(self, score):
    self.score = score
  def __repr__(self):
    return str(self.score)
  def is_passing(self, score):
    #Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
    if self.score >= Grade.minimum_passing:
      return "You passed!"
    else:
      return "You failed!"



#Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().
pieter_grade = Grade(100)
pieter.add_grade(pieter_grade)

#tests
pieter.add_grade(Grade(60))
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(50))
pieter.set_attendance("20/04/2019", 1)
pieter.set_attendance("21/04/2019", 0)
pieter.set_attendance("21/05/2020", 1)
pieter.set_attendance("30/07/2022", 1)
print(pieter.attendance)
print(pieter.grades[1].score)
print(pieter_grade.is_passing(pieter_grade))
print(pieter.grades[2].score)
print(pieter.get_average())
