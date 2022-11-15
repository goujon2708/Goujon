import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QTabWidget
)


class WelPage(QWidget):

    def __init__(self):
        super().__init__()
        wel_tab = QWidget()
        grid = QGridLayout()

        lab_name = QLabel("This is a label")
        git_link = QLabel("This is a link")
        git_link.setOpenExternalLinks(True)
        yt_link = QLabel("Another Link")
        yt_link.setOpenExternalLinks(True)

        grid.addWidget(lab_name, 0, 1)
        grid.addWidget(git_link, 1, 0)
        grid.addWidget(yt_link, 1, 3)

        wel_tab.setLayout(grid)
        wel_tab.show()

class AboutPage(QWidget):

    def __init__(self):
        super().__init__()
        about_tab = QWidget()
        lo = QVBoxLayout()
        purpose = QLabel("A really long label")

        lo.addWidget(purpose)
        about_tab.setLayout(lo)
        about_tab.show()
        
def main():
    w = QWidget()
    layout = QVBoxLayout()
    tw = QTabWidget()
    w.resize(450, 250)
    w.setWindowTitle('Window Title')
    layout.addWidget(tw)

    tw.addTab(WelPage(), "Welcome Screen")
    tw.addTab(AboutPage(), "About")
    tw.show()


    w.setLayout(layout)
    w.show()
    app.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main()