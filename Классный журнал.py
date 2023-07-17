class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def __average_rating_student(self):
        grades_sum = 0
        grades_count = 0
        for grades in self.grades.values():
            for grade in grades:
                grades_sum += grade
                grades_count += 1
        return grades_sum/grades_count

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return 
        return self.__average_rating_student() < other.__average_rating_student()

    def __str__ (self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {str(self.__average_rating_student())} \n Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
                

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def __average_rating_lecturer(self, lecturer_grade):
        grades_sum = 0
        grades_count = 0
        for grades in self.grades.values():
            for grade in grades:
                grades_sum += grade
                grades_count += 1
        return grades_sum/grades_count
        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.__average_rating_lecturer() < other.__average_rating_lecturer()

    def __str__ (self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {str(self.__average_rating_lecturer())}'
        return res


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__ (self):
        res = f'Имя: {self.name} \n Фамилия: {self.surname}'
        return res        


student_1 = Student('Иван', 'Иванов', 'муж.')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в програмирование']

student_2 = Student('Лена', 'Ленина', 'жен.')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Введение в програмирование']
student_2.finished_courses += ['Git']


lecturer_1 = Lecturer('Сергей', 'Сергеев')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_in_progress += ['Python']
lecturer_1.courses_in_progress += ['Git']

lecturer_2 = Lecturer('Петр', 'Петров')
lecturer_2.courses_attached += ['Введение в програмирование']
lecturer_2.courses_in_progress += ['Введение в програмирование']
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_in_progress += ['Git']

reviewer_1 = Reviewer('Света', 'Светина')
reviewer_1.courses_attached += ['Git']
reviewer_1.courses_attached += ['Введение в програмирование']

reviewer_2 = Reviewer('Катя', 'Катина')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_2, 'Введение в програмирование', 9)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)


print(student_2.grades)

print(student_1)

print(student_2 < student_1)






#реализовать функции