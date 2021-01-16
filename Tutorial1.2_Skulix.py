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
		super().__init__(ID, names)
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
		
#Create a class for students
class student(Person):
	def __init__(self, level):
		super().__init__(ID, names, age, sex)
		self.level= level
	
	def getLevel(self):
		return self.level
	def setLevel(self, Level):
		self.level= Level

#Create a class for teachers
class teacher(Person):
	def __init__(self, courseID):
		super().__init__(ID, names, age, sex)
		self.courseID= courseID
	
	def getCourseID(self):
		return self.courseID
	def setCourseID(self, CourseId):
		self.courseID= CourseId

#Create a class for courses.
course={'ID':[1, 2], 'names':["Python programming", "Machine Learning"], 'category':["Computer Science", "Mathematics"], 'teacherID':[1,1]}
#Create a database to save the notes.
note={'ID':[1, 2, 3, 4], 'studentID':[1,2,1,2], 'courseID':[1,1,2,2], 'values':[60, 60, 50, 50]}
