from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100,100,200,300)
    window.setWindowTitle("Title!")


    # layout helps to diplay the boxes vertically QVerticalBox
    layout = QVBoxLayout()

    label = QLabel("press the btn")
    textbox = QTextEdit()

    button = QPushButton("Press me")
    
    # Trigger the function
    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(button)
    layout.addWidget(textbox)

    window.setLayout(layout)


    window.show()
    app.exec()



# Display the text from the textbox when the button is trigged
def on_clicked(msg):
    message = QMessageBox()
    message.setText(msg)
    message.exec()


if __name__ == '__main__':
    main()