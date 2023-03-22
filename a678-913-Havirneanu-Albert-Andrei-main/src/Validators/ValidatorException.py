class ValidatorException(Exception):
    def __init__(self , errors):
        self.errors = errors

    def __str__(self):
        result = '\n'
        for er in self.errors:
            result = result + er
            result = result + '\n'
        return result
