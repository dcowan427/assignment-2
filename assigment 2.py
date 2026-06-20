# Program Name: Assignment2.py
# Course: IT3883/Section XXX
# Student Name: Deandre Cowan
# Assignment Number: Assignment 2
# Due Date: 06/XX/2026
# Purpose:
# This program reads student grade data from a file,
# calculates each student's average score, sorts the
# students by average in descending order, and prints
# the results.
#
# Resources Used:
# Course notes, textbook, and personal coding practice.

# List to store student names and averages

student_averages =[]

#open the input file for reading
with open('student.txt','r') as f:

    # process each line in the file
	for line in f:


        #remove extra spaces and split data into fields
with open("student.txt", "r") as file:
    for line in file:
        name, score = line.split()
        score = float(score)
        student_averages.append((name, score))
        for student in students:
            for line in file:
                if x > 0:
                    for line in file:

# first item is the students name
name = data[0]

#convert the six scores form stirngs to floats
scores = []
for score in data[1:]:
    scores.append(float(score))

    #calculate average
    average = sum(scores)/len(scores)

    #store names and average as a tuple
    student_averages.append((name,average))

    #sort by average by descending order
    student_averages.sort(key=lambda x: x[1], reverse=True)
#display results
print(student_averages)
print(student_averages[0][1])("------------")
for student in student_averages:
    print(f"{student[0]}: {student[1]}")

