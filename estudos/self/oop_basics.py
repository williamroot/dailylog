class Student:

    '''
    course = 'Math'

    > This is a class variable. It means this object is automatically
    assigned to every instance we create. Class variables are positioned
    outside methods.

    '''
    course = 'Math'

    '''
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    > This is the initial method. It means that when we create an
    instance (i.e. st1 = Student()), it will receive the arguments we
    pass (i.e. name, age, grade).
    > Each argument is an instance variable.
    > Examples:
    > st1 = Student('Rodolfo', 38, 7.9)
    > st2 = Student('Fernanda', 35, 9.1)

    '''
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    '''
    def passed(self):
        if self.grade >= 8:
            return 'Passed'
        else:
            return 'Failed'

    > This is an instance method. An instance method is sort of a
    function to work with info from an instance. In this case we are
    dealing with self.grade, or the grade of each instance.

    '''
    def passed(self):
        if self.grade >= 8:
            return 'Passed'
        else:
            return 'Failed'

    '''
    def info(cls):
        return cls.course

    > This is a class method. Class method is a function to call info
    from the class, not from an instance. In this case we want to work
    with a class variable, and that is why we need a class method.

    @classmethod

    > It is a decorator. It means you do not need to specify the class
    inside parenthesis when you call it. If we do not use it, we must
    write the class inside parenthesis.

    '''
    @classmethod
    def info(cls):
        return cls.course

    '''
    def school():
        return 'Objetivo'

    > This is a static method. Static method is a function not related
    to instance or class: it is a method aside. In this case we never
    mentioned school in instance or class, but we want to agregate this
    info to our instances and our class itself.

    @staticmethod

    > It is a decorator. It means the method is a static method (which
    means "not related to class or instance"). If we do not use it we
    get a TypeError because it will be considered an instance method,
    which means the interpreter will search for self as an argument and
    will find nothing.

    '''
    @staticmethod
    def school():
        return 'Objetivo'

# INPUTS

st1 = Student('Rodolfo', 38, 7.9)
st2 = Student('Fernanda', 35, 9.1)

# OUTPUTS

print(st1)
# <__main__.Student object at 0x7fb64a254cf8>
print(st2)
# <__main__.Student object at 0x7fb64a0c5668>
print(st1.name, st1.age, st1.grade, st1.course, st1.passed())
# Rodolfo 38 7.9 Math Failed
print(st2.name, st2.age, st2.grade, st2.course, st2.passed())
# Fernanda 35 9.1 Math Passed
print(st1.info())
# Math
print(st2.info())
# Math
print(Student.info())
# Math
print(st1.school())
# Objetivo
print(st2.school())
# Objetivo
print(Student.school())
# Objetivo
