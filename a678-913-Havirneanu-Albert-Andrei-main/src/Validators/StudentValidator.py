from src.domain.student import Student
from src.Validators.ValidatorException import ValidatorException

class StudentValidator:
    @staticmethod
    def validate(student):
        errors = []
        if isinstance(student , Student) is False:
            errors.append("Is not a student!")
        if int(student.id < 1):
            errors.append("Id must be a positive integer!")
        if not(student.name and student.name.strip()):
            errors.append("Name can't be empty!")
        if int(student.group) < 1:
            errors.append("Group number must be a positive integer!")
        if len(errors) > 0:
            raise ValidatorException(errors)

    @staticmethod
    def validate_id(id):
        errors = []
        if int(id) < 1:
            errors.append("id must be a positive integer!")
        if len(errors) > 0:
            raise ValidatorException(errors)

    @staticmethod
    def validate_name(name):
        errors = []
        if not (name and name.strip()):
            errors.append("Name can't be empty!")
        if len(errors) > 0:
            raise ValidatorException(errors)

    @staticmethod
    def validate_group(group):
        errors = []
        if int(group) < 1:
            errors.append("Group number must be a positive integer!")
        if len(errors) > 0:
            raise ValidatorException(errors)