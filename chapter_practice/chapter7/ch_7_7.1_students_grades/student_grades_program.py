# Program to input student name & grade, print two dimensional list, write list to grade.txt


def main():                                                             # define main() function
    try:                                                                # try statement
        num_students = int(input('Enter the number of students: '))     # input for student quantity
        student_grades = []                                             # initialize list for student and grade
        for student in range(num_students):               # for statement to append name & grade to student_grades list
            name = input('Enter student name: ')                        # input student name
            grade = input('Enter student\'s final letter grade: ')      # input student grade
            student_grades.append([name, grade])                        # append name and grade to student_grade list
        print(student_grades)                                           # output student & grade two dimensional list
        file_doc = open('grades.txt', 'w')                              # open to write grades.txt
        for line in student_grades:                       # for statement to write student_grades list to grade.txt
            line_out = "'" + line[0] + "', '" + line[1] + "'\n"         # value to format line for txt document
            file_doc.write(line_out)                                    # write line_out value to grade.txt
        file_doc.close()                                                # close grade.txt document
    except Exception as error:                                          # exception to print error, resume main()
        print("Error: ", error)                                         # output error message
        print()
        main()                                                          # resume main()


main()                                                                  # call main() function
