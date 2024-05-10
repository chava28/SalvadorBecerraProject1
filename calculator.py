from PyQt6.QtWidgets import *
from gui import *
import math


class Calculator(QMainWindow, Ui_MainWindow):
    """
    Various variables needed to make functions operate
    """
    nums = ["none", "none"]
    index_num = 0
    operation = 'none'
    del_pass = 0
    first_operation = True
    mode_on = False
    areaCalc = 'none'

    def __init__(self, *args, **kwargs) -> None:
        """
        This initializes the whole function and all the initial values
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.circle.setEnabled(False)
        self.triangle.setEnabled(False)
        self.square.setEnabled(False)
        self.rectangle.setEnabled(False)
        self.enter_1.setEnabled(False)
        self.enter_2.setEnabled(False)
        self.submit.setEnabled(False)

        self.zero.clicked.connect(lambda: self.button_zero())
        self.one.clicked.connect(lambda: self.button_one())
        self.two.clicked.connect(lambda: self.button_two())
        self.three.clicked.connect(lambda: self.button_three())
        self.four.clicked.connect(lambda: self.button_four())
        self.five.clicked.connect(lambda: self.button_five())
        self.six.clicked.connect(lambda: self.button_six())
        self.seven.clicked.connect(lambda: self.button_seven())
        self.eight.clicked.connect(lambda: self.button_eight())
        self.nine.clicked.connect(lambda: self.button_nine())
        self.decimal.clicked.connect(lambda: self.point())
        self.pos_neg.clicked.connect(lambda: self.neg_pos())
        self.add.clicked.connect(lambda: self.addition())
        self.subtract.clicked.connect(lambda: self.subtraction())
        self.multiply.clicked.connect(lambda: self.multiplication())
        self.divide.clicked.connect(lambda: self.division())
        self.equals.clicked.connect(lambda: self.calculate())
        self.clear.clicked.connect(lambda: self.erase())
        self.delete_2.clicked.connect(lambda: self.delete())
        self.mode.clicked.connect(lambda: self.extra())
        self.circle.clicked.connect(lambda: self.circ())
        self.triangle.clicked.connect(lambda: self.tri())
        self.square.clicked.connect(lambda: self.squ())
        self.rectangle.clicked.connect(lambda: self.rect())
        self.submit.clicked.connect(lambda: self.areaSubmit())

    def button_zero(self) -> None:
        """
        This sends the numeric value of zero to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "0"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "0"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_one(self) -> None:
        """
        This sends the numeric value of one to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "1"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "1"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_two(self) -> None:
        """
        This sends the numeric value of two to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "2"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "2"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_three(self) -> None:
        """
        This sends the numeric value of three to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "3"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "3"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_four(self) -> None:
        """
        This sends the numeric value of four to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "4"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "4"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_five(self) -> None:
        """
        This sends the numeric value of five to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "5"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "5"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_six(self) -> None:
        """
        This sends the numeric value of six to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "6"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "6"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_seven(self) -> None:
        """
        This sends the numeric value of seven to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "7"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "7"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_eight(self) -> None:
        """
        This sends the numeric value of eight to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "8"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "8"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def button_nine(self) -> None:
        """
        This sends the numeric value of nine to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "9"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "9"
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def point(self) -> None:
        """
        This sends a decimal to the calculator
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = "0."
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        else:
            Calculator.nums[Calculator.index_num] += "."
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def neg_pos(self) -> None:
        """
        This makes the number in the calculator positive or negative
        :return:
        """
        if Calculator.nums[Calculator.index_num] == 'none':
            Calculator.nums[Calculator.index_num] = '-'
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        elif Calculator.nums[Calculator.index_num] != 'none' and Calculator.nums[Calculator.index_num][0] != '-':
            Calculator.nums[Calculator.index_num] = '-' + Calculator.nums[Calculator.index_num]
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])
        elif Calculator.nums[Calculator.index_num] != 'none' and Calculator.nums[Calculator.index_num][0] == '-':
            Calculator.nums[Calculator.index_num] = Calculator.nums[Calculator.index_num][1:]
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def operate(self) -> None:
        """
        This completes all of the operations that you do
        :return:
        """
        try:
            if Calculator.operation == 'add':
                Calculator.index_num = 1
                Calculator.del_pass += 1
                Calculator.nums[0] = str(float(Calculator.nums[0]) + float(Calculator.nums[1]))
                Calculator.nums[1] = 'none'
                self.textBrowser.setText(Calculator.nums[0])
            elif Calculator.operation == 'subtract':
                Calculator.index_num = 1
                Calculator.del_pass += 1
                Calculator.nums[0] = str(float(Calculator.nums[0]) - float(Calculator.nums[1]))
                Calculator.nums[1] = 'none'
                self.textBrowser.setText(Calculator.nums[0])
            elif Calculator.operation == 'multiply':
                Calculator.index_num = 1
                Calculator.del_pass += 1
                Calculator.nums[0] = str(float(Calculator.nums[0]) * float(Calculator.nums[1]))
                Calculator.nums[1] = 'none'
                self.textBrowser.setText(Calculator.nums[0])
            elif Calculator.operation == 'divide':
                Calculator.index_num = 1
                Calculator.del_pass += 1
                Calculator.nums[0] = str(float(Calculator.nums[0]) / float(Calculator.nums[1]))
                Calculator.nums[1] = 'none'
                self.textBrowser.setText(Calculator.nums[0])
        except ValueError:
            Calculator.index_num = 0
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def addition(self) -> None:
        """
        This saves the operation as add for the operate function
        :return:
        """
        self.textBrowser.clear()
        if Calculator.nums[1] == 'none' and Calculator.first_operation == True:
            Calculator.index_num += 1
            if Calculator.index_num > 1:
                Calculator.index_num = 1
            Calculator.del_pass += 1
            Calculator.first_operation = False
            Calculator.operation = 'add'
        else:
            self.operate()
            Calculator.operation = 'add'
            Calculator.nums[1] = 'none'
            self.textBrowser.setText(Calculator.nums[0])

    def subtraction(self) -> None:
        """
        This saves the operation as subtraction for the operate function
        :return:
        """
        self.textBrowser.clear()
        if Calculator.nums[1] == 'none' and Calculator.first_operation == True:
            Calculator.index_num += 1
            if Calculator.index_num > 1:
                Calculator.index_num = 1
            Calculator.del_pass += 1
            Calculator.first_operation = False
            Calculator.operation = 'subtract'
        else:
            self.operate()
            Calculator.operation = 'subtract'
            Calculator.nums[1] = 'none'
            self.textBrowser.setText(Calculator.nums[0])

    def multiplication(self) -> None:
        """
        This saves the operation as multuplication for the operate function
        :return:
        """
        self.textBrowser.clear()
        if Calculator.nums[1] == 'none' and Calculator.first_operation == True:
            Calculator.index_num += 1
            Calculator.del_pass += 1
            Calculator.first_operation = False
            Calculator.operation = 'multiply'
        else:
            self.operate()
            Calculator.operation = 'multiply'
            Calculator.nums[1] = 'none'
            self.textBrowser.setText(Calculator.nums[0])

    def division(self) -> None:
        """
        This saves the operation as division for the operate function
        :return:
        """
        self.textBrowser.clear()
        if Calculator.nums[1] == 'none' and Calculator.first_operation == True:
            Calculator.index_num += 1
            Calculator.del_pass += 1
            Calculator.first_operation = False
            Calculator.operation = 'divide'
        else:
            self.operate()
            Calculator.operation = 'divide'
            Calculator.nums[1] = 'none'
            self.textBrowser.setText(Calculator.nums[0])

    def calculate(self) -> None:
        """
        Makes it so that when the = button is clicked the final operation is calculated
        :return:
        """
        self.operate()

    def erase(self) -> None:
        """
        Gets rid of everything and you can restart your calculations
        :return:
        """
        self.textBrowser.clear()
        Calculator.nums[0] = 'none'
        Calculator.nums[1] = 'none'
        Calculator.index_num = 0
        Calculator.operation = 'none'
        Calculator.del_pass = 0
        Calculator.first_operation = True

    def delete(self) -> None:
        """
        Removes the last character from your numeric entry
        :return:
        """
        if Calculator.nums[1] == 'none' and Calculator.del_pass > 0:
            pass
        else:
            Calculator.nums[Calculator.index_num] = Calculator.nums[Calculator.index_num][
                                                    :len(Calculator.nums[Calculator.index_num]) - 1]
            self.textBrowser.setText(Calculator.nums[Calculator.index_num])

    def extra(self) -> None:
        """
        Changes between the calculator and the shape area calculator
        :return:
        """
        if Calculator.mode_on == False:
            Calculator.mode_on = True
            self.zero.setEnabled(False)
            self.one.setEnabled(False)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.four.setEnabled(False)
            self.five.setEnabled(False)
            self.six.setEnabled(False)
            self.seven.setEnabled(False)
            self.eight.setEnabled(False)
            self.nine.setEnabled(False)
            self.pos_neg.setEnabled(False)
            self.add.setEnabled(False)
            self.subtract.setEnabled(False)
            self.multiply.setEnabled(False)
            self.divide.setEnabled(False)
            self.decimal.setEnabled(False)
            self.equals.setEnabled(False)
            self.delete_2.setEnabled(False)

            self.circle.setEnabled(True)
            self.triangle.setEnabled(True)
            self.square.setEnabled(True)
            self.rectangle.setEnabled(True)
            self.enter_1.setEnabled(True)
            self.enter_2.setEnabled(True)
            self.submit.setEnabled(True)
        else:
            Calculator.mode_on = False
            self.zero.setEnabled(True)
            self.one.setEnabled(True)
            self.two.setEnabled(True)
            self.three.setEnabled(True)
            self.four.setEnabled(True)
            self.five.setEnabled(True)
            self.six.setEnabled(True)
            self.seven.setEnabled(True)
            self.eight.setEnabled(True)
            self.nine.setEnabled(True)
            self.pos_neg.setEnabled(True)
            self.add.setEnabled(True)
            self.subtract.setEnabled(True)
            self.multiply.setEnabled(True)
            self.divide.setEnabled(True)
            self.decimal.setEnabled(True)
            self.equals.setEnabled(True)
            self.delete_2.setEnabled(True)

            self.circle.setEnabled(False)
            self.triangle.setEnabled(False)
            self.square.setEnabled(False)
            self.rectangle.setEnabled(False)
            self.enter_1.setEnabled(False)
            self.enter_2.setEnabled(False)
            self.submit.setEnabled(False)
            self.label_1.setText('')
            self.label_2.setText('')

    def circ(self) -> None:
        """
        Sets up code to input the Circle requirements
        :return:
        """
        self.enter_2.setEnabled(False)
        self.label_1.setText('Radius')
        self.label_2.setText('')
        Calculator.areaCalc = 'circ'

    def tri(self) -> None:
        """
        Sets up code to input the Triangle requirements
        :return:
        """
        self.enter_2.setEnabled(True)
        self.label_1.setText('Base')
        self.label_2.setText('Height')
        Calculator.areaCalc = 'tri'

    def squ(self) -> None:
        """
        Sets up code to input the Square requirements
        :return:
        """
        self.enter_2.setEnabled(False)
        self.label_1.setText('Side')
        self.label_2.setText('')
        Calculator.areaCalc = 'squ'

    def rect(self) -> None:
        """
        Sets up code to input the Rectangle requirements
        :return:
        """
        self.enter_2.setEnabled(True)
        self.label_1.setText('Length')
        self.label_2.setText('Width')
        Calculator.areaCalc = 'rect'

    def areaSubmit(self) -> None:
        """
        Calculates the area for each of the individual shapes
        :return:
        """
        if Calculator.areaCalc == 'circ':
            try:
                if float(self.enter_1.text()) <= 0:
                    raise TypeError
                else:
                    self.textBrowser.setText(
                        f' Area = {math.pi * (float(self.enter_1.text()) * float(self.enter_1.text()))}')
            except TypeError:
                self.textBrowser.setText('Please Enter Numeric Values above 0')
        elif Calculator.areaCalc == 'tri':
            try:
                if float(self.enter_1.text()) <= 0 or float(self.enter_2.text()) <= 0:
                    raise TypeError
                else:
                    self.textBrowser.setText(f'Area = {0.5 * float(self.enter_1.text()) * float(self.enter_2.text())}')
            except TypeError:
                self.textBrowser.setText('Please Enter Numeric Values above 0')
        elif Calculator.areaCalc == 'squ':
            try:
                if float(self.enter_1.text()) <= 0:
                    raise TypeError
                else:
                    self.textBrowser.setText(f'Area = {float(self.enter_1.text()) * float(self.enter_1.text())}')
            except TypeError:
                self.textBrowser.setText('Please Enter Numeric Values above 0')
        elif Calculator.areaCalc == 'rect':
            try:
                if float(self.enter_1.text()) <= 0 or float(self.enter_2.text()) <= 0:
                    raise TypeError
                else:
                    self.textBrowser.setText(f'Area = {float(self.enter_1.text()) * float(self.enter_2.text())}')
            except TypeError:
                self.textBrowser.setText('Please Enter Numeric Values above 0')
        else:
            self.textBrowser.setText(f'Must enter values')
