#project1: Basic School administrationTool
import csv
def write_into_csv(info_list):
    with open('student_info.csv' , 'a', newline= '') as csv_file:
        writer   = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name","Age","Contact Number","Email Id"])
        writer.writerow(info_list)
if __name__ == '__main__':
    condition = True
    student_num = 1
    while condition:
        student_info  = input("Enter some Student Information for Student {} in the following format(Name,Age,Contact No,Email Id) :  ".format(student_num))
        Student_info_list = student_info.split(',')
        print("\nThe Entered information is - \nName: {}\nAge: {}\nContact Number: {}\nEmail Id: {}".format(Student_info_list[0],Student_info_list[1],Student_info_list[2],Student_info_list[3]))
        

        choice_check = input("Is the Entered information is Correct?")
        choice_check=choice_check.casefold()
        if choice_check == "yes":
            write_into_csv(Student_info_list)
            student_num = student_num + 1
            
            condition_check =  input("Enter Yes or No if you want to Enter a Information of a Student:   ")
            condition_check=condition_check.casefold()
            if condition_check == "no":
                condition =  False
            elif condition_check == "yes":
                condition  = True
        elif choice_check == "no":
            print("Please re-enter the Information")
        
            
