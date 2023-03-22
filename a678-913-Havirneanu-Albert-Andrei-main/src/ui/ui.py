from src.domain.grade import Grade
from src.Validators.ValidatorException import ValidatorException
from src.repository.grade_repo import GradeRepo
from src.repository.assigment_repo import AssignmentRepo
from src.repository.students_repo import StudentRepo
from src.Validators.AssignmentValidator import AssignmentValidator
from src.Validators.StudentValidator import StudentValidator
from src.services.student_service import StudentServices
from src.services.assignments_services import AssignmentServices
from src.services.grade_services import GradeServices
from src.Validators.GradeValidator import GradeValidator
from src.services.undo_redo import UndoRedoService

class Ui:
    def __init__(self):
        self.__stud_repo = StudentRepo()
        self.__assignment_repo = AssignmentRepo()
        self.__gr_repo = GradeRepo()
        self.__stud_validator = StudentValidator()
        self.__assign_validator = AssignmentValidator()
        self.__grade_validator = GradeValidator()
        self.__stud_services = StudentServices(self.__stud_repo , self.__stud_validator)
        self.__assignment_services = AssignmentServices(self.__assignment_repo , self.__assign_validator)
        self.__grade_services = GradeServices(self.__stud_repo , self.__stud_validator , self.__assignment_repo , self.__assign_validator , self.__gr_repo , self.__grade_validator)
        self.__undo_redo = UndoRedoService(self.__stud_services , self.__assignment_services , self.__grade_services)


    @staticmethod
    def print_menu():
        """
        Prints menu
        :return: None
        """
        print("1 for adding a student to the list")
        print("2 for removing a student from the list")
        print("3 for updating a student's name")
        print("4 for updating a student's group")
        print("5 for printing all the students")
        print("6 for adding an assignment to the list")
        print("7 for removing an assignment from the list")
        print("8 for updating the description of an assignment")
        print("9 for updating the deadline of an assignment")
        print("10 for listing the assignments")
        print("11 for giving a student an assignment")
        print("12 for giving a group of students an assignment")
        print("13 for grading a student at an assignment")
        print("14 for printing all grades")
        print("15 for All students wh o received a given assignment, ordered descending by grade")
        print("16 for All students who are late in handing in at least one assignment")
        print("17 for Students with the best school situation, sorted in descending order")
        print("18 undo")
        print("19 redo")

    def __ui_add_student(self):
        """
        Ui function for adding a student
        :return: None
        """
        try:
            id = int(input("Id: "))
        except ValueError:
            print("Invalid id")
            return
        name = input("Name: ")
        try:
            group = int(input("Group: "))
        except ValueError:
            print("Invalid group")
            return
        try:
            self.__stud_services.add_student(id , name , group)
            self.__undo_redo.clear_redo_stack()
            self.__undo_redo.add_to_undo_stack("Sremove" , id)
        except ValidatorException as err:
            print(err)

    def __ui_remove_student(self):
        """
        Ui function for removing a student
        :return: None
        """
        try:
            id = int(input("Id:"))
        except ValueError:
            print("Invalid id!")
            return
        try:
            grades_list = self.__grade_services.search_grade_student_id(id)
            stud = self.__stud_services.search_student_by_id(id)
            self.__grade_services.remove_grade_by_student(id)
            self.__stud_services.remove_student_by_id(id)
            self.__undo_redo.clear_redo_stack()
            self.__undo_redo.add_to_undo_stack("Sadd" , [stud , grades_list])
        except ValidatorException as err:
            print(err)
            return

    def __ui_update_name(self):
        """
        Updates the name of a student
        :return: None
        """
        try:
            id = int(input("Id: "))
        except ValueError:
            print("Invalid id!")
            return
        name = input("Name: ")
        try:
            self.__undo_redo.clear_redo_stack()
            old_name = self.__stud_services.search_student_by_id(id).name
            self.__undo_redo.add_to_undo_stack("Sname" , [old_name , id])
            self.__stud_services.update_name(id , name)
        except ValidatorException as err:
            print(err)


    def __ui_update_group(self):
        """
        Updates the group of a student
        :return:
        """
        try:
            id = int(input("Id: "))
        except ValueError:
            print("Invalid id!")
            return
        try:
            group = int(input("Group"))
        except ValueError:
            print("Invalid group!")
            return
        try:
            self.__undo_redo.clear_redo_stack()
            old_group = self.__stud_services.search_student_by_id(id).group
            self.__undo_redo.add_to_undo_stack("Sgroup" , [id , old_group])
            self.__stud_services.update_group(id, group)
        except ValidatorException as err:
            print(err)


    def print_students(self):
        """
        Prints all the students
        :return: None
        """
        for stud in self.__stud_services.get_all_students():
            print(stud)


    #Assignments here we go



    def print_assignments(self):
        """
        Prints all the assignments
        :return: None
        """
        for ass in self.__assignment_services.get_all_assignments():
            print(ass)


    def __ui_add_assignment(self):
        """
        ui for adding an assingment
        :return: None
        """
        try:
            id = int(input("Id: "))
        except ValueError:
            print("invalid id!")
            return
        description = input("Description: ")
        try:
            deadline = int(input("Deadline: "))
        except ValueError:
            print("Invalid deadline!")
            return
        try:
            self.__assignment_services.add_assignment(id , description , deadline)
            self.__undo_redo.clear_redo_stack()
            self.__undo_redo.add_to_undo_stack("Aremove" , id)
        except ValidatorException as err:
            print(err)


    def __ui_remove_assignment(self):
        """
        Ui function for removing an assignment
        :return: None
        """
        try:
            id = int(input("Id: "))
        except ValueError:
            print("Invalid id!")
            return
        try:
            grade_list = self.__grade_services.search_grade_assignment_id(id)
            assignment = self.__assignment_services.find_assignment(id)
            self.__grade_services.remove_grade_by_assignment(id)
            self.__assignment_services.remove_assignment(id)
            self.__undo_redo.clear_redo_stack()
            self.__undo_redo.add_to_undo_stack("Aadd" , [assignment , grade_list])
        except ValidatorException as err:
            print(err)
            return


    def __ui_update_description(self):
        """
        Ui function for updating the description of an assignment
        :return: None
        """
        try:
            id = int(input("Id:"))
        except ValueError:
            print("Invalid id!")
            return
        description = input("Description: ")
        try:
            self.__undo_redo.clear_redo_stack()
            old_desc = self.__assignment_services.find_assignment(id).description
            self.__undo_redo.add_to_undo_stack("Adescription" , [id , old_desc])
            self.__assignment_services.update_description(id , description)
        except ValidatorException as err:
            print(err)


    def __ui_update_deadline(self):
        """
        Function for updating the deadline of an assignment
        :return:None
        """
        try:
            id = int(input("Id:"))
        except ValueError:
            print("Invalid id!")
            return
        try:
            deadline = int(input("Deadline: "))
        except ValueError:
            print("Invalid deadline!")
            return
        try:
            self.__undo_redo.clear_redo_stack()
            old_deadline = self.__assignment_services.find_assignment(id).deadline
            self.__undo_redo.add_to_undo_stack("Adeadline", [id, old_deadline])
            self.__assignment_services.update_deadline(id, deadline)
        except ValidatorException as err:
            print(err)


    #Grades here we go


    def print_grades(self):
        """
        Prints all the grades
        :return: None
        """
        for gr in self.__grade_services.get_all_grades():
            print(gr)


    def __ui_add_assignment_one_student(self):
        """
        Ui for adding an assignment to a student
        :return: None
        """
        try:
            ass_id = int(input("Assignment id: "))
        except ValueError:
            print("Invalid assignment id!")
            return
        try:
            stud_id = int(input("Student id:"))
        except ValueError:
            print("Invalid student assignment!")
            return
        grade = Grade(ass_id , stud_id , 0)
        try:
            self.__undo_redo.clear_redo_stack()
            self.__undo_redo.add_to_undo_stack("Gremove" , grade)
            self.__grade_services.add_grade_to_student(grade)
        except ValidatorException as err:
            print(err)


    def __ui_add_assignment_group(self):
        """
        Ui function for adding an assignment to a group of students
        :return: None
        """
        try:
            ass_id = int(input("Assignment id:"))
        except ValueError:
            print("Invalid assignment id!")
            return
        try:
            group = int(input("Group number: "))
        except ValueError:
            print("Invalid group number!")
            return
        try:
            self.__undo_redo.clear_redo_stack()
            self.__grade_services.add_grade_to_group(group , ass_id)
            self.__undo_redo.add_to_undo_stack("GroupRemove", [group , ass_id])
        except ValidatorException as err:
            print(err)


    def __ui_grade_student(self):
        """
        Ui function for grading a student at an assignment
        :return: None
        """
        try:
            ass_id = int(input("Assignment id: "))
        except ValueError:
            print("Invalid assignment id!")
            return
        try:
            stud_id = int(input("Student id:"))
        except ValueError:
            print("Invalid student id!")
            return
        try:
            grade_value = int(input("Grade value:"))
        except ValueError:
            print("Invalid grade value!")
            return
        try:
            self.__grade_services.update_grade_value(stud_id , ass_id , grade_value)
        except ValidatorException as err:
            print(err)


    def __ui_statistic1(self):
        try:
            ass_id = int(input("Assignment id: "))
        except ValueError:
            print("Invalid assignment id!")
            return
        try:
            l = self.__grade_services.statistic1(ass_id)
            for gr in l:
                print(gr)
            if not l:
                print("No students")
        except ValidatorException as err:
            print(err)


    def __ui_statistic2(self):
        result = self.__grade_services.statistic2()
        if not result:
            print("No students")
        for key in result:
            print(result[key])


    def __ui_statistic3(self):
        result = self.__grade_services.statistic3()
        if not result:
            print("No students")
        for element in result:
            print(f"student with id {element[0].id} and name {element[0].name} has the average grade: {element[1]}")


    def run(self):
        """
        Takes commands from the user
        :return: None
        """
        self.__stud_services.add_20()
        self.__assignment_services.add_20()
        while True:
            self.print_menu()
            command = input(">>>")
            if command == "1":
                self.__ui_add_student()
            elif command == "2":
                self.__ui_remove_student()
            elif command == "3":
                self.__ui_update_name()
            elif command == "4":
                self.__ui_update_group()
            elif command == "5":
                self.print_students()
            elif command == "6":
                self.__ui_add_assignment()
            elif command == "7":
                self.__ui_remove_assignment()
            elif command == "8":
                self.__ui_update_description()
            elif command == "9":
                self.__ui_update_deadline()
            elif command == "10":
                self.print_assignments()
            elif command == "11":
                self.__ui_add_assignment_one_student()
            elif command == "12":
                self.__ui_add_assignment_group()
            elif command == "13":
                self.__ui_grade_student()
            elif command == "14":
                self.print_grades()
            elif command == "15":
                self.__ui_statistic1()
            elif command == "16":
                self.__ui_statistic2()
            elif command == "17":
                self.__ui_statistic3()
            elif command == "18":
                self.__undo_redo.undo()
            elif command == "19":
                self.__undo_redo.redo()
            else:
                print("Invalid command.")


if __name__ == "__main__":
    ui = Ui()
    ui.run()