#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : "GarryZheng"
# __Date__ : 2025-12-13


"""
学生信息管理系统 - 增强版
修复了联系电话输入可能导致的问题
"""

import os
import json
import hashlib
import re

class StudentManagementSystem:
    def __init__(self):
        """初始化系统"""
        self.students_file = "students.json"
        self.users_file = "users.json"
        self.current_user = None
        self.students = self.load_students()
        self.users = self.load_users()
        
        # 如果用户文件不存在，创建默认管理员
        if not os.path.exists(self.users_file):
            self.create_default_admin()
    
    def validate_phone(self, phone):
        """验证电话号码格式"""
        if not phone:  # 允许为空
            return True, ""
        
        # 清理电话号码：移除所有非数字字符（除了+号）
        cleaned_phone = re.sub(r'[^\d+]', '', phone)
        
        # 简单验证：至少应该有7位数字，最多15位
        digits_only = re.sub(r'\D', '', phone)
        if 7 <= len(digits_only) <= 15:
            return True, cleaned_phone
        else:
            return False, "电话号码应该在7-15位数字之间"
    
    def safe_input(self, prompt, validation_func=None, allow_empty=False):
        """安全的输入函数，处理各种输入异常"""
        while True:
            try:
                value = input(prompt).strip()
                
                # 检查是否允许空值
                if allow_empty and value == "":
                    return value
                
                # 如果有验证函数，使用它
                if validation_func:
                    is_valid, message_or_value = validation_func(value)
                    if is_valid:
                        return message_or_value if isinstance(message_or_value, str) else value
                    else:
                        print(f"输入错误: {message_or_value}")
                        continue
                
                # 没有验证函数，直接返回
                return value
                
            except EOFError:
                print("\n检测到EOF，返回主菜单")
                return None
            except KeyboardInterrupt:
                print("\n操作已取消")
                return None
            except Exception as e:
                print(f"输入时发生错误: {e}")
                choice = input("是否重试？(y/n): ").lower()
                if choice != 'y':
                    return None
    
    def load_students(self):
        """从文件加载学生信息"""
        try:
            if os.path.exists(self.students_file):
                with open(self.students_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 确保数据是字典格式
                    if isinstance(data, dict):
                        return data
                    else:
                        print("警告：学生数据格式不正确，已重置")
                        return {}
            return {}
        except Exception as e:
            print(f"加载学生数据时出错: {e}")
            # 尝试恢复备份文件
            backup_file = "students.json.bak"
            if os.path.exists(backup_file):
                print("尝试从备份文件恢复...")
                try:
                    with open(backup_file, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except:
                    print("备份文件也损坏了")
            return {}
    
    def save_students(self):
        """保存学生信息到文件"""
        try:
            # 先备份当前文件
            if os.path.exists(self.students_file):
                import shutil
                shutil.copy2(self.students_file, self.students_file + ".bak")
            
            # 保存新文件
            with open(self.students_file, 'w', encoding='utf-8') as f:
                json.dump(self.students, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"保存学生数据时出错: {e}")
            return False
    
    def load_users(self):
        """从文件加载用户信息"""
        try:
            if os.path.exists(self.users_file):
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"加载用户数据时出错: {e}")
            return {}
    
    def save_users(self):
        """保存用户信息到文件"""
        try:
            with open(self.users_file, 'w', encoding='utf-8') as f:
                json.dump(self.users, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"保存用户数据时出错: {e}")
            return False
    
    def hash_password(self, password):
        """密码加密"""
        try:
            return hashlib.sha256(password.encode()).hexdigest()
        except:
            return ""
    
    def create_default_admin(self):
        """创建默认管理员账户"""
        self.users = {
            "admin": {
                "password": self.hash_password("admin123"),
                "role": "admin",
                "name": "系统管理员"
            }
        }
        if self.save_users():
            print("已创建默认管理员账号: admin, 密码: admin123")
    
    def clear_screen(self):
        """清屏函数"""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except:
            print("\n" * 50)  # 如果清屏失败，至少打印一些空行
    
    def display_header(self, title):
        """显示标题头"""
        self.clear_screen()
        print("=" * 60)
        print(" " * 20 + "学生信息管理系统")
        print("=" * 60)
        if self.current_user:
            print(f"当前用户: {self.current_user}")
        print(f"功能: {title}")
        print("-" * 60)
    
    def login(self):
        """用户登录"""
        self.display_header("用户登录")
        
        while True:
            username = self.safe_input("请输入用户名: ")
            if username is None:
                return False
            
            password = self.safe_input("请输入密码: ")
            if password is None:
                return False
            
            if not username or not password:
                print("用户名和密码不能为空！")
                choice = self.safe_input("是否重试？(y/n): ")
                if choice and choice.lower() != 'y':
                    return False
                continue
            
            if username in self.users:
                hashed_password = self.hash_password(password)
                if self.users[username]["password"] == hashed_password:
                    self.current_user = self.users[username]["name"]
                    print(f"登录成功！欢迎您，{self.current_user}")
                    self.safe_input("按回车键继续...")
                    return True
            
            print("用户名或密码错误！")
            choice = self.safe_input("是否重试？(y/n): ")
            if not choice or choice.lower() != 'y':
                return False
    
    def add_student(self):
        """添加学生信息"""
        self.display_header("录入学生信息")
        
        while True:
            print("\n录入新学生信息 (输入q返回主菜单)")
            print("-" * 40)
            
            student_id = self.safe_input("请输入学号: ")
            if student_id is None or student_id.lower() == 'q':
                return
            
            # 检查学号是否已存在
            if student_id in self.students:
                print(f"学号 {student_id} 已存在！")
                continue
            
            name = self.safe_input("请输入姓名: ")
            if name is None:
                return
            if not name:
                print("姓名不能为空！")
                continue
            
            gender = self.safe_input("请输入性别(男/女): ")
            if gender is None:
                return
            while gender not in ['男', '女']:
                print("性别输入错误，请重新输入！")
                gender = self.safe_input("请输入性别(男/女): ")
                if gender is None:
                    return
            
            age = self.safe_input("请输入年龄: ")
            if age is None:
                return
            while not age.isdigit() or not (1 <= int(age) <= 100):
                print("年龄输入错误，请重新输入(1-100)！")
                age = self.safe_input("请输入年龄: ")
                if age is None:
                    return
            
            major = self.safe_input("请输入专业: ", allow_empty=True)
            if major is None:
                return
            
            # 加强版的电话号码输入
            while True:
                phone = self.safe_input("请输入联系电话(可选，7-15位数字，可包含+-号): ", allow_empty=True)
                if phone is None:
                    return
                
                if phone == "":  # 允许为空
                    cleaned_phone = ""
                    break
                
                # 验证电话号码
                is_valid, result = self.validate_phone(phone)
                if is_valid:
                    cleaned_phone = result
                    break
                else:
                    print(f"提示: {result}")
                    choice = self.safe_input("是否重新输入？(y)或跳过留空(n): ")
                    if choice and choice.lower() == 'n':
                        cleaned_phone = ""
                        break
            
            # 保存学生信息
            self.students[student_id] = {
                "学号": student_id,
                "姓名": name,
                "性别": gender,
                "年龄": int(age),
                "专业": major if major else "未指定",
                "联系电话": cleaned_phone
            }
            
            if self.save_students():
                print(f"\n学生 {name} 的信息已成功录入！")
            else:
                print("警告：保存学生信息时出现问题！")
            
            choice = self.safe_input("\n是否继续录入？(y/n): ")
            if not choice or choice.lower() != 'y':
                break
    
    def modify_student(self):
        """修改学生信息"""
        self.display_header("修改学生信息")
        
        if not self.students:
            print("暂无学生信息，请先录入学生信息！")
            self.safe_input("按回车键返回...")
            return
        
        while True:
            print("\n当前所有学生:")
            print("-" * 60)
            print(f"{'学号':<10} {'姓名':<8} {'性别':<4} {'年龄':<4} {'专业':<12} {'联系电话':<12}")
            print("-" * 60)
            
            for student_id, info in self.students.items():
                phone_display = info['联系电话'] if info['联系电话'] else "未填写"
                print(f"{info['学号']:<10} {info['姓名']:<8} {info['性别']:<4} "
                      f"{info['年龄']:<4} {info['专业']:<12} {phone_display:<12}")
            
            print("\n修改学生信息 (输入q返回主菜单)")
            print("-" * 40)
            
            student_id = self.safe_input("请输入要修改的学生学号: ")
            if student_id is None or student_id.lower() == 'q':
                return
            
            if student_id not in self.students:
                print(f"学号 {student_id} 不存在！")
                continue
            
            # 显示当前信息
            print(f"\n当前学生信息:")
            student = self.students[student_id]
            for key, value in student.items():
                display_value = value if value else "未填写"
                print(f"{key}: {display_value}")
            
            print("\n请选择要修改的字段 (输入q结束修改):")
            print("1. 姓名")
            print("2. 性别")
            print("3. 年龄")
            print("4. 专业")
            print("5. 联系电话")
            print("6. 修改所有信息")
            
            while True:
                choice = self.safe_input("\n请选择(1-6): ")
                
                if choice is None or choice.lower() == 'q':
                    break
                
                try:
                    if choice == '1':
                        new_name = self.safe_input(f"请输入新的姓名 (当前: {student['姓名']}): ")
                        if new_name is None:
                            break
                        if new_name:
                            student['姓名'] = new_name
                    elif choice == '2':
                        new_gender = self.safe_input(f"请输入新的性别 (当前: {student['性别']}): ")
                        if new_gender is None:
                            break
                        while new_gender not in ['男', '女']:
                            print("性别输入错误，请重新输入！")
                            new_gender = self.safe_input("请输入性别(男/女): ")
                            if new_gender is None:
                                break
                        if new_gender:
                            student['性别'] = new_gender
                    elif choice == '3':
                        new_age = self.safe_input(f"请输入新的年龄 (当前: {student['年龄']}): ")
                        if new_age is None:
                            break
                        while new_age and (not new_age.isdigit() or not (1 <= int(new_age) <= 100)):
                            print("年龄输入错误，请重新输入(1-100)！")
                            new_age = self.safe_input("请输入年龄: ")
                            if new_age is None:
                                break
                        if new_age:
                            student['年龄'] = int(new_age)
                    elif choice == '4':
                        new_major = self.safe_input(f"请输入新的专业 (当前: {student['专业']}): ", allow_empty=True)
                        if new_major is None:
                            break
                        student['专业'] = new_major if new_major else "未指定"
                    elif choice == '5':
                        # 加强版的电话号码修改
                        current_phone = student['联系电话'] if student['联系电话'] else "未填写"
                        while True:
                            new_phone = self.safe_input(f"请输入新的联系电话 (当前: {current_phone}): ", allow_empty=True)
                            if new_phone is None:
                                break
                            
                            if new_phone == "":
                                student['联系电话'] = ""
                                break
                            
                            is_valid, result = self.validate_phone(new_phone)
                            if is_valid:
                                student['联系电话'] = result
                                break
                            else:
                                print(f"提示: {result}")
                                choice2 = self.safe_input("是否重新输入？(y)或留空(n): ")
                                if choice2 and choice2.lower() == 'n':
                                    student['联系电话'] = ""
                                    break
                    elif choice == '6':
                        # 修改所有信息
                        new_name = self.safe_input(f"请输入姓名 (当前: {student['姓名']}): ")
                        if new_name is None:
                            break
                        if new_name:
                            student['姓名'] = new_name
                        
                        new_gender = self.safe_input(f"请输入性别 (当前: {student['性别']}): ")
                        if new_gender is None:
                            break
                        while new_gender and new_gender not in ['男', '女']:
                            print("性别输入错误，请重新输入！")
                            new_gender = self.safe_input("请输入性别(男/女): ")
                            if new_gender is None:
                                break
                        if new_gender:
                            student['性别'] = new_gender
                        
                        new_age = self.safe_input(f"请输入年龄 (当前: {student['年龄']}): ")
                        if new_age is None:
                            break
                        while new_age and (not new_age.isdigit() or not (1 <= int(new_age) <= 100)):
                            print("年龄输入错误，请重新输入(1-100)！")
                            new_age = self.safe_input("请输入年龄: ")
                            if new_age is None:
                                break
                        if new_age:
                            student['年龄'] = int(new_age)
                        
                        new_major = self.safe_input(f"请输入专业 (当前: {student['专业']}): ", allow_empty=True)
                        if new_major is None:
                            break
                        student['专业'] = new_major if new_major else "未指定"
                        
                        # 电话号码输入
                        current_phone = student['联系电话'] if student['联系电话'] else "未填写"
                        while True:
                            new_phone = self.safe_input(f"请输入联系电话 (当前: {current_phone}): ", allow_empty=True)
                            if new_phone is None:
                                break
                            
                            if new_phone == "":
                                student['联系电话'] = ""
                                break
                            
                            is_valid, result = self.validate_phone(new_phone)
                            if is_valid:
                                student['联系电话'] = result
                                break
                            else:
                                print(f"提示: {result}")
                                choice2 = self.safe_input("是否重新输入？(y)或留空(n): ")
                                if choice2 and choice2.lower() == 'n':
                                    student['联系电话'] = ""
                                    break
                    else:
                        print("无效选择，请重新输入！")
                        continue
                    
                    if self.save_students():
                        print("修改已保存！")
                    else:
                        print("警告：保存修改时出现问题！")
                    
                    more = self.safe_input("是否继续修改其他字段？(y/n): ")
                    if not more or more.lower() != 'y':
                        break
                except Exception as e:
                    print(f"修改过程中发生错误: {e}")
                    break
            
            if self.save_students():
                print(f"\n学生 {student_id} 的信息已成功修改！")
            else:
                print("警告：保存修改时出现问题！")
            
            choice = self.safe_input("\n是否继续修改其他学生？(y/n): ")
            if not choice or choice.lower() != 'y':
                break
    
    def delete_student(self):
        """删除学生信息"""
        self.display_header("删除学生信息")
        
        if not self.students:
            print("暂无学生信息！")
            self.safe_input("按回车键返回...")
            return
        
        while True:
            print("\n当前所有学生:")
            print("-" * 60)
            print(f"{'学号':<10} {'姓名':<8} {'性别':<4} {'年龄':<4} {'专业':<12} {'联系电话':<12}")
            print("-" * 60)
            
            for student_id, info in self.students.items():
                phone_display = info['联系电话'] if info['联系电话'] else "未填写"
                print(f"{info['学号']:<10} {info['姓名']:<8} {info['性别']:<4} "
                      f"{info['年龄']:<4} {info['专业']:<12} {phone_display:<12}")
            
            print("\n删除学生信息 (输入q返回主菜单)")
            print("-" * 40)
            
            student_id = self.safe_input("请输入要删除的学生学号: ")
            if student_id is None or student_id.lower() == 'q':
                return
            
            if student_id not in self.students:
                print(f"学号 {student_id} 不存在！")
                continue
            
            # 确认删除
            student = self.students[student_id]
            print(f"\n要删除的学生信息:")
            for key, value in student.items():
                display_value = value if value else "未填写"
                print(f"{key}: {display_value}")
            
            confirm = self.safe_input(f"\n确定要删除学生 {student['姓名']} 吗？(y/n): ")
            if confirm and confirm.lower() == 'y':
                del self.students[student_id]
                if self.save_students():
                    print(f"学生 {student['姓名']} 的信息已成功删除！")
                else:
                    print("警告：删除信息时保存出现问题！")
            
            choice = self.safe_input("\n是否继续删除其他学生？(y/n): ")
            if not choice or choice.lower() != 'y':
                break
    
    def display_all_students(self):
        """显示所有学生信息"""
        self.display_header("查看所有学生信息")
        
        if not self.students:
            print("暂无学生信息！")
            self.safe_input("按回车键返回...")
            return
        
        print(f"\n共找到 {len(self.students)} 名学生:")
        print("-" * 70)
        print(f"{'学号':<10} {'姓名':<8} {'性别':<4} {'年龄':<4} {'专业':<15} {'联系电话':<12}")
        print("-" * 70)
        
        for student_id, info in self.students.items():
            phone_display = info['联系电话'] if info['联系电话'] else "未填写"
            print(f"{info['学号']:<10} {info['姓名']:<8} {info['性别']:<4} "
                  f"{info['年龄']:<4} {info['专业']:<15} {phone_display:<12}")
        
        print("-" * 70)
        self.safe_input("\n按回车键返回主菜单...")
    
    def main_menu(self):
        """主菜单"""
        while True:
            self.display_header("主菜单")
            
            print("1. 录入学生信息")
            print("2. 修改学生信息")
            print("3. 删除学生信息")
            print("4. 查看所有学生")
            print("0. 退出系统")
            
            print("-" * 60)
            
            choice = self.safe_input("请选择操作(0-4): ")
            
            if choice is None:
                continue
            elif choice == '0':
                print("感谢使用学生信息管理系统，再见！")
                break
            elif choice == '1':
                self.add_student()
            elif choice == '2':
                self.modify_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.display_all_students()
            else:
                print("无效选择，请重新输入！")
                self.safe_input("按回车键继续...")
    
    def run(self):
        """运行系统"""
        # 显示欢迎界面
        self.display_header("欢迎使用")
        print("欢迎使用学生信息管理系统 - 增强版")
        print("版本: 1.1 (修复了联系电话输入问题)")
        print("-" * 60)
        self.safe_input("按回车键进入登录界面...")
        
        # 登录
        if not self.login():
            print("登录失败，系统退出！")
            return
        
        # 显示主菜单
        self.main_menu()

def main():
    """主函数"""
    try:
        system = StudentManagementSystem()
        system.run()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断")
    except Exception as e:
        print(f"\n程序发生未预期错误: {e}")
        print("请检查数据文件是否损坏")
        input("按回车键退出...")

if __name__ == "__main__":
    main()

