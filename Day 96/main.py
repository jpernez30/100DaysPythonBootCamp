from flask import Flask, render_template, request, redirect, url_for
import requests
import html
import time

app = Flask(__name__)

# Function to get a random trivia question
def get_trivia():
    while True:
        response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
        data = response.json()
        if data['response_code'] == 0:
            question_data = data['results'][0]
            question = html.unescape(question_data['question'])
            correct_answer = html.unescape(question_data['correct_answer'])
            incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
            options = [correct_answer] + incorrect_answers
            return question, correct_answer, options
        else:
            time.sleep(3)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if user_answer == correct_answer:
            result = 'Correct!'
        else:
            result = f'Incorrect! The correct answer was: {correct_answer}'
        question, correct_answer, options = get_trivia()
        return render_template('index.html', question=question, correct_answer=correct_answer, options=options, result=result)

    question, correct_answer, options = get_trivia()
    return render_template('index.html', question=question, correct_answer=correct_answer, options=options)

if __name__ == '__main__':
    app.run(debug=True)