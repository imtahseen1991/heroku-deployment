"""
Creating flask application for CRUD methods
Developer: Tahseen Siddiqi
"""

# Importing the modules
from flask import Flask, jsonify, request, render_template, flash, session
from dbconnection import connection
import logging
from chatbot_prediction import prediction

cursor = connection()

# create logger for chatbot.log
chatbot_logger = logging.getLogger('chatbot')
chatbot_logger.setLevel(logging.INFO)
chatbot_file_handler = logging.FileHandler('C:/Users/imtah/Documents/ai_in_es/Final_project_chatbot/logs/chatbot.log')
chatbot_logger.addHandler(chatbot_file_handler)

# create logger for all other logs
other_logger = logging.getLogger('other')
other_logger.setLevel(logging.INFO)
other_file_handler = logging.FileHandler('C:/Users/imtah/Documents/ai_in_es/Final_project_chatbot/logs/dbconnection.log')
other_logger.addHandler(other_file_handler)

app = Flask(__name__)
app.secret_key = 'tahseen1234'


@app.route("/", methods=["GET", "POST"])
def main_page():
    input_data = ""
    if request.method == "POST":
        data = request.form.get("input", "")
        chatbot_logger.info("Question: " + data)
        pred = prediction(data)
        chatbot_logger.info("Answer: " + pred)
        flash("Chatbot says: " + pred)
        query = "INSERT INTO prediction (input, prediction) VALUES (?, ?)"
        cursor.execute(query, data, pred)
        cursor.commit()
    return render_template("login_page.html", input_value=input_data)



if __name__ == "__main__":
    app.run(debug=True, port=5001)