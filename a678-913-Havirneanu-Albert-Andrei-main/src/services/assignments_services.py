from src.domain.assigment import Assignment

class AssignmentServices:
    def __init__(self , repo , validator):
        """
        Initializes the repo and the validator
        :param repo: assignment repo
        :param validator: assignment validator
        :return Nothing
        """
        self.__repo = repo
        self.__validator = validator


    def assignments_length(self):
        """
        getther for the length of the assignment list
        :return: length of the assignment list
        """
        return len(self.__repo)

    def get_all_assignments(self):
        """
        getter for the list of assignments
        :return: list of assignments
        """
        return self.__repo.assignment_list

    def add_assignment(self , id , desc , deadline):
        """
        adds assignment to the list after it's validated
        :param id: assignment id
        :param desc: assignment description
        :param deadline: assignment deadline
        :return: Nothing
        """
        assignment = Assignment(id , desc , deadline)
        self.__validator.validate(assignment)
        self.__repo.add_assignment(assignment)

    def find_assignment(self , ass_id):
        return self.__repo.find_assignment(ass_id)


    def remove_assignment(self , id):
        """
        Removes assignments after it's id is validated
        :param id: assignment id
        :return: Nothing
        """
        self.__validator.validate_id(id)
        self.__repo.remove_assignment(id)


    def update_description(self , id , new_desc):
        """
        Updates the description after the id and new description are validated
        :param id: assignment id
        :param new_desc:  new description
        :return: Nothing
        """
        self.__validator.validate_id(id)
        self.__validator.validate_desc(new_desc)
        self.__repo.update_description(id , new_desc)


    def update_deadline(self , id , new_deadline):
        """
        Updates the deadline after the id and new description are validated
        :param id:asssignment id
        :param new_deadline: new deadline
        :return: Nothing
        """
        self.__validator.validate_id(id)
        self.__validator.validate_deadline(new_deadline)
        self.__repo.update_deadline(id , new_deadline)

    def add_20(self):
        """
        Adds 20 elements
        :return:
        """
        self.__repo.add_20()
