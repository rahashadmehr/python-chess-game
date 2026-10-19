import json
class Course:
    id: int = 0
    name: str = ""
    units: int = 0
    scores: float = 0

    def __init__(self, id: int, name: str, units: int):
        self.id = id
        self.name = name
        self.units = units

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.units}"

    def __eq__(self, other):
        return (self.id == other.id)


class Student:
    id: int = 0
    name: str = ""
    family: str = ""
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str):
        self.id = id
        self.name = name
        self.family = family
        self.courses = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}"

    def __eq__(self, other):
        return (self.id == other.id)
    
    def info(self) -> None:
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")


class Teacher:
    id: int = 0
    name: str = ""
    family: str = ""
    grade: int = 0
    courses: list[Course]

    def __init__(self, id: int, name: str, family: str, grade: int):
        self.id = id
        self.name = name
        self.family = family
        self.grade = grade
        self.courses = []

    def __str__(self):
        return f"{self.id}\t{self.name}\t{self.family}\t{self.grade}"

    def __eq__(self, other):
        return (self.id == other.id)
    
    def info(self) -> None:
        print(f"id: {self.id}")
        print(f"name: {self.name}")
        print(f"family: {self.family}")
        for c in self.courses:
            print(f"{c.id}\t{c.name}\t{c.scores}")


class Classroom:
    id: int = 0
    name: str = ""
    teacher: Teacher
    course: Course
    students: list[Student]

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.students = []



class School:
    name: str = ""
    selected_students: Student= None

    def __init__(self, name: str):
        self.name = name
        self.courses: list[Course] = []
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []
        self.selected_students:Student=None
        self.selected_teachers:Teacher=None
        self.selected_courses:Course=None

    def print_students(self) -> None:
        for s in self.students:
            print(s)

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)
        else:
            print("student already exist")

    def edit_student(self, student: Student) -> None:
        if student in self.students:
            i = self.students.index(student) 
            self.students[i] = student 
            print("student updated")
        else:
            print("student not found")

    def remove_student(self, id: int) -> None:
        s = Student(id, "", "")
        if s in self.students:
            self.students.remove(s)
        else:
            print("id not found.")


    def print_courses(self) -> None:
        for c in self.courses:
            print(c)

    def add_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
        else:
            print("course already exist")

    def edit_course(self, course: Course) -> None:
        if course in self.courses:
            i = self.courses.index(course) 
            self.courses[i] = course 
            print("course updated")
        else:
            print("course not found")
    def remove_course(self, id: int) -> None:
        c = Course(id, "", 0)
        if c in self.courses:
            self.courses.remove(c)
        else:
            print("id not found.")

    def print_teachers(self) -> None:
        for t in self.teachers:
            print(t)

    def add_teacher(self, teacher: Teacher) -> None:
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print("teacher already exist")

    def edit_teacher(self, teacher: Teacher) -> None:
        if teacher in self.teachers:
            i = self.teachers.index(teacher) 
            self.teachers[i] = teacher 
            print("teacher updated")
        else:
            print("teacher not found")

    def remove_teacher(self, id: int) -> None:
        t = Teacher(id, "", "",0)
        if t in self.teachers:
            self.teachers.remove(t)
        else:
            print("id not found.")
    def load_data(self):
        file=open("01.json","rt")
        f=file.read()
        data=json.loads(f)
        file.close()
    
        for s in data["students"]:
            self.students.append(Student(s["id"], s["name"], s["family"]))

        for c in data["courses"]:
            self.courses.append(Course(c["id"], c["name"], c["units"]))

        for t in data["teachers"]:
            self.teachers.append(Teacher(t["id"], t["name"], t["family"],0))

    def save_data(self):
        data={
            "students":[],
            "courses":[],
            "teachers":[]
        }
        for s in self.students:
            data["students"].append({
                "id":s.id,
                "name":s.name,
                "family":s.family
            })
        for c in self.courses:
            data["courses"].append({
                "id":c.id,
                "name":c.name,
                "units":c.units
            })
        for t in self.teachers:
            data["teachers"].append({
                "id":t.id,
                "name":t.name,
                "family":t.family,
                "grade": t.grade
            })
        file=open("01.json","w")
        json.dump(data, file)
        file.close()
level = "root"
sc1 = School("sama")
sc1.load_data()

while True:
    if level == "root":
        print("1- students")
        print("2- teachers")
        print("3- courses")
        print("4- classrooms")
        print("5- save")
        print("0- exit")
        cmd = int(input(">>: "))
        if cmd == 1:
            level = "students"
        elif cmd == 2:
            level = "teachers"
        elif cmd == 3:
            level = "courses"
        elif cmd == 4:
            level = "classrooms"
        elif cmd == 5:
            sc1.save_data()
        elif cmd == 0:
            break
    elif level == "students":
        print("1- show students")
        print("2- add student")
        print("3- edit student")
        print("4- delete student")
        print("5- select student")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            sc1.print_students()
        elif cmd == 2:
            id = int(input("id: "))
            name = input("name: ")
            family = input("family: ")
            sc1.add_student(Student(id, name, family))
        elif cmd == 3:
            pass
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_student(id)
        elif cmd == 5:
            sc1.print_students()
            id = int(input("id: "))
            search_st = Student(id, "", "")
            if search_st in sc1.students:
                idx = sc1.students.index(search_st)
                sc1.selected_students = sc1.students[idx]
                level="students_select"
            else:
                print("students not found")
                
                
        elif cmd == 0:
            level = "root"
    elif level=="students_select":
        print("1- info")
        print("2- show courses")
        print("3- add course")
        print("4- delete course")
        print("5- set score")
        print("0- back")
        
        cmd = int(input(">>: "))
        if cmd==1:
            sc1.selected_students.info()
           
        elif cmd==2:
            pass
        elif cmd==3:
#            sc1.print_courses()
#            cid=int(input("course id: "))
#            search_course= Course(cid,"",0)
#            if search_course in sc1.courses:
#                target= sc1.courses[sc1.courses.index(search_course)]
#                sc1.selected_students.courses.append(target)
            for c in sc1.courses:
                if c not in sc1.selected_students.courses:
                    print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course not in sc1.selected_students.courses:
                target= sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_students.courses.append(target)
        elif cmd==4:
            for c in sc1.selected_students.courses:
                print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course in sc1.selected_students.courses:
                target= sc1.selected_students.courses.index(search_course)
                new_score=float(input("new score: "))
                sc1.selected_students.courses[idx].scores=new_score
        elif cmd==5: #غلطع هم این هم تیچر
            for c in sc1.selected_students.courses:
                print(f"{c.id}\t{c.name}\t{c.units}")

            cid = int(input("course id: "))
            score = float(input("score: "))

            search_course = Course(cid, "", 0)

            if search_course in sc1.selected_students.courses:
                idx = sc1.selected_students.courses.index(search_course)
                selected_course = sc1.selected_students.courses[idx]
                print(selected_course.name)
                score = float(input("Enter score: "))
                selected_course.scores = score

        elif cmd==0:
            level = "students"

        
    elif level == "teachers":
        print("1- show teachers")
        print("2- add teacher")
        print("3- edit teacher")
        print("4- delete teacher")
        print("5- select teacher")
        print("0- back")
        cmd = int(input(">>: "))


        if cmd == 1:
            sc1.print_teachers()
        elif cmd == 2:
            id = int(input("id: "))
            name = input("name: ")
            family = input("family: ")
            grade = int(input("grade: "))
            sc1.add_teacher(Teacher(id, name, family, grade))
        elif cmd == 3:
            pass
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_teacher(id)
        elif cmd == 5:
            sc1.print_teachers()
            id = int(input("id: "))
            search_tch = Teacher(id, "", "",0)
            if search_tch in sc1.teachers:
                idx = sc1.teachers.index(search_tch)
                sc1.selected_teachers = sc1.teachers[idx]
                level="teachers_select"
            else:
                print("teacher not found")
                
                
        elif cmd == 0:
            level = "root"
    elif level=="teachers_select":
        sc1.selected_teachers.info()
        if cmd==1:
            sc1.selected_students.info()
        elif cmd==2:
            pass
        elif cmd==3:
#            sc1.print_courses()
#            cid=int(input("course id: "))
#            search_course= Course(cid,"",0)
#            if search_course in sc1.courses:
#                target= sc1.courses[sc1.courses.index(search_course)]
#                sc1.selected_teachers.courses.append(target)
            for c in sc1.courses:
                if c not in sc1.selected_teachers.courses:
                    print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course not in sc1.selected_teachers.courses:
                target= sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.append(target)
        elif cmd==4:
            for c in sc1.selected_teachers.courses:
                print(c)
            cid=int(input("course id: "))
            search_course= Course(cid,"",0)
            if search_course in sc1.selected_teachers.courses:
                target= sc1.courses[sc1.courses.index(search_course)]
                sc1.selected_teachers.courses.remove(target)
        elif cmd==5:
            cid=int(input("score: "))
            search_course= Course(cid,"",0)
            for c in sc1.selected_teachers.courses:
                print(c)
                
                idx = sc1.teachers.index(search_course)
                sc1.selected_teachers.courses[idx].scores=cid
        elif cmd==0:
            level = "teachers"
    elif level == "courses":
        print("1- show courses")
        print("2- add course")
        print("3- edit course")
        print("4- delete course")
        print("5- select course")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            sc1.print_courses()
        elif cmd == 2:
            id = int(input("id: "))
            name = input("name: ")
            units = int(input("units: "))
            sc1.add_course(Course(id, name, units))
        elif cmd == 3:
            pass
        elif cmd == 4:
            id = int(input("id: "))
            sc1.remove_course(id)
        elif cmd == 5:
            pass
        elif cmd == 0:
            level = "root"
    elif level == "classrooms":
        print("1- show classrooms")
        print("2- add classroom")
        print("3- edit classroom")
        print("4- delete classroom")
        print("5- select classroom")
        print("0- back")
        cmd = int(input(">>: "))
        if cmd == 1:
            pass
        elif cmd == 2:
            pass
        elif cmd == 3:
            pass
        elif cmd == 4:
            pass
        elif cmd == 5:
            pass
        elif cmd == 0:
            level = "root"