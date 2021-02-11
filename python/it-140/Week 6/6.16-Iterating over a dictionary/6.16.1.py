# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}


# Print the name and grade percentage of the student
 # with the highest total of points
highest_name = next(iter(student_grades))
highest_total_of_points = sum(student_grades[highest_name])
for name, lst in student_grades.items():
  total_of_points = sum(lst)
  if total_of_points > highest_total_of_points:
    highest_name = name
    highest_total_of_points = total_of_points
print('{}: {:.2f}%'.format(highest_name, highest_total_of_points / 5))


# Find the average score of each assignment
average_scores = {}
assignments = ('A1', 'A2', 'A3', 'A4', 'A5')
 #scores = [0 for i in range(5)]
scores = [0] * 5
for name in student_grades.keys():
  lst = student_grades[name]
  for i in range(5):
    scores[i] += 0.2 * lst[i]
for i in range(len(assignments)):
  average_scores[assignments[i]] = scores[i]
for ass, scr in sorted(average_scores.items()):
  print('{}: {:.2f}'.format(ass, scr))



 # Find and apply a curve to each student's total score,
 # such that the best student has 100% of the total points.
new_student_grades = student_grades
highest_grades = student_grades[highest_name]
grades = []
for name, lst in student_grades.items():
  new_lst = []
  for i in range(len(lst)):
    new_lst.append(lst[i] * (1 / highest_grades[i] * 100))
  new_student_grades[name] = new_lst
for name, lst in student_grades.items():
  print('{:8s}: '.format(name) + ', '.join(['{:8.2f}'.format(j) for j in lst]))