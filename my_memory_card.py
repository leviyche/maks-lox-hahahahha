#создай приложение для запоминания
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('.-MEMORY CARD-.')
main_win.resize(600, 500)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Первая буква алфавита', 'а', 'б', 'в', 'г'))
questions_list.append(Question('Сколько хп дает армлет', '500', '450', '400', '300'))
questions_list.append(Question('Сколько персонажей в доте', '120', '124', '121', '130'))
questions_list.append(Question('Сколько денег дает мидас', '160', '320', '80', '240'))
question =  QLabel('Сколько персонажей в Dota 2?')

button1 = QRadioButton('118')
button2 = QRadioButton('115')
button3 = QRadioButton('124')
button4 = QRadioButton('110')

answer_button = QPushButton('Ответить')

radio_vline1 = QVBoxLayout()
radio_vline2 = QVBoxLayout()

radio_vline1.addWidget(button1)
radio_vline1.addWidget(button2)

radio_vline2.addWidget(button3)
radio_vline2.addWidget(button4)

radio_hline = QHBoxLayout()
radio_hline.addLayout(radio_vline1)
radio_hline.addLayout(radio_vline2)

RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox.setLayout(radio_hline)
RadioGroupBox.show()

AnsGroupBox = QGroupBox('Результаты теста')
txt_result = QLabel('Верно/Неверно')
txt_answer = QLabel('Ответ')

ans_vline = QVBoxLayout()
ans_vline.addWidget(txt_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
ans_vline.addWidget(txt_answer, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(ans_vline)
AnsGroupBox.hide()

total_text = QLabel('Всего вопросов: 0')
correct_text = QLabel('Правильных ответов: 0')
rating_text = QLabel('Рейтинг: 0%')

StatGroupBox = QGroupBox('Статистика')
stat_vline = QVBoxLayout()
stat_vline.addWidget(total_text, alignment=(Qt.AlignLeft | Qt.AlignTop))
stat_vline.addWidget(correct_text, alignment=(Qt.AlignLeft | Qt.AlignTop))
stat_vline.addWidget(rating_text, alignment=(Qt.AlignLeft | Qt.AlignTop))
StatGroupBox.setLayout(stat_vline)

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()

hline1.addWidget(question, alignment=Qt.AlignHCenter)
hline2.addWidget(answer_button, alignment=Qt.AlignHCenter)

main_vline = QVBoxLayout()
main_vline.addWidget(StatGroupBox)
main_vline.addLayout(hline1)
main_vline.addWidget(RadioGroupBox)
main_vline.addWidget(AnsGroupBox)
main_vline.addLayout(hline2)
main_win.setLayout(main_vline)

RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer_button.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)

from random import shuffle, randint
answers = [button1, button2, button3, button4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    txt_answer.setText(q.right_answer)
    show_question()

def show_correct(res):
    txt_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.correct += 1
        correct_text.setText('Правильных ответов:' + str(main_win.correct))
        rating = main_win.correct / main_win.total * 100
        rating_text.setText('Рейтинг:' + str(rating) + '%')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно!')

def next_question():
    main_win.total += 1
    total_text.setText('Всего вопросов: ' + str(main_win.total))
    rating = main_win.correct / main_win.total * 100
    rating_text.setText('Рейтинг:' + str(rating) + '%')
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)
def click_ok():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
main_win.total = 0
main_win.correct = 0

answer_button.clicked.connect(click_ok)
next_question()
main_win.show()
app.exec_()