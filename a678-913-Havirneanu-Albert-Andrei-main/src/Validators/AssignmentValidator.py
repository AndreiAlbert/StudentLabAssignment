from src.domain.assigment import Assignment
from src.Validators.ValidatorException import ValidatorException
import datetime

class AssignmentValidator:
    @staticmethod
    def validate(assigment):
        error = []
        if isinstance(assigment , Assignment) is False:
            error.append("It's not a discipline!")
        if int(assigment.id) < 1:
            error.append("Id must be a positive integer!")
        if not(assigment.description or assigment.description.strip()):
            error.append("Description mustn't be empty!")
        if int(assigment.deadline) < int(datetime.datetime.now().strftime("%d")):
            error.append("Deadline can't be before the current day!")
        if int(assigment.deadline) < 1 or int(assigment.deadline) > 31:
            error.append("Deadline must be an integer between 1 and 31")
        if len(error) > 0:
            raise ValidatorException(error)

    @staticmethod
    def validate_id(id):
        error = []
        if int(id) < 1:
            error.append("Id must be a positive integer!")
        if len(error) > 0:
            raise ValidatorException(error)

    @staticmethod
    def validate_desc(description):
        error = []
        if not (description or description.strip()):
            error.append("Description mustn't be empty!")
        if len(error) > 0:
            raise ValidatorException(error)

    @staticmethod
    def validate_deadline(deadline):
        error = []
        if int(deadline) < int(datetime.datetime.now().strftime("%d")):
            error.append("Deadline can't be before the current day!")
        elif int(deadline) < 1 or int(deadline) > 31:
            error.append("Deadline must be an integer between 1 and 30")
        if len(error) > 0:
            raise ValidatorException(error)


