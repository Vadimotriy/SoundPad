import sys
from design.menu import Name, excepthook, QApplication


if __name__ == '__main__':  # запуск
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    exe = Name()
    exe.show()
    sys.exit(app.exec())