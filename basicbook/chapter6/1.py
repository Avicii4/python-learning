class Person(object):  # 必须以object为基类
    def __init__(self, name='', age=20, sex='male'):
        self.set_name(name)
        self.set_age(age)
        self.set_sex(sex)

    def set_name(self, name):
        if not isinstance(name, str):
            print('名字类型错误')
            return
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int):
            print('年龄类型错误')
            return
        self.__age = age

    def set_sex(self, sex):
        if sex != 'male' and sex != 'female':
            print('性别错误')
            return
        self.__sex = sex

    def show(self):
        print('Name:', self.__name)
        print('Age:', self.__age)
        print('Sex:', self.__sex)


class Teacher(Person):  # 由Person派生
    def __init__(self, name='', age=20, sex='male', department='CS'):
        super(Teacher, self).__init__(name, age, sex)
        # or  Person.__init__(self,name, age, sex)
        self.set_department(department)

    def set_department(self, department):
        if not isinstance(department, str):
            print('部门类型错误')
            return
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print('Department:', self.__department)


class Student(Person):
    def __init__(self, name='', age=15, sex='female', grade=92):
        super(Student, self).__init__(name, age, sex)
        self.set_grade(grade)

    def set_grade(self, grade):
        if not isinstance(grade, int):
            print('成绩类型错误')
            return
        if grade < 0 or grade > 100:
            print('成绩范围错误')
            return
        self.__grade = grade

    def show(self):
        super(Student, self).show()
        print('Grade:', self.__grade)


if __name__ == '__main__':
    zhang = Person('zhang', 18, 'male')
    zhang.show()
    li = Teacher('li', 40, 'male', 'English')
    li.show()
    wong = Student('wong', 16, 'female', 80)
    wong.show()
