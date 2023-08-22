students = {
            "Muhammad": 20.5,
            "Saif": 25.5
            }

while True:
  new_student = input("Enter student name: ")
  if new_student == "quit":
    break
  else:
    new_score = int(input("Enter score: "))
    students[new_student] = new_score

for key, value in students.items():
  print(key, "->", value)