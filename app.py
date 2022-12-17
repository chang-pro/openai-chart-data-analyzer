import os
import openai
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import QSize

# Set the OpenAI API key
openai.api_key =

# Read the chart data from the file
with open("chart.txt", "r") as f:
    chart_data = f.read()

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Set the window properties
        self.setWindowTitle("GPT-3 Question Answering")
        self.setMinimumSize(QSize(600, 400))
        self.setMaximumSize(QSize(600, 400))

        # Create the question input field
        self.question_input = QLineEdit(self)
        self.question_input.move(20, 20)
        self.question_input.resize(560, 40)
        # Connect the returnPressed signal to the on_return_pressed slot
        self.question_input.returnPressed.connect(self.on_return_pressed)

        # Create the submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(500, 80)
        self.submit_button.clicked.connect(self.on_submit)

        # Create the response output field
        self.response_output = QTextEdit(self)
        self.response_output.move(20, 120)
        self.response_output.resize(560, 260)
        self.response_output.setReadOnly(True)

    def on_return_pressed(self):
        # When the user presses the Enter key, press the submit button
        self.submit_button.click()

    def on_submit(self):
        # Get the question from the input field
        question = self.question_input.text()

        # Use the GPT-3 model to generate a response to the question
        response = openai.Completion.create(
            prompt=f"{question}\n{chart_data}",
            engine="text-davinci-003",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        #Extract the text from the response object
        response_text = response["choices"][0]["text"]
        # Display the response in the output field
        self.response_output.setText(str(response_text))
        


if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    # Run the application loop
    sys.exit(app.exec_())
