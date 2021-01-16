"""
In this tutorial, you will learn to implement a school management system with Python classes and interact with it via functions
@gbazack, Jan 2021
"""
#Create a main class with common attributes and methods
#Then we create subclasses for student, teacher and course that will inherit from the main class
class Entity():
  def __init__(self, ID, names):
    self.ID= ID
    self.names= names
  
  def getID(self):
    return self.ID
  def getName():
    retunr self.names
  
  def setID(self, Id):
    self.ID= Id
  def setName(self, Name):
    self.names= Name

#Create a class Person to inherit from Entity
class Person(Entity):
  def __init__(self, age, sex):
		self.age= age
		self.sex= sex
		
	def getAge(self):
    return self.age
  def getSex():
    retunr self.sex
  
  def setAge(self, Age):
    self.age= Age
  def setSex(self, Sex):
    self.sex= Sex
		
#Create a database to save students
student=dict(ID=[1, 2], names=["Joel Ndoumbe", "Paule Hadja"], age=[1,2], level=["Master", "Master"], sex=["Male", "Female"])
#Create a database to save teacher.
teacher={'ID': [1], 'names':["Edinio Zacko"], 'age':[30], 'sex':["Male"], 'courseID':[1]}
#Create a database to register courses.
course={'ID':[1, 2], 'names':["Python programming", "Machine Learning"], 'category':["Computer Science", "Mathematics"], 'teacherID':[1,1]}
#Create a database to save the notes.
note={'ID':[1, 2, 3, 4], 'studentID':[1,2,1,2], 'courseID':[1,1,2,2], 'values':[60, 60, 50, 50]}
