class Student:
    def __init__(self , id , name , group):
        """
        Initializer for the student with id, name, and group. Also initializes an empty list which is the assignments
        the student has
        :param id: id of the student
        :param name: name of the students
        :param group: group in which the students belongs
        """
        self.__id = id
        self.__name = name
        self.__group = group

    def __str__(self):
        """
        Initialize the format in which the students should be printed
        :return: the format for printing students
        """
        return f"Student with id {self.id} , name {self.name} and from group {self.group}"


    @property
    def id(self):
        """
        getter for it
        :return: student's id
        """
        return self.__id

    @property
    def name(self):
        """
        getter for student's name
        :return: student's name
        """
        return self.__name

    @property
    def group(self):
        """
        getter for student's group
        :return: student's group
        """
        return self.__group

    @name.setter
    def name(self , new_name):
        """
        setter for the name of the student
        :param new_name: the new name
        :return: Nothing
        """
        self.__name = new_name

    @group.setter
    def group(self , new_group):
        """
        setter for the group of the student
        :param new_group: the new group
        :return: Nothing
        """
        self.__group = new_group


