import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def show_score():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 34, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, men_means, width, label='Men')
    rects2 = ax.bar(x + width / 2, women_means, width, label='Women')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    plt.show()

def show_course(course):
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 230, 45, 10]
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def show_student(stu):
    matplotlib.rcParams['font.family'] = 'Simhei'
    radar_labels = np.array(['数学', '语文', '英语', '化学', '物理', '地理'])
    data = np.array([55, 78, 12, 74, 23, 86])
    angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
    fig = plt.figure(facecolor="white")
    plt.subplot(111, polar=True)
    plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)
    plt.fill(angles, data, alpha=0.25)
    plt.thetagrids(angles * 180 / np.pi, radar_labels)
    plt.grid(True)
    plt.savefig('holland_radar.jpg')
    plt.show()

# 菜单类
class menu (object):
    def __init__(self, master=None):
        self.window = master
        self.window.title("菜单")
        self.window.geometry('%dx%d' % (300, 300))
        self.draw()

    def draw(self):
        self.page = Frame(self.window)  # 创建Frame
        self.page.pack()
        # 1. 指定学生信息统计
        Button(self.page, text='学生信息统计', command=self.student).grid(row=1,column=1, stick=E, pady=10)
        # 2. 指定课程信息统计
        Button(self.page, text='课程信息统计', command=self.course).grid(row=2,column=1, stick=E, pady=10)        # 2. 指定课程信息统计
        # 3. 课程成绩
        Button(self.page, text='课程成绩分布', command=self.scores).grid(row=3,column=1, stick=E, pady=10)        # 2. 指定课程信息统计

    def student(self):
        show_student(1)


    def course(self):
        print("student1")
        show_course(1)


    def scores(self):
        show_score()
        print("student2")



class view():
    def __init__(self):
        # 启动登录界面
        root= tk.Tk()
        root.title('数据查看')
        menu(root)
        root.mainloop()

view()