class Assignment:
    def __init__(self , id , desc , deadline):
        """
        Initializes an assignment
        :param id: id of the assignment
        :param desc: description of assignment
        :param deadline: deadline of assignment
        """
        self.__id = id
        self.__desc = desc
        self.__deadline = deadline

    def __str__(self):
        """
        Initializes the format in which students should be printed
        :return: Format
        """
        return f"Assignment with id {self.id} , description {self.description} and deadline {self.deadline}"

    @property
    def id(self):
        """
        getter for the id
        :return: id
        """
        return self.__id

    @property 
    def description(self):
        """
        getter for the description
        :return: description
        """
        return self.__desc

    @property
    def deadline(self):
        """
        getter for the deadline
        :return: deadline
        """
        return self.__deadline

    @description.setter
    def description(self , new_desc):
        """
        description setter
        :param new_desc: new description
        :return: Nothing
        """
        self.__desc = new_desc

    @deadline.setter
    def deadline(self , new_deadline):
        """
        deadline setter
        :param new_deadline: new deadline
        :return: Nothing
        """
        self.__deadline = new_deadline