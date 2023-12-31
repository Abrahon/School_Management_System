class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.classroom = {}
        
    def add_classroom(self, classroom):
        self.classroom[classroom.name] = classroom
        
    def add_teacher(self, subject,teacher):
        self.teachers[subject] = teacher
            
       
        
    def student_admission(self, student, classroom_name):
        if classroom_name in self.classrooms:
            # TODO: set student id, (roll num) at the time of adding the student 
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'No classroom as named{classroom_name}')
            

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.student = [] 
        
    def add_student(self, student):
       serial_id = f'{self.name}-{len(self.students) + 1}'
       student.id = serial_id
       student.classroom = self.name
       self.students.append(student)
       
    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    # TODO: sort students by 
    
    def get_top_students(self):
        pass
    
      
    
        