number_of_labs = int(input("Enter the number of labs completed: "))
if number_of_labs > 6:
    number_of_labs = 6

number_of_quizzes_andor_inclass_activities = int(input("Enter the number of quizzes completed: "))
if number_of_quizzes_andor_inclass_activities > 6:
    number_of_quizzes_andor_inclass_activities = 6

Assignment1_grade = float(input("Enter grade for Assignment 1: "))
Assignment2_grade = float(input("Enter grade for Assignment 2: "))
Assignment3_grade = float(input("Enter grade for Assignment 3: "))
Assignment4_grade = float(input("Enter grade for Assignment 4: "))

Midterm1_grade = float(input("Enter grade for Midterm 1: "))
Midterm2_grade = float(input("Enter grade for Midterm 2: "))
FinalExam_grade = float(input("Enter grade for Final Exam: "))
Midterm_and_Final_prep = float(input("Enter grade for Midterms and Final Preparation: "))

labs_weighted_grade = ((number_of_labs/6)*100*0.2)
quizzes_andor_inclass_weighted_grade = ((number_of_quizzes_andor_inclass_activities/6)*100*0.15)
weighted_assignments_grade = (((Assignment1_grade + Assignment2_grade + Assignment3_grade + Assignment4_grade)/4)*0.16)
weighted_midterms_grade = (((Midterm1_grade + Midterm2_grade)/2)*0.25)
weighted_finalexam_grade = (FinalExam_grade*0.18)
weighted_examprep_for_midterm_and_final = (Midterm_and_Final_prep*0.06)

Total_grade = (labs_weighted_grade + quizzes_andor_inclass_weighted_grade + weighted_assignments_grade + weighted_midterms_grade + weighted_finalexam_grade + weighted_examprep_for_midterm_and_final)
print("Your Grade is:", round(Total_grade,2), "%")

