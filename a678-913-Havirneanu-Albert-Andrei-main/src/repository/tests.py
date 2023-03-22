from src.domain.assigment import Assignment
from src.domain.grade import Grade
from src.domain.student import Student

from src.repository.students_repo import StudentRepo
from src.repository.assigment_repo import AssignmentRepo
from src.repository.grade_repo import GradeRepo

from src.Validators.AssignmentValidator import AssignmentValidator
from src.Validators.StudentValidator import StudentValidator
from src.Validators.GradeValidator import GradeValidator
from src.Validators.ValidatorException import ValidatorException

from src.services.student_service import StudentServices
from src.services.grade_services import GradeServices
from src.services.assignments_services import AssignmentServices

from src.services.undo_redo import UndoRedoService

import unittest

class DomainAndValidators(unittest.TestCase):
    def test_create_student(self):
        std1 = Student(1 , "marian" , 20)
        self.assertEqual(std1.id , 1)
        self.assertEqual(std1.name , "marian")
        self.assertEqual(std1.group , 20)
        std1.name = "ted"
        self.assertEqual(std1.name , "ted")
        std1.group = 45
        self.assertEqual(std1.group , 45)
        self.assertEqual(str(std1) , "Student with id 1 , name ted and from group 45")


    def test_student_validator(self):
        std1 = Student(-10, "marian", 20)
        self.assertRaises(ValidatorException , StudentValidator.validate , std1)
        std1.name = " "
        self.assertRaises(ValidatorException , StudentValidator.validate , std1)
        std1.group = -5
        self.assertRaises(ValidatorException , StudentValidator.validate , std1)
        self.assertRaises(ValidatorException , StudentValidator.validate_id , -7)
        self.assertRaises(ValidatorException , StudentValidator.validate_group , -30)


    def test_create_assignment(self):
        ass = Assignment(1 , "problem1" , 30)
        self.assertEqual(ass.id , 1)
        self.assertEqual(ass.description , "problem1")
        self.assertEqual(ass.deadline , 30)
        ass.description = "problem2"
        self.assertEqual(ass.description , "problem2")
        ass.deadline = 15
        self.assertEqual(ass.deadline , 15)
        self.assertEqual(str(ass) , "Assignment with id 1 , description problem2 and deadline 15")


    def test_validate_ass(self):
        ass = Assignment(-3 , "pb1" , 45)
        self.assertRaises(ValidatorException , AssignmentValidator.validate , ass)
        self.assertRaises(ValidatorException , AssignmentValidator.validate_id , -3)
        self.assertRaises(ValidatorException , AssignmentValidator.validate_desc , "")
        self.assertRaises(ValidatorException , AssignmentValidator.validate_deadline , 45)


    def test_create_grade(self):
        grade = Grade(2 , 10 , 0)
        self.assertEqual(grade.assignment_id , 2)
        self.assertEqual(grade.student_id , 10)
        self.assertEqual(grade.grade_value , 0)
        self.assertEqual(str(grade) , "Student with id 10 has the assigment with the id 2. Grade: 0")
        grade.grade_value = 10
        self.assertEqual(grade.grade_value , 10)


    def test_validate_grade(self):
        grade = Grade(-2 , 10 , 0)
        self.assertRaises(ValidatorException , GradeValidator.validate , grade)
        grade = Grade(2 , -3 , 0)
        self.assertRaises(ValidatorException , GradeValidator.validate , grade)
        self.assertRaises(ValidatorException , GradeValidator.validate_value , 20)


class StudRepo(unittest.TestCase):
    def test_add(self):
        repo = StudentRepo()
        self.assertEqual(len(repo) , 0)
        std1 = Student(1 , "Marian" , 20)
        repo.add_student(std1)
        self.assertEqual(len(repo.students_list) , 1)
        self.assertEqual(repo.students_list , [std1])


    def test_remove(self):
        repo = StudentRepo()
        std1 = Student(1 , "Marian" , 20)
        std2 = Student(2 , "Shrek" , 20)
        repo.add_student(std1)
        repo.add_student(std2)
        repo.remove_student_by_id(1)
        self.assertEqual(len(repo) , 1)
        self.assertEqual(repo.students_list , [std2])


    def test_update_name(self):
        repo = StudentRepo()
        std1 = Student(1 , "Marian" , 20)
        repo.add_student(std1)
        repo.update_name(1 , "Ilinoi")
        self.assertEqual(repo.students_list[0].name , "Ilinoi")


    def test_update_group(self):
        repo = StudentRepo()
        std1 = Student(1 , "Marian" , 20)
        repo.add_student(std1)
        repo.update_group(1 , 40)
        self.assertEqual(repo.students_list[0].group , 40)


    def test_find_student(self):
        repo = StudentRepo()
        std1 = Student(1 , "Marian" , 20)
        repo.add_student(std1)
        self.assertEqual(repo.search_student(1) , std1)


    def test_add_20(self):
        repo = StudentRepo()
        repo.add_20()
        self.assertEqual(len(repo) , 20)
        self.assertEqual(repo.students_list[0].id , 1)



class AssRepo(unittest.TestCase):
    def test_add_assignment(self):
        repo = AssignmentRepo()
        self.assertEqual(len(repo) , 0)
        ass = Assignment(1 , "pb1" , 30)
        repo.add_assignment(ass)
        self.assertEqual(len(repo) , 1)
        self.assertEqual(repo.assignment_list , [ass])


    def test_remove_assignment(self):
        repo = AssignmentRepo()
        ass = Assignment(1, "pb1", 30)
        ass2 = Assignment(2 , "pb2" , 25)
        repo.add_assignment(ass)
        repo.add_assignment(ass2)
        repo.remove_assignment(1)
        self.assertEqual(len(repo) , 1)
        self.assertEqual(repo.assignment_list , [ass2])


    def test_update_description(self):
        repo = AssignmentRepo()
        ass = Assignment(1, "pb1", 30)
        repo.add_assignment(ass)
        repo.update_description(1 , "pb4")
        self.assertEqual(repo.assignment_list[0].description , "pb4")


    def test_update_deadline(self):
        repo = AssignmentRepo()
        ass = Assignment(1, "pb1", 30)
        repo.add_assignment(ass)
        repo.update_deadline(1 , 20)
        self.assertEqual(repo.assignment_list[0].deadline , 20)


    def test_find_assignment(self):
        repo = AssignmentRepo()
        ass = Assignment(1, "pb1", 30)
        ass2 = Assignment(2 , "pb4" , 20)
        repo.add_assignment(ass)
        repo.add_assignment(ass2)
        self.assertEqual(repo.find_assignment(1) , ass)
        self.assertEqual(repo.find_assignment(2) , ass2)


    def test_add_20(self):
        repo = AssignmentRepo()
        repo.add_20()
        self.assertEqual(len(repo) , 22)


class GrRepo(unittest.TestCase):
    def test_add_grade(self):
        repo = GradeRepo()
        gr = Grade(1 , 2 , 10)
        repo.add_grade(gr)
        self.assertEqual(len(repo) , 1)
        self.assertEqual(repo.grade_list , [gr])


    def test_remove_grade_by_student(self):
        repo = GradeRepo()
        gr = Grade(1 , 2 , 10)
        repo.add_grade(gr)
        repo.remove_grade_by_student(2)
        self.assertEqual(len(repo) , 0)


    def test_remove_grade_by_ass(self):
        repo = GradeRepo()
        gr = Grade(1 , 2 , 10)
        gr1 = Grade(2 , 3 , 4)
        repo.add_grade(gr)
        repo.add_grade(gr1)
        repo.remove_grade_by_assignment(2)
        self.assertEqual(repo.grade_list , [gr])


    def test_update_grade(self):
        repo = GradeRepo()
        gr = Grade(1, 2, 0)
        gr1 = Grade(2, 3, 0)
        repo.add_grade(gr)
        repo.add_grade(gr1)
        repo.update_grade_value(gr.assignment_id , gr.student_id , 7)
        self.assertEqual(repo.grade_list[0].grade_value , 7)
        repo.update_grade_value(gr1.assignment_id , gr1.student_id , 10)
        self.assertEqual(repo.grade_list[1].grade_value , 10)




class ServiceStudentTests(unittest.TestCase):
    def setUp(self):
        self.repo = StudentRepo()
        self.validator = StudentValidator()
        self.srv = StudentServices(self.repo , self.validator)


    def test_add_student(self):
        self.srv.add_student(1 , "Marian" , 20)
        self.assertEqual(self.srv.student_length() , 1)
        self.srv.add_student(2 , "Maria" , 30)
        self.assertEqual(self.srv.student_length() , 2)


    def test_remove_student(self):
        self.srv.add_student(1, "Marian", 20)
        self.srv.add_student(2, "Maria", 30)
        self.srv.remove_student_by_id(1)
        self.assertEqual(self.srv.student_length() , 1)
        self.srv.remove_student_by_id(2)
        self.assertEqual(self.srv.student_length() , 0)


    def test_update_name(self):
        self.srv.add_student(1 , "Marian" , 20)
        self.srv.update_name(1 , "Ilie")
        self.assertEqual(self.repo.search_student(1).name , "Ilie")


    def test_update_group(self):
        self.srv.add_student(1, "Marian", 20)
        self.srv.update_group(1 , 50)
        self.assertEqual(self.repo.search_student(1).group , 50)


    def test_add_20(self):
        self.srv.add_20()
        self.assertEqual(self.srv.student_length() , 20)


class ServiceAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.repo = AssignmentRepo()
        self.validator = AssignmentValidator()
        self.srv = AssignmentServices(self.repo , self.validator)


    def test_add_assignment(self):
        self.srv.add_assignment(1 , "pb2" , 30)
        self.assertEqual(self.srv.assignments_length() , 1)
        self.srv.add_assignment(2 , "pb3" , 20)
        self.assertEqual(self.srv.assignments_length() , 2)


    def test_remove_assignment(self):
        self.srv.add_assignment(1, "pb2", 30)
        self.srv.add_assignment(2, "pb3", 20)
        self.srv.remove_assignment(1)
        self.assertEqual(self.srv.assignments_length(), 1)
        self.srv.remove_assignment(2)
        self.assertEqual(self.srv.assignments_length(), 0)


    def test_update_description(self):
        self.srv.add_assignment(1, "pb2", 30)
        self.srv.add_assignment(2, "pb3", 20)
        self.srv.update_description(1 , "pb20")
        self.assertEqual(self.repo.find_assignment(1).description , "pb20")
        self.srv.update_description(2, "pb30")
        self.assertEqual(self.repo.find_assignment(2).description, "pb30")


    def test_update_deadline(self):
        self.srv.add_assignment(1, "pb2", 30)
        self.srv.add_assignment(2, "pb3", 20)
        self.srv.update_deadline(1 , 30)
        self.assertEqual(self.repo.find_assignment(1).deadline, 30)
        self.srv.update_deadline(2, 29)
        self.assertEqual(self.repo.find_assignment(2).deadline , 29)


    def test_add_20(self):
        self.srv.add_20()
        self.assertEqual(self.srv.assignments_length() , 22)


class ServiceGradeTests(unittest.TestCase):
    def setUp(self):
        self.repo_grade = GradeRepo()
        self.validator_grade = GradeValidator()
        self.repo_assignment = AssignmentRepo()
        self.validator_assignment = AssignmentValidator()
        self.srv_assignment = AssignmentServices(self.repo_assignment, self.validator_assignment)
        self.repo_student = StudentRepo()
        self.validator_student = StudentValidator()
        self.srv_student = StudentServices(self.repo_student , self.validator_student)
        self.srv_grade = GradeServices(self.repo_student , self.validator_student , self.repo_assignment , self.validator_assignment
                                       , self.repo_grade , self.validator_grade)


    def test_add_grade_student(self):
        self.srv_student.add_student(1 , "Marian" , 20)
        self.srv_assignment.add_assignment(1 , "pb1" , 20)
        grade = Grade(1 , 1 , 0)
        self.srv_grade.add_grade_to_student(grade)
        self.assertEqual(self.srv_grade.get_grade_length() , 1)


    def test_add_grade_group(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_assignment.add_assignment(1, "pb1", 20)
        self.srv_student.add_student(2, "Andrei", 20)
        self.srv_student.add_student(3, "Maria", 30)
        self.srv_grade.add_grade_to_group(20 , 1)
        self.assertEqual(self.srv_grade.get_grade_length() , 2)


    def test_remove_grade_by_student(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_assignment.add_assignment(1, "pb1", 20)
        grade = Grade(1, 1, 0)
        self.srv_grade.add_grade_to_student(grade)
        self.srv_grade.remove_grade_by_student(1)
        self.assertEqual(self.srv_grade.get_grade_length() , 0)


    def test_remove_grade_by_assignment(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_assignment.add_assignment(1, "pb1", 20)
        grade = Grade(1, 1, 0)
        self.srv_grade.add_grade_to_student(grade)
        self.srv_grade.remove_grade_by_assignment(1)
        self.assertEqual(self.srv_grade.get_grade_length() , 0)


    def test_update_grade_value(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_assignment.add_assignment(1, "pb1", 20)
        grade = Grade(1, 1, 0)
        self.srv_grade.add_grade_to_student(grade)
        self.srv_grade.update_grade_value(1 , 1 , 10)
        self.assertEqual(self.srv_grade.get_all_grades()[0].grade_value , 10)


    def test_statistic1(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_student.add_student(2, "Maria", 20)
        self.srv_student.add_student(3, "Denis", 20)
        self.srv_assignment.add_assignment(1, "pb1", 30)
        self.srv_grade.add_grade_to_group(20 , 1)
        self.srv_grade.update_grade_value(1 , 1 , 10)
        self.srv_grade.update_grade_value(2 , 1 , 9)
        self.assertEqual(len(self.srv_grade.statistic1(1)) , 2)


    def test_statistic2(self):
        self.srv_student.add_student(1, "Marian", 20)
        self.srv_student.add_student(2, "Maria", 20)
        self.srv_student.add_student(3, "Denis", 20)
        self.repo_assignment.assignment_list.append(Assignment(1 , "pb1" , 1))
        self.srv_grade.add_grade_to_group(20, 1)
        result = self.srv_grade.statistic2()
        self.assertEqual(len(result.keys()) , 3)


    def test_statistic3(self):
        self.srv_student.add_student(1, "Marian", 10)
        self.srv_student.add_student(2, "Maria", 20)
        self.srv_student.add_student(3, "Denis", 30)
        self.srv_assignment.add_assignment(1, "pb1", 30)
        self.srv_assignment.add_assignment(2, "pb2", 20)
        self.srv_grade.add_grade_to_student(Grade(1 , 1 , 0))
        self.srv_grade.add_grade_to_student(Grade(2, 1, 0))
        self.srv_grade.add_grade_to_student(Grade(1, 2, 0))
        self.srv_grade.add_grade_to_student(Grade(2, 2, 0))
        self.srv_grade.update_grade_value(1 , 1 , 10)
        self.srv_grade.update_grade_value(1, 2, 7)
        result = self.srv_grade.statistic3()
        self.assertEqual(len(result) , 1)
        self.assertEqual(result[0][1] , 8.5)


class TestUndoRedo(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_grade = GradeRepo()
        self.validator_grade = GradeValidator()
        self.repo_assignment = AssignmentRepo()
        self.validator_assignment = AssignmentValidator()
        self.srv_assignment = AssignmentServices(self.repo_assignment, self.validator_assignment)
        self.repo_student = StudentRepo()
        self.validator_student = StudentValidator()
        self.srv_student = StudentServices(self.repo_student, self.validator_student)
        self.srv_grade = GradeServices(self.repo_student, self.validator_student, self.repo_assignment,
                                       self.validator_assignment
                                       , self.repo_grade, self.validator_grade)
        self.undo_redo = UndoRedoService(self.srv_student , self.srv_assignment , self.srv_grade)


    def test_add_to_undo_stack(self):
        self.undo_redo.add_to_undo_stack("Sremove" , 3)
        self.assertEqual(self.undo_redo.undo_stack_length() , 1)
        self.undo_redo.add_to_undo_stack("Aremove" , 1)
        self.assertEqual(self.undo_redo.undo_stack_length() , 2)


    def test_add_to_redo_stack(self):
        self.undo_redo.add_to_redo_stack("Sadd" , Student(1 , "dfd" , 913))
        self.assertEqual(self.undo_redo.redo_stack_length() , 1)


    def test_undo_redo(self):
        self.srv_student.add_student(1 , "Marian" , 43)
        self.assertEqual(self.srv_student.student_length() , 1)
        self.undo_redo.add_to_undo_stack("Sremove" , 1)
        self.undo_redo.undo()
        self.assertEqual(self.srv_student.student_length() , 0)
        self.undo_redo.redo()
        self.assertEqual(self.srv_student.student_length() , 1)
        self.srv_student.update_name(1 , "Catalin")
        self.assertEqual(self.srv_student.search_student_by_id(1).name , "Catalin")
        self.undo_redo.add_to_undo_stack("Sname" , ["Marian" , 1])
        self.undo_redo.undo()
        self.assertEqual(self.srv_student.search_student_by_id(1).name , "Marian")
        self.undo_redo.redo()
        self.assertEqual(self.srv_student.search_student_by_id(1).name , "Catalin")
        self.srv_student.update_group(1 , 68)
        self.undo_redo.add_to_undo_stack("Sgroup" , [1 , 43])
        self.assertEqual(self.srv_student.search_student_by_id(1).group , 68)
        self.undo_redo.undo()
        self.assertEqual(self.srv_student.search_student_by_id(1).group , 43)
        self.undo_redo.redo()
        self.assertEqual(self.srv_student.search_student_by_id(1).group , 68)
        self.srv_assignment.add_assignment(1 , "pb1" , 30)
        self.undo_redo.add_to_undo_stack("Aremove" , 1)
        self.assertEqual(self.srv_assignment.assignments_length() , 1)
        self.undo_redo.undo()
        self.assertEqual(self.srv_assignment.assignments_length() , 0)
        self.undo_redo.redo()
        self.assertEqual(self.srv_assignment.assignments_length() , 1)





