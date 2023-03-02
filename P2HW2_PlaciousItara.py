# CTI-110
# P2HW2 - List
# Itara Placious
# Date: 3/2/23
#

#create a list
grade_list = []
grade = float(input("Enter grade for Module 1: "))
grade_list.append(grade)
print(grade_list)
grade = float(input("Enter grade for Module 2: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 3: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 4: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 5: "))
grade_list.append(grade)
grade = float(input("Enter grade for Module 6: "))
grade_list.append(grade)


print()
print('-'*12, 'Results' , '-'*12)
print('Lowest Grade:  ', min(grade_list))
print('Highest Grade: ', max(grade_list))
print('Sum of Grades:', sum(grade_list))
print('Average Grade:', format(sum(grade_list)/ len(grade_list),'.2f'))

print('-'*40)
