from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication
)




app = QApplication([])
from exam_window import *
from menu_window import *
from time import sleep
from random import choice, shuffle
#клас для зберігання запитань
class Question:
    def __init__(self, question, correct, incorrect_1, incorrect_2, incorrect_3):
        self.question = question
        self.correct = correct
        self.incorrect_1 = incorrect_1
        self.incorrect_2 = incorrect_2
        self.incorrect_3 = incorrect_3

count_ask = 0
count_right = 0
q1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')
q5 = Question('Мед', 'Honey', 'Sweets', 'Pollen', 'bee food')

radio_buttons = [rbtrn_1, rbtrn_2, rbtrn_3, rbtrn_4]
questions = [q1, q2, q3, q4, q5]

def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_correct.setText(cur_quest.correct)

    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_quest.incorrect_1)
    radio_buttons[1].setText(cur_quest.incorrect_2)
    radio_buttons[2].setText(cur_quest.incorrect_3)
    radio_buttons[3].setText(cur_quest.correct)

new_question()

def check():
    global count_ask, count_right
    radio_button_group.setExclusive(False)
    for correct in radio_buttons:
        if correct.isChecked():
            if correct.text() == lbl_correct.text():
                count_ask += 1
                count_right += 1
                lbl_results.setText("Правильно")
                correct.setChecked(False)
                break
            else:
                lbl_results.setText("Не правильно")
                correct.setChecked(False)
                count_ask += 1
    radio_button_group.setExclusive(True)

def add_new_question():
    q = Question(ld_question.text(), ld_correct.text(), ld_incorrect_1.text(), ld_incorrect_2.text(), ld_incorrect_3.text())
    if ld_question.text() != '' and ld_correct.text() != '' and ld_incorrect_1.text() != '' and ld_incorrect_2.text() != '' and ld_incorrect_3.text() != '':
        questions.append(q)
    reset()
btn_addquestion.clicked.connect(add_new_question)

def switch_screen():
    if btn_answer.text() == 'Відповісти':
        check()
        radio_groupbox.hide()
        AnsGroupBox.show()

        btn_answer.setText("Наступне запитання")
    else:
        new_question()

        AnsGroupBox.hide()
        radio_groupbox.show()

        btn_answer.setText("Відповісти")
btn_answer.clicked.connect(switch_screen)
def to_menu():
    exam_win.hide()
    if count_ask == 0:
        c = 0
    else:
        c = (count_right/count_ask) * 100

    text = f'Всього відповідей: {count_ask}\n' \
            f'Правильних відповідей: {count_right}\n' \
            f'Успішність: {round(c, 2)}%'
    
    lbl_statistics_info.setText(text)

    window_menu.show()
btn_menu.clicked.connect(to_menu)

def to_exam():
    window_menu.hide()
    exam_win.show()
btn_back.clicked.connect(to_exam)



def reset():
    ld_question.clear()
    ld_correct.clear()
    ld_incorrect_1.clear()
    ld_incorrect_2.clear()
    ld_incorrect_3.clear()
btn_reset.clicked.connect(reset)

def relax():
    exam_win.hide()
    sleep(spin_minutes.value() * 60)
    exam_win.show()
btn_relax.clicked.connect(relax)

exam_win.show()
app.exec_()