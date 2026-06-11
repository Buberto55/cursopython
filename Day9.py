# Dictionaries
# Create
prog_dic = {
    "Bug" : "An error in a program that preveents the program from running as expected.",
    "Function" : "A piece ofr code that you can easly call over an over again",
    "Loop" : "The action of doing something over an over again"
}

print(prog_dic["Function"])
print(prog_dic)

# Edit
prog_dic["Bug"] = "Una pelucita en tu compu"

# Clear
empty_dictionary = {}

#prog_dic = {}

print(prog_dic)

for thing in prog_dic:
    print(thing)
    print(prog_dic[thing])

# Exercise 9: Grading program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key, value in student_scores.items():
    print(key, value)
    if 100 > value > 90:
        student_grades[key] = "Outstanding"
    elif 90 > value > 80:
        student_grades[key] = "Exceeds Expectations"
    elif 80 > value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# Nesting
# we can have a dictionary and a list inside a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon-"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])