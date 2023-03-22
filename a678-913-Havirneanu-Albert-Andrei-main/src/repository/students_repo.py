import random
from src.domain.student import Student
from src.Validators.StudentValidator import StudentValidator
from src.Validators.ValidatorException import ValidatorException

class StudentRepo:
    def __init__(self):
       """
       Initialize the list of students
       """
       self.__students_list = []


    @property
    def students_list(self):
        """
        getter for the list of students
        :return: list of students
        """
        return self.__students_list

    def __len__(self):
        """
        Method for determining the length of the students list
        :return: length of the students list
        """
        return len(self.__students_list)


    def add_student(self , student):
        """
        Method for adding a new student to the list. Raise error if students already exists
        :param student: object of the Student class
        :return: Nothing
        """
        for stud in self.__students_list:
            if student.id == stud.id:
                raise ValidatorException(["Student already exists!"])
        self.__students_list.append(student)


    def remove_student_by_id(self , id):
        """
        Method for removing a student based on id. Raise error if id doesn't exist
        :param id:id of the student to be removed
        :return:Nothing
        """
        exists = False
        for stud in self.__students_list:
            if stud.id == id:
                exists = True
                self.__students_list.remove(stud)
                break
        if not exists:
            raise ValidatorException(["Id doesn't exist!"])


    def update_name(self , id , new_name):
        """
        Update the name of a student. Raise error if the id of the student doesn't exist
        :param id: id of the student to be updated
        :param new_name: the new name
        :return: Nothing
        """
        exists = False
        for stud in self.__students_list:
            if stud.id == id:
                exists = True
                stud.name = new_name
                break
        if not exists:
            raise ValidatorException(["id doesn't exist!"])


    def update_group(self , id , new_group):
        """
        Update the name of a student. Raise error if the id of the student doesn't exist
        :param id: id of the student to be updated
        :param new_group: the new group
        :return:Nothing
        """
        exists = False
        for stud in self.__students_list:
            if stud.id == id:
                exists = True
                stud.group = new_group
                break
        if not exists:
            raise ValidatorException(["id doesn't exist!"])

    def search_student(self , stud_id):
        """
        Search for a student by it's id
        :param stud_id: id of the student
        :return: student we're lookin' for
        """
        for stud in self.__students_list:
            if stud.id == stud_id:
                return stud

    def add_20(self):
        """
        Adds 20 students to the list
        :return: Nothing
        """
        name_list = ["Shrek" , "Johny" , "Juan" , "Carlos" , "Mega Juan" , "Corneliu" , "Tudor"  , "Mihai" , "Steve",
                     "Aoki"]
        for i in range(1 , 21):
            self.__students_list.append(Student(i , random.choice(name_list) , random.randint(1 , 10)))





