import pandas as pd
import matplotlib.pyplot as plt

class Grade:
    def __init__(self, student_id, course_id, grade_value):
        self.student_id = student_id
        self.course_id = course_id
        self.grade_value = grade_value

    def __str__(self):
        return f"Student ID: {self.student_id}, Course ID: {self.course_id}, Grade: {self.grade_value}"

    @staticmethod
    def get_statistics(grades_list, course_id):
        print(f"Received grades_list: {grades_list}")
        print(f"Calculating statistics for course_id: {course_id}")
        
        # 筛选特定课程的成绩
        course_grades = [g.grade_value for g in grades_list if g.course_id == course_id]
        
        if not course_grades:
            print(f"No grades available for course ID {course_id}.")
            return
        
        # 转换为 DataFrame 进行统计计算
        df_grades = pd.DataFrame(course_grades, columns=["grade_value"])
        
        # 计算中位数、最大值和最小值
        median_grade = df_grades["grade_value"].median()
        max_grade = df_grades["grade_value"].max()
        min_grade = df_grades["grade_value"].min()
        
        # 显示统计信息
        print(f"\nStatistics for Course ID {course_id}:")
        print(f"Median: {median_grade}")
        print(f"Max: {max_grade}")
        print(f"Min: {min_grade}")
        
        # 绘制箱型图
        plt.figure(figsize=(6, 4))
        plt.boxplot(df_grades["grade_value"], vert=False)
        plt.title(f"Boxplot of Grades for Course ID {course_id}")
        plt.xlabel("Grade Value")
        plt.show()