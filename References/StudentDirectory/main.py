import os

with open("Student_Directory.txt", "r+") as f:
    Students = [tuple(map(str, i.split(','))) for i in f]                                                               #Creates list of tuples from file, using "," as a separator between elements in tuple, each newline is a seperate tuple.
Students = [tuple(ele for ele in sub if ele != "\n") for sub in Students]                                               #Removes last element from each tuple within the list, as it is just a newline character,
Students = list(Students)
get = None

class StdDir:                                                                                                           #Class used for adding new students along with correct information

    def __init__(self, stdnum, fname, lname, age):
        self.stdnum = stdnum
        self.fname = fname
        self.lname = lname
        self.age = age

    def add_student(self):
        new = (str(self.stdnum), self.lname, self.fname, str(self.age))
        Students.append(new)
        with open("Student_Directory.txt", "a") as file:                                                                #Writes to the file using proper format so that it can be read as list of tuples
            for i in Students[-1]:
                file.write(i+",")
        with open("Student_Directory.txt", "rb+") as f:                                                                 #Doesnt seem to actually do anything, but when I remove it, it breaks
            f.seek(-0, os.SEEK_END)
            f.truncate()
            f.write(b"\n")
            f.truncate()


def line_restructure():                                                                                                 #This function replaces the first character of each line,(stdnum) with the line's number
    with open("Student_Directory.txt", "r") as f:                                                                       #Useful so that when removing an entry, and later adding another entry, we dont end up with
        global Students
        x = 1                                                                                                           #duplicate stdnums, as they are now all unique based on line number.
        output = []
        for line in f:
            index_of_comma = line.index(",")
            new = str(x) + line[index_of_comma:]
            output.append(new)
            x += 1
    with open("Student_Directory.txt", "w") as f:
        f.writelines(output)
    with open("Student_Directory.txt", "r+") as f:
        Students = [tuple(map(str, i.split(','))) for i in f]
    Students = [tuple(ele for ele in sub if ele != "\n") for sub in Students]
    Students = list(Students)

# def add_student():                                                                                                      #Function to add students
#     while True:
#         stdnum = len(Students)+1
#         fname = input("First Name: ")
#         lname = input("Last Name: ")
#         age = int(input("Age: "))
#         new_student = StdDir(stdnum, fname, lname, age)
#         new_student.add_student()
#         print(fname, lname, age, "has been added to the Student Directory.")
#         get = input("Add another student? Y/N: ").lower()
#         if get != "y":
#             break


def add_student():
    while True:
        stdnum = len(Students)+1
        new = input("Enter First Name, Last Name, and Age: ")
        student = tuple(new.split(' '))
        student_add = StdDir(stdnum, student[0], student[1], student[2])
        student_add.add_student()
        print(new+" has been added to the Student Directory.")
        get = input("Add another student? Y/N: ").lower()
        if get != "y":
            line_restructure()
            break


def del_student():                                                                                                      #Function to remove students
    while True:
        while True:
            lname = input("Enter Student's last name: ")
            result = list(filter(lambda c: c[1] == lname, Students))                                                    #Looks up students lastname in the "Students" list of tuples
            if len(result) < 1:
                print("Student not found. Try Again")
            else:
                break
        for x in result:                                                                                                #Prints each student with that last name
            print(x[0], x[1], x[2], x[3])
        while True:
            try:
                verify = input("Enter Student Number of Student to verify deletion: ")
                newresult = list(filter(lambda x: x[0] == verify, result))                                              #Using the unique variable stdnum assigned to each student, we can verify the student to delete
                deletion = newresult[0]                                                                                 #and create a newvar to store the selected student.
                break                                                                                                   #Because the newvar is a list of tuples with only one element, this removes the list portion, and converts it to a newvar which is just the tuple.
            except IndexError:
                print("Student Number not found. Try Again: ")
        dellist = ""                                                                                                    #dellist used in removing the student from the Student_Directory.txt file
        print("Deleting: ", end="")
        for x in deletion:
            print(x, end=" ")
            dellist = dellist+x+","                                                                                     #creates string using each element in deletion tuple, and follows format of Student_Directory.txt
        dellist = dellist[:-1]                                                                                          #removes duplicate comma
        index = Students.index(deletion)
        f = open("Student_Directory.txt")                                                                               #From here to next comment is deleting and rewriting the Student_Directory.txt
        output = []                                                                                                     #with every line the same, except for the deleted student being removed.
        for line in f:
            if not dellist in line:
                output.append(line)
        f = open("Student_Directory.txt", "w")
        f.writelines(output)
        f.close()
        del Students[index]                                                                                             #Removes student from list of tuples at index
        line_restructure()                                                                                              #Line restructure to fix student numbers and avoid duplicates due to the adding process
        get = input("\nRemove another Student? Y/N: ").lower()
        if get != "y":
            break


def main():
    print("Bean's Student Directory v1.0")
    print("Made by: Brandon Gillis")
    print("01-10-2021")
    print(str(len(Students))+" students in directory.")
    line_restructure()
    while True:
        global get
        get = int(input("Options: "
                        "1. View Students "
                        "2. Add Students "
                        "3. Remove Students "
                        "4. Clear Directory."
                        "\nEnter choice: "))
        if get == 1:
            line_restructure()
            for x in Students:
                print(x[0], x[1], x[2], x[3])
            if input("See options? Y/N: ").lower() != "y":
                break
        elif get == 2:
            add_student()
            if input("See options? Y/N: ").lower() != "y":
                break
        elif get == 3:
            del_student()
            if input("See options? Y/N: ").lower() != "y":
                break
        elif get == 4:
            with open("Student_Directory.txt", "w") as file:
                file.write("")
            Students.clear()
            print("Directory cleared!")
            if input("See options? Y/N: ").lower() != "y":
                break
    line_restructure()


main()
