"""
In this tutorial, you will learn to implement a school management system with Python classes and interact with it via functions
@gbazack, Jan 2021
"""

#Create a database to save students
student=dict(ID=[1, 2], names=["Joel Ndoumbe", "Paule Hadja"], age=[1,2], level=["Master", "Master"], sex=["Male", "Female"])
#Create a database to save teacher.
teacher={'ID': [1], 'names':["Edinio Zacko"], 'age':[30], 'sex':["Male"], 'courseID':[1]}
#Create a database to register courses.
course={'ID':[1, 2], 'names':["Python programming", "Machine Learning"], 'category':["Computer Science", "Mathematics"], 'teacherID':[1,1]}
#Create a database to save the notes.
note={'ID':[1, 2, 3, 4], 'studentID':[1,2,1,2], 'courseID':[1,1,2,2], 'values':[60, 60, 50, 50]}
