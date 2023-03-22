from src.Validators.ValidatorException import ValidatorException
from src.domain.student import Student

class StudentServices():
    def __init__(self , repo , validator):
        """
        Initializez the student repo and the student validator
        :param repo: student repository
        :param validator: student validator
        """
        self.__repo = repo
        self.__validator = validator


    def get_all_students(self):
        """
        getter fot the list of students
        :return: the list of students
        """
        return self.__repo.students_list


    def student_length(self):
        """
        Method for getting the number of students
        :return: number of students
        """
        return len(self.__repo)


    def add_student(self , id , name , group):
        """
        Adds a student to the list after it's been validated
        :param id:student's id
        :param name:student's name
        :param group:student's group
        :return:Nothing
        """
        student = Student(id , name , group)
        self.__validator.validate(student)
        self.__repo.add_student(student)

    def remove_student_by_id(self , id):
        """
        Method for removing a student after it's id has been validated
        :param id: id of the student
        :return: Nothing
        """
        self.__validator.validate_id(id)
        self.__repo.remove_student_by_id(id)


    def update_name(self , id , new_name):
        """
        Method for updating the name of a student after it's been validated
        :param new_name: the new name
        :param id: id of the student to be updated
        :return: Nothing
        """
        self.__validator.validate_name(new_name)
        self.__validator.validate_id(id)
        self.__repo.update_name(id , new_name)


    def update_group(self , id , new_group):
        """
        Method for updating the name of a student after it's been validated
        :param id: id of the student to be updated
        :param new_group: the new group
        :return: Nothing
        """
        self.__validator.validate_id(id)
        self.__validator.validate_group(new_group)
        self.__repo.update_group(id , new_group)


    def search_student_by_id(self , stud_id):
        """
        searches for a student
        :param stud_id: student id
        :return: Student
        """
        return self.__repo.search_student(stud_id)

    def add_20(self):
        """
        Method for adding 20 students to the list
        :return: Nothing
        """
        self.__repo.add_20()



