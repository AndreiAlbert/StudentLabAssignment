from src.Validators.AssignmentValidator import AssignmentValidator
from src.domain.assigment import Assignment
from src.Validators.ValidatorException import ValidatorException
import random
import datetime

class AssignmentRepo:
    def __init__(self):
        """
        initializes the list of assignments
        """
        self.__assignment_list = []


    def __len__(self):
        """
        getter for the length of the assignment list
        :return: length of the assignment list
        """
        return len(self.__assignment_list)


    @property
    def assignment_list(self):
        """
        getter for the assignment list
        :return: assignment list
        """
        return self.__assignment_list


    def add_assignment(self , assignment):
        """
        adds an assignment to the list if it doesn't exist already
        :param assignment: object of class assignment
        :return: Nothing
        """
        for ass in self.__assignment_list:
            if ass.id == assignment.id:
                raise ValidatorException(["Asssignment already exists!"])
        self.__assignment_list.append(assignment)


    def remove_assignment(self , id):
        """
        removes assignment by id. Raise error if doesn't exist
        :param id:id of the assignment
        :return:Nothing
        """
        exists = False
        for ass in self.__assignment_list:
            if ass.id == id:
                exists = True
                self.__assignment_list.remove(ass)
        if not exists:
            raise ValidatorException(["Assignment doesn't exist!"])


    def update_description(self , id , new_desc):
        """
        Updated description of assignment. Raise error if assignment doesn't exist
        :param id:id of assignment
        :param new_desc:new description
        :return:Nothing
        """
        exists = False
        for ass in self.__assignment_list:
            if ass.id == id:
                exists = True
                ass.description = new_desc
                break
        if not exists:
            raise ValidatorException(["Assignment doesnt't exist!"])


    def update_deadline(self , id , new_deadline):
        """
        Updated deadline of an assignment. Raises error if assignment doesn't exist
        :param id: id of assignment
        :param new_deadline: new deadline
        :return:Nothing
        """
        exists = False
        for ass in self.__assignment_list:
            if ass.id == id:
                exists = True
                ass.deadline = new_deadline
                break
        if not exists:
            raise ValidatorException(["Assignment doesnt't exist!"])

    def find_assignment(self , ass_id):
        """
        Finds assignment by it's id
        :param ass_id: assignment id
        :return: assignment
        """
        for ass in self.__assignment_list:
            if ass.id == ass_id:
                return ass


    def add_20(self):
        """
        Adds 20 assignments to the list
        :return: Nothing
        """
        descriptions = ["problem1" , "problem2" , "problem3" , "problem4" , "problem5" , "problem6" , "problem7" ,
                        "problem8" , "problem9" , "problem10"]
        current_day = int(datetime.datetime.now().strftime("%d"))
        for i in range(1 , 21):
            self.__assignment_list.append(Assignment(i , random.choice(descriptions) , random.randint(current_day + 1 , 31)))

        #these are just to show that the 2nd statistic works
        self.__assignment_list.append(Assignment(21 , random.choice(descriptions) , 1))
        self.__assignment_list.append(Assignment(22 , random.choice(descriptions) , 1))




