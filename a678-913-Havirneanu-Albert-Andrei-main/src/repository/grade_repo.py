from src.Validators.ValidatorException import ValidatorException
from src.domain.grade import Grade

class GradeRepo:
    def __init__(self):
        self.__grade_list = []

    def __len__(self):
        """
        getter for the length of the grade list
        :return: lenght of grade list
        """
        return len(self.__grade_list)

    @property
    def grade_list(self):
        return self.__grade_list


    @grade_list.setter
    def grade_list(self , gr_list):
        self.__grade_list = gr_list

    def search_grade_student(self , stud_id):
        """
        searches for grades based on student id
        :param stud_id: student id
        :return: Grade list
        """
        grades_list = []
        for gr in self.__grade_list:
            if gr.student_id == stud_id:
                grades_list.append(gr)
        return grades_list

    def search_grade_ass(self , ass_id):
        """
        searches for a grade based on the assignment id
        :param ass_id:
        :return:list assignment
        """
        grade_list = []
        for gr in self.__grade_list:
            if gr.assignment_id == ass_id:
                grade_list.append(gr)
        return grade_list

    def remove_grade(self , stud_id , ass_id):
        """
        removes a grade based on student and assignment id
        :param stud_id: student id
        :param ass_id: assignment id
        :return: None
        """
        for gr in self.__grade_list:
            if gr.student_id == stud_id and gr.assignment_id == ass_id:
                self.__grade_list.remove(gr)


    def add_grade(self , grade):
        """
        Adds a grade to the list. Raise error if grade already exists
        :param grade: object of class grade
        :return: Nothing
        """
        for gr in self.__grade_list:
            if gr.student_id == grade.student_id and gr.assignment_id == grade.assignment_id:
                raise ValidatorException(["Grade already exists!"])
        self.__grade_list.append(grade)

    def remove_grade_by_student(self , stud_id):
        """
        Remove all the grades from a student.
        :param stud_id: id of student
        :return: Nothing
        """
        new_grade_list = []
        for gr in self.__grade_list:
            if gr.student_id != stud_id:
                new_grade_list.append(gr)
        self.__grade_list = new_grade_list

    def remove_grade_by_assignment(self , ass_id):
        """
        Remove all the grades from an assignment.
        :param ass_id: id of assignment
        :return: Nothing
        """
        new_grade_list = []
        for gr in self.__grade_list:
            if gr.assignment_id != ass_id:
                new_grade_list.append(gr)
        self.__grade_list = new_grade_list

    def update_grade_value(self , ass_id , stud_id , new_value):
        """
        Updates the value
        :param ass_id:
        :param stud_id:
        :param new_value:
        :return:
        """
        exists = False
        for gr in self.__grade_list:
            if gr.student_id == stud_id and gr.assignment_id == ass_id:
                exists = True
                if gr.grade_value != 0:
                    raise ValidatorException(["Assignment has already been graded!"])
                else:
                    gr.grade_value = new_value
                break
        if not exists:
            raise ValidatorException(["Grade doesn't exist!"])






