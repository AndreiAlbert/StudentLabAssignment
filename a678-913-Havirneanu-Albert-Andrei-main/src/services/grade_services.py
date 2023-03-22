from src.Validators.ValidatorException import ValidatorException
from src.domain.grade import Grade
import datetime

class GradeServices:
    def __init__(self , stud_repo , stud_valid , ass_repo , ass_valid , grade_repo , grade_valid):
        """
        Initialize the class with repos and validators from assignments and students
        :param stud_repo:  student repo
        :param stud_valid: student validator
        :param ass_repo: assignment repo
        :param ass_valid: assignment validator
        :param grade_repo: grade repo
        :param grade_valid: grade validator
        """
        self.__stud_repo = stud_repo
        self.__stud_valid = stud_valid
        self.__ass_repo = ass_repo
        self.__ass_valid = ass_valid
        self.__grade_repo = grade_repo
        self.__grade_valid = grade_valid

    def get_grade_length(self):
        """
        getter for the length of grade list
        :return: length of grade list
        """
        return len(self.__grade_repo)

    def get_all_grades(self):
        """
        getter for the grade list
        :return: grade list
        """
        return self.__grade_repo.grade_list


    def search_grade_student_id(self , stud_id):
        return self.__grade_repo.search_grade_student(stud_id)

    def search_grade_assignment_id(self , ass_id):
        return self.__grade_repo.search_grade_ass(ass_id)

    def remove_grade(self , stud_id , ass_id):
        self.__grade_repo.remove_grade(stud_id , ass_id)


    def remove_grade_group(self , group , ass_id):
        new_grade_list = []
        for gr in self.__grade_repo.grade_list:
            if self.__stud_repo.search_student(gr.student_id).group != group and gr.assignment_id != ass_id:
                new_grade_list.append(gr)
        self.__grade_repo.grade_list = new_grade_list


    def add_grade_to_student(self , grade):
        """
        adds a grade to the list
        :param grade: object of class grade
        :return: Nothing
        """
        self.__stud_valid.validate_id(grade.student_id)
        self.__ass_valid.validate_id(grade.assignment_id)
        self.__grade_valid.validate_value(grade.grade_value)
        exists_student = False
        exists_ass = False
        for stud in self.__stud_repo.students_list:
            if stud.id == grade.student_id:
                exists_student = True
                break
        if not exists_student:
            raise ValidatorException(["Student doens't exist!"])
        for ass in self.__ass_repo.assignment_list:
            if ass.id == grade.assignment_id:
                exists_ass = True
                break
        if not exists_ass:
            raise ValidatorException(["Assignment doesn't exist!"])
        if exists_ass and exists_student:
            self.__grade_repo.add_grade(grade)


    def add_grade_to_group(self , group_number , ass_id):
        """
        Adds an assignment to all the students of a group
        :param group_number: group number
        :param ass_id: assignment id
        :return: Nothing
        """
        self.__stud_valid.validate_group(group_number)
        self.__ass_valid.validate_id(ass_id)
        exists_group = False
        exists_ass = False
        for stud in self.__stud_repo.students_list:
            if stud.group == group_number:
                exists_group = True
                break
        if not exists_group:
            raise ValidatorException(["Group doesn't exist!"])
        for ass in self.__ass_repo.assignment_list:
            if ass.id == ass_id:
                exists_ass = True
                break
        if not exists_ass:
            raise ValidatorException(["Assignment doesn't exist!"])
        if exists_ass and exists_group:
            for stud in self.__stud_repo.students_list:
                if stud.group == group_number:
                    self.__grade_repo.add_grade(Grade(ass_id , stud.id , 0))

    def remove_grade_by_student(self , stud_id):
        """
        Removes all the grades by a student
        :param stud_id: student id
        :return: Nothing
        """
        self.__grade_repo.remove_grade_by_student(stud_id)


    def remove_grade_by_assignment(self , ass_id):
        """
        Removes all the grades by an assignment
        :param ass_id: assignment id
        :return: Nothing
        """
        self.__grade_repo.remove_grade_by_assignment(ass_id)


    def update_grade_value(self , stud_id , ass_id , value):
        """
        Gives grade to a student at an assignemtn
        :param stud_id: student id
        :param ass_id: assignment id
        :param value: grade value
        :return:
        """
        self.__stud_valid.validate_id(stud_id)
        self.__ass_valid.validate_id(ass_id)
        self.__grade_valid.validate_value(value)
        exists_student = False
        exists_ass = False
        for ass in self.__ass_repo.assignment_list:
            if ass.id == ass_id:
                exists_ass = True
                break
        if not exists_ass:
            raise ValidatorException(["Assignment doesn't exist!"])
        for stud in self.__stud_repo.students_list:
            if stud.id == stud_id:
                exists_student = True
                break
        if not exists_student:
            raise ValidatorException(["Student doesn't exist!"])
        if exists_ass and exists_student:
            self.__grade_repo.update_grade_value(ass_id , stud_id , value)

    def statistic1(self , ass_id):
        auxiliar_list = []
        ass_exists = False
        for ass in self.__ass_repo.assignment_list:
            if ass.id == ass_id:
                ass_exists = True
        if not ass_exists:
            raise ValidatorException(["Assignment doesn't exist"])
        ass_exists = False
        for gr in self.__grade_repo.grade_list:
            if gr.assignment_id == ass_id:
                ass_exists = True
        if not ass_exists:
            raise ValidatorException(["There are no students with this assignment!"])
        for gr in self.__grade_repo.grade_list:
            if gr.assignment_id == ass_id and gr.grade_value != 0:
                auxiliar_list.append(gr)
        auxiliar_list.sort(key = lambda x : x.grade_value , reverse=True)
        return auxiliar_list


    def statistic2(self):
        dict = {}
        current_day = int(datetime.datetime.now().strftime("%d"))
        for gr in self.__grade_repo.grade_list:
            if self.__ass_repo.find_assignment(gr.assignment_id).deadline < current_day and gr.grade_value == 0:
                if gr.student_id not in dict.keys():
                    dict[gr.student_id] = self.__stud_repo.search_student(gr.student_id)
        return dict


    def statistic3(self):
        result = []
        for stud in self.__stud_repo.students_list:
            sum = 0
            counter = 0
            for gr in self.__grade_repo.grade_list:
                if gr.student_id == stud.id and gr.grade_value != 0:
                    sum += gr.grade_value
                    counter += 1
            if sum != 0:
                result.append([stud , sum / counter])
        result.sort(key = lambda x : x[1] , reverse=True)
        return result


