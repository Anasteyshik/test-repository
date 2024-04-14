from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('2+2','4', '5', '6', '7'))
questions_list.append(Question('3+3', '6', '7','10', '0'))


    
app = QApplication([])
main_win = QWidget()
main_win.cur_question = -1

main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400, 200)
box = QGroupBox()
box_answer = QGroupBox()
layout_box = QVBoxLayout()
answer_text = QLabel('Прав ты или нет!')
layout_box.addWidget(answer_text, alignment=Qt.AlignCenter)
box_answer.setLayout(layout_box)
question = QLabel('В каком году канал получил «золотую кнопку» от YouTube?')
group_btn = QButtonGroup()
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
group_btn.addButton(btn_answer1)
group_btn.addButton(btn_answer2)
group_btn.addButton(btn_answer3)
group_btn.addButton(btn_answer4)


layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutV1 = QVBoxLayout()
layoutV1.addLayout(layoutH2)
layoutV1.addLayout(layoutH3)
box.setLayout(layoutV1)
btn = QPushButton('Ответить')
layout_main.addLayout(layoutH1)
layout_main.addWidget(box)
layout_main.addWidget(box_answer)
box_answer.hide()
layout_main.addWidget(btn, stretch=2)
main_win.setLayout(layout_main)
 
def show_answer():
    box.hide()
    box_answer.show()
    btn.setText('Следующий вопрос')

def show_question():
    box.show()
    box_answer.hide()
    btn.setText('Ответить')
    group_btn.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    group_btn.setExclusive(True)
answer = [btn_answer1, btn_answer2, btn_answer3,btn_answer4]
def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question)
    
    show_question()
def show_correct(res):
    answer_text.setText(res)
    show_answer()
def check_answer():
    if answer[0].isChecked():
        show_correct('правильный ответ')
    else:
        if answer[1].isChecked() or  answer[2].isChecked() or  answer[3].isChecked():
            show_correct('неправильный ответ')
def next_question():
    main_win.cur_question += 1
   
    if main_win.cur_question >= len (questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)
   

def change():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

next_question()
btn.clicked.connect(change)
main_win.show()
app.exec_()
# comment
