# Родительский класс Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Дочерний класс Lecturer (лекторы)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()


# Дочерний класс Reviewer (эксперты, проверяющие домашние задания)
class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс Student
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        avg_grade = self.calculate_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return sum(all_grades) / len(all_grades)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()


# Пример использования
# Создаем студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

# Создаем эксперта (Reviewer)
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# Эксперт выставляет оценки студенту
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

# Создаем лектора (Lecturer)
cool_lecturer = Lecturer('Another', 'Person')
cool_lecturer.courses_attached += ['Python']

# Студент выставляет оценки лектору
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)

# Выводим информацию
print(cool_reviewer)
# Имя: Some
# Фамилия: Buddy

print(cool_lecturer)
# Имя: Another
# Фамилия: Person
# Средняя оценка за лекции: 9.0

print(best_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.0
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# Сравнение студентов и лекторов
student1 = Student('Alice', 'Smith', 'female')
student1.courses_in_progress += ['Python']
cool_reviewer.rate_hw(student1, 'Python', 7)
cool_reviewer.rate_hw(student1, 'Python', 8)

student2 = Student('Bob', 'Johnson', 'male')
student2.courses_in_progress += ['Python']
cool_reviewer.rate_hw(student2, 'Python', 9)
cool_reviewer.rate_hw(student2, 'Python', 10)

print(student1 < student2)  # True (7.5 < 9.5)
print(student1 == student2)  # False

lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached += ['Python']
best_student.rate_lecturer(lecturer1, 'Python', 8)
best_student.rate_lecturer(lecturer1, 'Python', 7)

lecturer2 = Lecturer('Jane', 'Doe')
lecturer2.courses_attached += ['Python']
best_student.rate_lecturer(lecturer2, 'Python', 9)
best_student.rate_lecturer(lecturer2, 'Python', 10)

print(lecturer1 > lecturer2)  # False (7.5 < 9.5)
print(lecturer1 == lecturer2)  # False