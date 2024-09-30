#Enunciado:
    #1.Add a new student with their grade.
    #2.Remove an existing student by their name.
    #3.Update the grade of an existing student.
    #4.Show the list of all students with their grades.
    #5.Search for the grade of a specific student.

class StudentManager:

    """Initializes the StudentManager with and empty list of students"""
    def __init__(self):
        self.students = []
    

    """Adds a new student with their grade to the list"""
    def add_student(self, name, grade):
        #add_student pertenece a la clase StudentManager, por eso hay que usar el self
        #1.Crear el diccionario para almacenar a los estudiantes
        student = {'name':name, 'grade':grade}
        #2.Añadir estudiantes al diccionario
        #self.students = lista de estudiantes que pertenece a la instancia actual de la clase
        self.students.append(student)
        print(f"Name: {name} Grade: {grade}")
        pass


    """Removes a student from the list by their name"""
    def remove_student(self, name):
        #sólo hace falta el parámetro nombre porque se busca por el nombre
        for student in self.students:
            if student['name'] == name:
                #si el nombre introducido coincide con el "name" del diccionario, se borra
                #y si hay dos nombres iguales? -> sólo borra el primero por el return
                #Para borrar todos los que coincidan esto no sirve :(
                self.students.remove(student)
                print(f"{name} has been removed from the list")
                return
        pass
    
    """Removes ALL students from the list by their name"""
    def remove_all_student(self, name):
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                print(f"{name} has been removed from the list")
    
    
    """Updates the grade of an existing student"""
    def update_grade(self, name, new_grade):
        
        for student in self.students:
            if student['name'] == name:
                #Si el nombre coincide se asigna nuevo valor a grade
                student['grade'] = new_grade
                print(f"The grade of {name} has been updated to {new_grade}")
                return
        pass

    def show_student(self):
        """Shows the list of all students with their grades"""
        for student in self.students:
                print(f"Name: {student['name']}, Grade: {student['grade']}")
        pass


    def search_grade(self, name):
        """Searches and shows the grade of a student by their name"""
        for student in self.students:
            if student['name'] == name:
                print(f"The grade of {name} is {student['grade']}")
                return
        pass


# Example usage of the StudentManager class
if __name__ == "__main__":
    manager = StudentManager()
    # Example calls to methods (to be implemented)
    manager.add_student("Ana", 85)
    manager.add_student("Luis", 90)
    manager.show_student()
    manager.update_grade("Ana", 88)
    manager.search_grade("Luis")
    manager.remove_student("Luis")
    manager.show_student()

    



