name = input("Enter the student's name: ")
no_of_subjects = int(input("Enter the number of subjects: "))
subjects = []
marks = []

for i in range(no_of_subjects):
    user = input(f"Enter the name and marks of subject {i+1} (Comma-Separated): ")
    data = user.split(",")
    subjects.append(data[0])
    marks.append(int(data[1]))

average = float(sum(marks)/len(marks))

print("Result:")
for subject, mark in zip(subjects, marks):
    if mark >= 80:
        print(f"Subject: {subject}, Marks: {mark}, Grade: A")
    elif mark >= 60:
        print(f"Subject: {subject}, Marks: {mark}, Grade: B")
    elif mark >= 50:
        print(f"Subject: {subject}, Marks: {mark}, Grade: C")
    elif mark >= 35:
        print(f"Subject: {subject}, Marks: {mark}, Grade: D")
    else:
        print(f"Subject: {subject}, Marks: {mark}, Grade: F")

if average >= 33:
    print(f"Average: {average}, {name} You are passed!")
else:
    print(f"Average: {average}, {name} You are failed!")
 