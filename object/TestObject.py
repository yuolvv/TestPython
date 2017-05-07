# class Student(object):
#     pass
#
# bart = Student()
# print(bart)
# print(Student)
#
# bart.name = 'tsing'
# print(bart.name)

class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            result = 'A'
        elif self.__score >=60:
            result = 'B'
        else:
            result = 'C'
        print(result)

bart = Student('tsing' ,98)

print(bart.get_name())
print(bart.get_score())

bart.print_score()
# print(bart.get_grade())
bart.get_grade()
# print(bart._Student.__name)

bart.__name = "New Name"
print(bart.__name)
print(bart.get_name())












































































