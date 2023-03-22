### 2. Student Lab Assignment
Write an application that manages student lab assignments for a discipline. The application will store:
- **Student**: `student_id`, `name`, `group`
- **Assignment**: `assignment_id`, `description`, `deadline`
- **Grade**: `assignment_id`, `student_id`, `grade_value`

Create an application that allows to:
1. Manage students and assignments. The user can add, remove, update, and list both students and assignments.
2. Give assignments to a student or a group of students. In case an assignment is given to a group of students, every student in the group will receive it. In case there are students who were previously given that assignment, it will not be assigned again.
3. Grade student for a given assignment. When grading, the program must allow the user to select the assignment that is graded, from the student’s list of ungraded assignments. A student’s grade for a given assignment cannot be changed. Deleting a student removes their assignments. Deleting an assignment also removes all grades at that assignment.
4. Create statistics:
    - All students wh o received a given assignment, ordered descending by grade.
    - All students who are late in handing in at least one assignment. These are all the students who have an ungraded assignment for which the deadline has passed.
    - Students with the best school situation, sorted in descending order of the average grade received for all graded assignments.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying)
