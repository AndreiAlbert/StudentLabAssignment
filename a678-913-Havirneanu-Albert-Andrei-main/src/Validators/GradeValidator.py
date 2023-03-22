from src.domain.grade import Grade
from src.Validators.ValidatorException import ValidatorException

class GradeValidator:
    @staticmethod
    def validate(grade):
        error = []
        if isinstance(grade , Grade) is False:
            error.append("Is not a grade!")
        if int(grade.student_id) < 1:
            error.append("Id of student must be a positive integer!")
        if int(grade.assignment_id) < 1:
            error.append("Id of assignment must be a positive integer!")
        if int(grade.grade_value) < 0 or grade.grade_value > 10:
            error.append("Value of the grade must be an integer between 0 and 10!")
        if len(error) > 0:
            raise ValidatorException(error)

    @staticmethod
    def validate_value(value):
        if value < 0 or value > 10:
            raise ValidatorException(["Value of grade must be an integer between 0 and 10!"])



