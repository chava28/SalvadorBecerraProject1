from calculator import *

def main():
    app = QApplication([])
    MainWindow = Calculator()
    MainWindow.show()
    app.exec()

if __name__ == '__main__':
    main()