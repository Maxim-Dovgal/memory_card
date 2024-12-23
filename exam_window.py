from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel, QPushButton, QWidget, QRadioButton, QVBoxLayout, QHBoxLayout, QSpinBox, QButtonGroup, QGroupBox
)

exam_win = QWidget()

exam_win.setWindowTitle("Memory card")
exam_win.resize(550, 450)

btn_menu = QPushButton("Меню")
btn_relax = QPushButton("Відпочити")

spin_minutes = QSpinBox()
spin_minutes.setValue(15)

lbl_minutes = QLabel("Хвилин")

lbl_question = QLabel()

rbtrn_1 = QRadioButton("")
rbtrn_2 = QRadioButton("")
rbtrn_3 =QRadioButton("")
rbtrn_4 = QRadioButton("")

AnsGroupBox = QGroupBox("Результат тесту")
lbl_results = QLabel("")
lbl_correct = QLabel("")

radio_button_group = QButtonGroup()

radio_button_group.addButton(rbtrn_1)
radio_button_group.addButton(rbtrn_2)
radio_button_group.addButton(rbtrn_3)
radio_button_group.addButton(rbtrn_4)

btn_answer = QPushButton("Відповісти")

h1 = QHBoxLayout()


h1.addWidget(btn_menu)
h1.addStretch(2)
h1.addWidget(btn_relax)
h1.addWidget(spin_minutes)
h1.addWidget(lbl_minutes)

line_ans = QVBoxLayout()
line_ans.addWidget(lbl_results, alignment=(Qt.AlignLeft|Qt.AlignTop))
line_ans.addWidget(lbl_correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(line_ans)
AnsGroupBox.hide()

h2 = QHBoxLayout()

h2.addWidget(lbl_question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

hb1 = QHBoxLayout()

hb1.addWidget(rbtrn_1)
hb1.addWidget(rbtrn_2)

hb2 = QHBoxLayout()

hb2.addWidget(rbtrn_3)
hb2.addWidget(rbtrn_4)

vb = QVBoxLayout()

vb.addLayout(hb1)
vb.addLayout(hb2)

radio_groupbox = QGroupBox("Варіанти відповідей")
radio_groupbox.setLayout(vb)

h3 = QHBoxLayout()

h3.addWidget(radio_groupbox)
h3.addWidget(AnsGroupBox)

h4 = QHBoxLayout()
h4.addStretch(1)
h4.addWidget(btn_answer, stretch=2)
h4.addStretch(1)

v_main = QVBoxLayout()

v_main.addLayout(h1, stretch=1)
v_main.addLayout(h2, stretch=2)
v_main.addLayout(h3, stretch=8)
v_main.addLayout(h4)

exam_win.setLayout(v_main)