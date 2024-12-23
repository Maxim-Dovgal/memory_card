from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
)
window_menu = QWidget()
window_menu.resize(400, 300)
window_menu.setWindowTitle("python")

lbl_new_question = QLabel("Введіть запитання:")

lbl_new_correct = QLabel("Введіть правильну відповідь:")

lbl_incorrect_1 = QLabel("Введіть першу хибну відповідь:")
lbl_incorrect_2 = QLabel("Введіть другу хибну відповідь:")
lbl_incorrect_3 = QLabel("Введіть третю хибну відповіть:")

ld_question = QLineEdit()
ld_correct = QLineEdit()
ld_incorrect_1 = QLineEdit()
ld_incorrect_2 = QLineEdit()
ld_incorrect_3 = QLineEdit()

btn_addquestion = QPushButton("Додати запитання")
btn_reset = QPushButton("Очистити")

lbl_statistics = QLabel("Статистика")
lbl_statistics.setStyleSheet("font-size: 20px; font-weight: bold;")
lbl_statistics_info = QLabel("")

btn_back = QPushButton("Назад")

h_question = QHBoxLayout()
h_question.addWidget(lbl_new_question, stretch=1)
h_question.addWidget(ld_question, stretch=1)

h_correct = QHBoxLayout()
h_correct.addWidget(lbl_new_correct, stretch=1)
h_correct.addWidget(ld_correct, stretch=1)

h_incorrect_1 = QHBoxLayout()
h_incorrect_1.addWidget(lbl_incorrect_1, stretch=1)
h_incorrect_1.addWidget(ld_incorrect_1, stretch=1)

h_incorrect_2 = QHBoxLayout()
h_incorrect_2.addWidget(lbl_incorrect_2, stretch=1)
h_incorrect_2.addWidget(ld_incorrect_2, stretch=1)

h_incorrect_3 = QHBoxLayout()
h_incorrect_3.addWidget(lbl_incorrect_3, stretch=1)
h_incorrect_3.addWidget(ld_incorrect_3, stretch=1)

h_btn = QHBoxLayout()
h_btn.addWidget(btn_addquestion)
h_btn.addWidget(btn_reset)

h_static = QHBoxLayout()
h_static.addWidget(lbl_statistics)
h_static.addWidget(lbl_statistics_info)

h_back = QHBoxLayout()
h_back.addWidget(btn_back)

v_main = QVBoxLayout()
v_main.addLayout(h_question)
v_main.addLayout(h_correct)
v_main.addLayout(h_incorrect_1)
v_main.addLayout(h_incorrect_2)
v_main.addLayout(h_incorrect_3)
v_main.addLayout(h_btn)
v_main.addLayout(h_static)
v_main.addLayout(h_back)

window_menu.setLayout(v_main)