class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self, grade):
    if isinstance (grade,Grade):
      self.grades.append(grade)
  def get_average(self):
    sum = 0
    for grade in self.grades:
      sum += grade.score
    return sum/len(self.grades)
 

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score
  def __repr__(self):
    return str(self.score)
  def is_passing(self, grade):
    if self.score >= Grade.minimum_passing:
        return "Yes! You passed!"
    else:
        return "Sorry! You didn´t pass"

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(50))

pieter_grade = Grade(100)
pieter.add_grade(pieter_grade)

print(pieter_grade.is_passing(pieter_grade))
print(pieter.grades[3].score)
print(pieter.grades)
print(pieter.get_average())