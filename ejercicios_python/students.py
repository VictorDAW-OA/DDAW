class StudentManager:
    def __init__(self):
        self.students = []


    def add_student(self, name, grade):
        student = {'name': name , 'grade': grade}
        self.students.append(student)
        print(f"El alumno {name} ha sido añadido")
        

    def remove_student(self, name):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print(f"El estudiante  {name} ha sido borrado.")
                return
        print(f"El estudiante {name} no ha sido encontrado.")


    def update_grade(self, name, new_grade):
        for student in self.students:
            if student['name'] == name:
                student['grade'] = new_grade
                print(f"La nota del alumno {name} ha sido actualizada a {new_grade}")
                return
        print(f"El estudiante  {name} no ha sido encontrado.")

    def show_students(self):
        if not self.students:
            print("No hay estudiantes en la lista")
        else:
            for student in self.students:
                    print(f"Estudiantes: {student['name']}, Grade: {student['grade']}")

    def search_grade(self, name):
        for student in self.students:
            if student['name'] == name:
                print(f"El grado del alumno {name}: es {student['grade']}")
                return
        print(f"El estudiante {name} no ha sido encontrado.")


# Example usage of the StudentManager class
if __name__ == "__main__":
    manager = StudentManager()
    # Example calls to methods (to be implemented)
    manager.add_student("Oscar", 85)
    manager.show_students()
    manager.update_grade("Oscar", 88)
    manager.search_grade("Oscar")
    manager.remove_student("Oscar")
    manager.show_students()
    