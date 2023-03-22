class UndoRedoService:
    def __init__(self , stud_service , ass_service , grade_service):
        self.__undo_stack = []
        self.__redo_stack = []
        self.__stud_service = stud_service
        self.__ass_service = ass_service
        self.__grade_service = grade_service


    def undo_stack_length(self):
        return len(self.__undo_stack)

    def redo_stack_length(self):
        return len(self.__redo_stack)

    def add_to_undo_stack(self , operation , params):
        self.__undo_stack.append([operation , params])


    def add_to_redo_stack(self , operation , params):
        self.__redo_stack.append([operation , params])


    def undo(self):
        if len(self.__undo_stack) > 0:
            last_one = self.__undo_stack.pop()
            if last_one[0] == "Sremove":
                stud = self.__stud_service.search_student_by_id(last_one[1])
                self.add_to_redo_stack("Sadd" , stud)
                self.__stud_service.remove_student_by_id(last_one[1])
            elif last_one[0] == "Sadd":
                id = last_one[1][0].id
                name = last_one[1][0].name
                group = last_one[1][0].group
                self.add_to_redo_stack("Sremove" , id)
                self.__stud_service.add_student(id , name , group)
                if last_one[1][1]:
                    for gr in last_one[1][1]:
                        self.__grade_service.add_grade_to_student(gr)
            elif last_one[0] == "Sname":
                old_name = last_one[1][0]
                id = last_one[1][1]
                self.add_to_redo_stack("Sname", [id , self.__stud_service.search_student_by_id(id).name])
                self.__stud_service.update_name(id , old_name)
            elif last_one[0] == "Sgroup":
                old_group = last_one[1][1]
                id = last_one[1][0]
                self.add_to_redo_stack("Sgroup" , [id , self.__stud_service.search_student_by_id(id).group])
                self.__stud_service.update_group(id , old_group)
            elif last_one[0] == "Aremove":
                assignment = self.__ass_service.find_assignment(last_one[1])
                self.add_to_redo_stack("Aadd" , assignment)
                self.__ass_service.remove_assignment(last_one[1])
            elif last_one[0] == "Aadd":
                id = last_one[1][0].id
                deadline = last_one[1][0].deadline
                desc = last_one[1][0].description
                self.add_to_redo_stack("Aremove" , id)
                self.__ass_service.add_assignment(id , desc , deadline)
                if last_one[1][1]:
                    for gr in last_one[1][1]:
                        self.__grade_service.add_grade_to_student(gr)
            elif last_one[0] == "Adescription":
                desc = last_one[1][1]
                id = last_one[1][0]
                self.add_to_redo_stack("Adescription" , [id , self.__ass_service.find_assignment(id).description])
                self.__ass_service.update_description(id , desc)
            elif last_one[0] == "Adeadline":
                deadline = last_one[1][1]
                id = last_one[1][0]
                self.add_to_redo_stack("Adeadline" , [id , self.__ass_service.find_assignment(id).deadline])
                self.__ass_service.update_deadline(id , deadline)
            elif last_one[0] == "Gremove":
                stud_id = last_one[1].student_id
                ass_id = last_one[1].assignment_id
                self.add_to_redo_stack("Gadd" , last_one[1])
                self.__grade_service.remove_grade(stud_id , ass_id)
            elif last_one[0] == "GroupRemove":
                group = last_one[1][0]
                ass_id = last_one[1][1]
                self.add_to_redo_stack("AddGroup" , [group , ass_id])
                self.__grade_service.remove_grade_group(group , ass_id)

    def redo(self):
        if len(self.__redo_stack) > 0:
            last_one = self.__redo_stack.pop()
            if last_one[0] == "Sadd":
                stud = last_one[1]
                id = stud.id
                group = stud.group
                name = stud.name
                self.__stud_service.add_student(id , name , group)
            elif last_one[0] == "Sremove":
                self.__stud_service.remove_student_by_id(last_one[1])
                self.__grade_service.remove_grade_by_student(last_one[1])
            elif last_one[0] == "Sname":
                name = last_one[1][1]
                id = last_one[1][0]
                self.__stud_service.update_name(id , name)
            elif last_one[0] == "Sgroup":
                group = last_one[1][1]
                id = last_one[1][0]
                self.__stud_service.update_group(id , group)
            elif last_one[0] == "Aadd":
                ass = last_one[1]
                id = ass.id
                desc = ass.description
                deadline = ass.deadline
                self.__ass_service.add_assignment(id , desc , deadline)
            elif last_one[0] == "Aremove":
                self.__grade_service.remove_grade_by_assignment(last_one[1])
                self.__ass_service.remove_assignment(last_one[1])
            elif last_one[0] == "Adescription":
                description = last_one[1][1]
                id = last_one[1][0]
                self.__ass_service.update_description(id , description)
            elif last_one[0] == "Adeadline":
                deadline = last_one[1][1]
                id = last_one[1][0]
                self.__ass_service.update_deadline(id , deadline)
            elif last_one[0] == "Gadd":
                self.__grade_service.add_grade_to_student(last_one[1])
            elif last_one[0] == "AddGroup":
                group = last_one[1][0]
                ass_id = last_one[1][1]
                self.__grade_service.add_grade_to_group(group , ass_id)

    def clear_redo_stack(self):
        self.__redo_stack.clear()

