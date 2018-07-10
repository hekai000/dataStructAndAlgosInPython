# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: 2-6类定义实例.py

@time: 2018/7/10 11:39

@desc:

'''
class PersonValueError(ValueError):
	pass


class PersonTypeError(TypeError):
	pass

import datetime
class Person(object):
	_num = 0


	def __init__(self, name, sex, birthday, ident):
		if not (isinstance(name, str)) or sex not in ("女", "男"):
			raise PersonValueError(name, sex)
		try:
			birth = datetime.date(*birthday)
		except:
			raise PersonValueError("Wrong date: ", birthday)
		self._name = name
		self._sex = sex
		self._birthday = birth
		self._id = ident
		Person._num += 1


	def id(self):
		return self._id


	def name(self):
		return self._name


	def sex(self):
		return self._sex


	def birthday(self):
		return self._birthday


	def age(self):
		return datetime.date.today().year - self._birthday.year

	def set_name(self, name):
		if not isinstance(name, str):
			raise PersonValueError("set_name", name)
		self._name = name

	def __lt__(self, other):
		if not isinstance(other, Person):
			raise PersonTypeError(other)
		return self._id < other._id

	@classmethod
	def num(cls):
		return Person._num

	def __str__(self):
		return " ".join((self._id, self._name, self._sex, str(self._birthday)))

	def details(self):
		return " ".join(("编号: " + self._id,
		                  "姓名: " + self._name,
		                  "性别: " + self._sex,
		                  "出生日期: " + str(self._birthday)))

p1 = Person("谢雨洁", "女", (1995, 7, 30), "1201510111")
p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
p3 = Person("张子玉", "女", (1974, 10, 16), "0197401032")
p4 = Person("李国栋", "男", (1962, 5, 24), "0196212018")

# plist2 = [p1, p2, p3, p4]
# for p in plist2:
# 	print(p)
# print("\nAfter sorting:")
# plist2.sort()
# for p in plist2:
# 	print(p.details())
#
# print "People created: " , Person.num(), "\n"


class Student(Person):
	_id_num = 0
	@classmethod
	def _id_gen(cls):
		cls._id_num += 1
		year = datetime.date.today().year
		return "1{:04}{:05}".format(year, cls._id_num)
	def __init__(self, name, sex, birthday, department):
		Person.__init__(self, name, sex, birthday, Student._id_gen())
		self._department = department
		self._enroll_date = datetime.date.today()
		self._courses = {}
	def set_course(self, course_name):
		self._courses[course_name] = None

	def set_scores(self, course_name, score):
		if course_name not in self._courses:
			raise PersonValueError("No this course selected:", course_name)
		self._courses[course_name] = score

	def scores(self):
		return [(cname, self._courses[cname]) for cname in self._courses]

	def details(self):
		return " ".join((Person.details(self),
		                 "入学日期: " + str(self._enroll_date),
		                 "院系: " + self._department,
		                 "课程记录: " + str(self.scores())))
	def department(self):
		return self._department

	def en_year(self):
		return self._enroll_date.year

# s1 = Student("谢雨洁", "女", (1995, 7, 30), "PA")
# s2 = Student("汪力强", "男", (1990, 2, 17), "PB")
# s3 = Student("张子玉", "女", (1974, 10, 16), "PC")
# s4 = Student("李国栋", "男", (1962, 5, 24), "PD")
# slist2 = [s1, s2, s3,s4]
#
# for s in slist2:
# 	print(s.details())


class Staff(Person):
	_id_num = 0
	@classmethod
	def _id_gen(cls):
		cls._id_num += 1
		year = datetime.date.today().year
		return "1{:04}{:05}".format(year, cls._id_num)
	def __init__(self, name, sex, birthday, entry_date):
		Person.__init__(self, name, sex, birthday, Student._id_gen())

		try:
			entry_date_d = datetime.date(*entry_date)
		except:
			raise PersonValueError("Wrong date: ", entry_date)
		self._entry_date = entry_date_d
		self._salary = None
		self._position = ""
		self._department = ""

	def set_salary(self, salary):
		if not isinstance(salary, int):
			raise PersonValueError("Wrong salary: ", salary)
		self._salary = salary

	def set_position(self, position):
		self._position = position

	def set_department(self, department):
		self._department = department

	def department(self):
		return self._department

	def entry_date(self):
		return self._entry_date

	def details(self):
		return " ".join((super(Staff, self).details(),
						 "入职日期: " + str(self._entry_date),
		                 "院系: " + self._department,
		                 "职位: " + self._position,
		                 "工资: " + str(self._salary)))
t1 = Staff("谢雨洁", "女", (1995, 7, 30), (2005, 7, 21))
t2 = Staff("汪力强", "男", (1990, 2, 17), (2005, 7, 20))
t3 = Staff("张子玉", "女", (1974, 10, 16), (2005, 7, 22))
t4 = Staff("李国栋", "男", (1962, 5, 24), (1995, 7, 2))
tlist2 = [t1, t2, t3, t4]
for t in tlist2:
	print(t.details())

t1.set_department("PU")
print t1.details()

t1.set_salary(4444)
print t1.details()