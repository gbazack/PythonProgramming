## Tutorial 1: School Management System 1

In this tutorial, you will learn how to implement a school management system with Python data structures such as list and dictionary and interact with it via functions. More precisely, you'll learn to
1. Create databases:
   1. A database to save students’ information. This information includes the student’s identification number, names, age, level, sex.
   2. A database to save teacher’s (lecturer) information such as his/her ID, name, age, sex, course ID.
   3. A database to register courses. Each course is described by an ID, title, category, lecturer ID.
   4. A database to save the notes. Notes should have the following attributes: Note ID, student ID, Course ID, and values.
2. Manipulate these databases:
   1. Search items from
   2. Add items to
   3. Remove items from
   4. Modify items of

For more information, visit our YouTube channel via [https://www.youtube.com/channel](https://www.youtube.com/channel/UCBqqJWMUr74vAtl65ZWc20A/featured) and subscribe to get notified whenever there's a new video.

```python
#Create a database to save students
student=dict(ID=[1, 2], names=["Joel Ndoumbe", "Paule Hadja"], age=[1,2], level=["Master", "Master"], sex=["Male", "Female"])
#Create a database to save teacher
teacher={'ID': [1], 'names':["Edinio Zacko"], 'age':[30], 'sex':["Male"], 'courseID':[1]}
#Create a database to register courses.
course={'ID':[1, 2], 'titles':["Python programming", "Machine Learning"], 'category':["Computer Science", "Mathematics"], 'teacherID':[1,1]}
#Create a database to save the notes
note={'ID':[1,2], 'studentID':[1,2], 'courseID':[1,1], 'values':[60,60]}


1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/gbazack/PythonProgramming/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
