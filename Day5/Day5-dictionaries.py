############################ EXERCICE 01 ###############################
#
student = {
    "name" : "toto",
    "academic_year" : 2000
}
print("Exercice 1 : ", student)

############################ EXERCICE 02 ###############################
#
student = {
    "name" : "toto",
    "academic_year" : 2000
}
upgrade = {
    "unit" : {"name" : "java", 
              "credits" : 100, 
              "grade" : "A"} 
}
student.update(upgrade)
print("Exercice 2 : ", student)

############################ EXERCICE 03 ###############################
# 
student = {
    "name" : "toto",
    "academic_year" : 2000,
    "unit" : {"name" : "java", 
              "credits" : 100, 
              "grade" : "A"} 
}
grade_weight_mapping = {
    "A" : 4,
    "B" : 3,
    "C" : 2,
    "D" : 1,
    "E" : 0
}
student.update({"total_credits" : grade_weight_mapping})
print("Exercice 3 : ", student)

############################ EXERCICE 04 ###############################
#
student2 = student.copy()
student2["name"] = "tata"
student3 = student.copy()
student3["name"] = "titi"
students = [student, student2, student3]
print("Exercice 4 : ", students)