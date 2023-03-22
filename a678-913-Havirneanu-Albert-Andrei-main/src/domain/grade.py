class Grade:
    def __init__(self , assignment_id , student_id , value):
        """
        initializes a grade with assignment id , student id and value
        :param assignment_id: assignment id
        :param student_id: student id
        :param value: value of the grade
        """
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__value = value

    def __str__(self):
        """
        Initializes the format in which the grades should be printed
        :return: Format
        """
        return f"Student with id {self.student_id} has the assigment with the id {self.assignment_id}. Grade: {self.grade_value}"

    @property
    def assignment_id(self):
        """
        getter the assignment id
        :return: assignment id
        """
        return self.__assignment_id

    @property
    def student_id(self):
        """
        getter the student id
        :return: student id
        """
        return self.__student_id

    @property
    def grade_value(self):
        """
        getter for the grade value
        :return: grade value
        """
        return self.__value

    @grade_value.setter
    def grade_value(self , new_value):
        """
        setter for the grade value
        :param new_value: new grade value
        :return: Nothing
        """
        self.__value = new_value
