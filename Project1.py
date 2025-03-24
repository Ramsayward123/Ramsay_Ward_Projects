
# File: Project1.py
# Student: Ramsay Ward
# UT EID: rjw2777
# Course Name: CS303E
#
# Date: Oct,9,2022
# Description of Program: This program takes the users grades for their homework, projetcs, and exams and then gives their averages and final course grade with the corresponding letter grade.











def homeworkAvg(x1,y1,z1):
    tot_1 = (x1 + y1 + z1)
    return ((tot_1)/ 3)*10
def examAvg(x,y):
    tot_2 = x + y
    return tot_2/2
def projectAvg(x,y):
    tot_3 = (x + y)/2
    return tot_3
def courseGrade(courseAvg):
    if (courseAvg(s1, s2, s3) >= 90):
        return ("A")
    elif (courseAvg(s1, s2, s3) >= 80):
        return ("B")
    elif (courseAvg(s1, s2, s3) >= 70):
        return ("C")
    elif (courseAvg(s1, s2, s3) >= 60):
        return ("D")
    elif (courseAvg(s1, s2, s3) >= 0):
        return ("F")

def courseAvg(s1, s2, s3):
    return float((s1*0.30)+(s2*0.40)+(s3*0.30))
    
    







while (True):
    HW_ERROR_MESSAGE = "  Grade must be in range [0..10]. Try again."
    PR_EX_ERROR_MESSAGE = "  Grade must be in range [0..100]. Try again."

    name =( input("Enter the student's name (or 'stop'): "))
    if name == "stop":
        print("Thanks for using the grade calculator! Goodbye.")
        break
    print()
    print ("HOMEWORKS:")
    HW1 = 0
    HW2 = 0
    HW3 = 0
    while  (HW1 >= 0 or HW1 <=10 ):
        HW1 = int(input("  Enter HW1 grade: "))
        if ( 0 > HW1 or HW1 > 10):
            print (HW_ERROR_MESSAGE)
        else:
            break
    while  (HW2 >= 0 or HW2 <=10 ):
        HW2 = int(input("  Enter HW2 grade: "))
        if ( 0 > HW2 or HW2 > 10):
            print (HW_ERROR_MESSAGE)
        else:
            break
    while  (HW3 >= 0 or HW3 <=10 ):
        HW3 = int(input("  Enter HW3 grade: "))
        if ( 0 > HW3 or HW3 > 10):
            print (HW_ERROR_MESSAGE)
        else:
            break
    print()

    print ("PROJECTS:")
    Pr1 = 0
    Pr2 = 0

    while  (Pr1 >= 0 or Pr1 <=100 ):
        Pr1 = int(input("  Enter Pr1 grade: "))
        if ( 0 > Pr1 or Pr1 > 100):
            print (PR_EX_ERROR_MESSAGE)
        else:
            break
    while  (Pr2 >= 0 or Pr2 <=100):
        Pr2 = int(input("  Enter Pr2 grade: "))
        if ( 0 > Pr2 or Pr2 > 100):
            print (PR_EX_ERROR_MESSAGE)
        else:
            break
    print()

    print ("EXAMS:")
    Ex1 = 0
    Ex2 = 0
    while  (Ex1 >= 0 or Ex1 <=100 ):
        Ex1 = int(input("  Enter Ex1 grade: "))
        if ( 0 > Ex1 or Ex1 > 100):
            print (PR_EX_ERROR_MESSAGE)
        else:
            break
    while  (Ex2 >= 0 or Ex2 <=100):
        Ex2 = int(input("  Enter Ex2 grade: "))
        if ( 0 > Ex2 or Ex2 > 100):
            print (PR_EX_ERROR_MESSAGE)
        else:
            break


    s1 = homeworkAvg(HW1,HW2,HW3)
    s2 = projectAvg(Pr1, Pr2)
    s3 = examAvg(Ex1, Ex2)



    

    print()
    print("Grade report for:", name)
    print("  Homework average (30% of grade):",(format(homeworkAvg(HW1, HW2, HW3),".2f")))
    print("  Project average (30% of grade):",(format(projectAvg(Pr1, Pr2),".2f")))
    print("  Exam average (40% of grade):",(format(examAvg(Ex1, Ex2),".2f")))
    print("  Student course average:",(format(courseAvg(s1, s2, s3),".2f")))
    print("  Course grade (CS303E: Fall, 2022):",(courseGrade(courseAvg)))
    print()
    

    
