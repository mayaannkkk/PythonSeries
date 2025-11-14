class Student:
    class_year = 2025
    num_student = 0

    def __init__(self,name,age):
        self.name = name
        self.age= age
        Student.num_student +=1

student1=Student("Mayank",20)
student2=Student("B",21)
student3=Student("C",20)
student4=Student("D",19)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")