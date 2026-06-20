# Practicing dictionaries
# Your data can be anything
# Keys can also be immutable datatypes (just use strings)

print()

student = {'name': 'Bryan', 'id': 99897, 'age': 23, 'courses': ['Math', 'CompSci']}

print("This is what happens when you print the dictionary 'student':")
print(student)
print()

# Specify key to access!
studentName = student['name']
print("Placing student['name'] into a string:")
print(studentName)
print()

print("Placing list data from the dictionary into a variable called studentCourses, then printing it:")
studentCourses = student['courses']
print(studentCourses)
print()

# Accessing a key that doesn't exist:
# print(student['phone']) - throws error

# .get() method for dictionaries.
# Returns None if the key does not exist in the dictionary student
print(".get() method. Checks if a dictionary has a passed key. If it does, it uses it. If it doesn't, passes none:")
print(student.get('phone'))
print()

# Default value for .get() - second argument
print(".get() method but with a second argument of what to return if the key is not present")
print(student.get('phone', 'Not Found!!!'))
print()

# Adding values to a dictionary:
print("Adding a key-value pair to student: student['phone'] - '555-555-5556'")
student['phone'] = '555-555-5556'
print(student.get('phone', 'Not Found'))
print()

# Changing names. Just reset the name key: doesn't add like json(), just replaces
print("Replacing student['name'] with a different value. Similar to json(), just replaces doesn't add:")
student['name'] = 'Jane'
print(student['name'])
print()

# .update() method. Lets you change the values of multiple keys in a dictionary at once.
print(".update() method. Lets you change multiple key-values in a dictionary at one time. Pass a dictionary as argument")
print("student.update({'name': 'Bob', 'courses': ['English']}):")
student.update({'name': 'Bob', 'courses': ['English', 'Art', 'Calculus']})
print(student)
print()

# Delete a key. Very simple. Two methods
print("Delete a key-value pair in a dictionary. Very simple just del student['age']:")
del student['age']
print(student)
print()

# Pop, delete a key value pair but can store it
print("student.pop() method. Just like popping in a stack. Remove key-value pair from dictionary, but RETURN it at the same time. With courses:")
courses = student.pop('courses')
print(student)
print(courses)
print()

# Extra knowledge: .keys(), .len()
print(".keys() returns all the keys in a dictionary:")
print(student.keys())
print()
print("len(student) returns the amount of keys in a dictionary, just like len() for strings:")
print(len(student))
print()

# Iterating through a dictionary. Keys and values
print("Iteratively printing dictionary data. Use the .items() method to turn the dictionary into pairs first:")
print(student.items())
print()

print("For-each loop will print out 'first' value and 'second' value in each item in the dictionary:")
for key, value in student.items():
    print(key, value)

print()