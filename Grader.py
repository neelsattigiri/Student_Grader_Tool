class Marks:
    def __init__(self, english, hindi, math, science, socialstudies):
        self.english = ('English', english)
        self.hindi = ('Hindi', hindi)
        self.math = ('Math', math)
        self.science = ('Science', science)
        self.socialstudies = ('Social Studies', socialstudies)
        self.total = english + hindi + math + science + socialstudies
        self.percent = self.total / 5



def getmarks(subject):
    return subject[1]

class Student:
    def __init__(self, name, grade, section, marks):
        self.name = name
        self.grade = grade
        self.section = section
        self.marks = marks

    def calc_result(self):
        if self.marks.percent >= 33:
            return 'Pass'
        else:
            return 'Fail'

    def calc_highest(self):
        marks_list = [self.marks.english, self.marks.hindi, self.marks.math,
                      self.marks.science, self.marks.socialstudies]

        marks_list.sort(key=getmarks, reverse=True)

        return marks_list[0][0]


class Question:
    def __init__(self, number, text, option_a, option_b, option_c, answer):
        self.number = number
        self.text = text
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.answer = answer


class QuestionPaper:
    def __init__(self, grade):
        self.grade = grade
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)


class Answer:
    def __init__(self, number, answer):
        self.number = number
        self.answer = answer

