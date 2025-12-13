#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : "GarryZheng"
# __Date__ : 2025-12-13

class Student:
    def __init__(self, student_id, name, age, gender, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def __str__(self):
        return f"学号: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 性别: {self.gender}, 成绩: {self.score}"

class StudentManager:
    def __init__(self):
        self.students = []
        self.username = "admin"
        self.password = "123456"

    def login(self):
        print("=== 学生信息管理系统登录 ===")
        for attempt in range(3):
            input_username = input("用户名: ")
            input_password = input("密码: ")
            if input_username == self.username and input_password == self.password:
                print("登录成功！")
                return True
            else:
                print(f"登录失败，剩余尝试次数: {2 - attempt}")
        print("登录失败次数过多，程序退出。")
        return False

    def add_student(self):
        print("\n=== 录入学生信息 ===")
        student_id = input("请输入学号: ")
        name = input("请输入姓名: ")
        age = input("请输入年龄: ")
        gender = input("请输入性别: ")
        score = input("请输入成绩: ")
        self.students.append(Student(student_id, name, age, gender, score))
        print("学生信息录入成功！")

    def modify_student(self):
        print("\n=== 修改学生信息 ===")
        student_id = input("请输入要修改的学生学号: ")
        for student in self.students:
            if student.student_id == student_id:
                student.name = input(f"请输入新姓名 [{student.name}]: ") or student.name
                student.age = input(f"请输入新年龄 [{student.age}]: ") or student.age
                student.gender = input(f"请输入新性别 [{student.gender}]: ") or student.gender
                student.score = input(f"请输入新成绩 [{student.score}]: ") or student.score
                print("学生信息修改成功！")
                return
        print("未找到该学号的学生信息。")

    def delete_student(self):
        print("\n=== 删除学生信息 ===")
        student_id = input("请输入要删除的学生学号: ")
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("学生信息删除成功！")
                return
        print("未找到该学号的学生信息。")

    def display_students(self):
        print("\n=== 学生信息列表 ===")
        if not self.students:
            print("暂无学生信息。")
            return
        for student in self.students:
            print(student)

    def run(self):
        if not self.login():
            return
        while True:
            print("\n=== 学生信息管理系统主菜单 ===")
            print("1. 录入学生信息")
            print("2. 修改学生信息")
            print("3. 删除学生信息")
            print("4. 显示所有学生信息")
            print("5. 退出系统")
            choice = input("请选择操作 (1-5): ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.modify_student()
            elif choice == "3":
                self.delete_student()
            elif choice == "4":
                self.display_students()
            elif choice == "5":
                print("感谢使用，系统即将退出！")
                break
            else:
                print("无效的选择，请重新输入。")

if __name__ == "__main__":
    manager = StudentManager()
    manager.run()