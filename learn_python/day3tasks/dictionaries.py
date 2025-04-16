# Make a dictionary called "student_1" - python dictionaries seem like JS objects to me (key-value pairs)
student_1 = {
    "name" : "susan",
    "stream" : "tech",
    "completed_lessons" : 4,
    "completed_lesson_names" : ["variables", "data_types", "set up"]
    }

# How do dictionaries save data? Key-value pairs.
print(student_1, type(student_1))

# Accessing a value in the dictionary
print(student_1["stream"])

# Printing the value of "completed_lesson_names"
print(student_1["completed_lesson_names"])

# Printing data type of "completed_lesson_names"
print(type(student_1["completed_lesson_names"]))

# Print the first element/item in the list "completed_lesson_names"
print(student_1["completed_lesson_names"][0])

# Change the value of "completed_lessons" to 3, the integer
print(student_1["completed_lessons"])
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Delete data types from the list of "completed_lesson_names".
# Going into the list and finding the key "completed_lesson_names", then popping element 1
print(student_1["completed_lesson_names"])
student_1["completed_lesson_names"].pop(1)
print(student_1["completed_lesson_names"])

# Use the keys method to print all the keys in a dictionary
print(student_1.keys())