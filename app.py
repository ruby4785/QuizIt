from flask import Flask, render_template

app = Flask(__name__)

quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['London', 'Paris', 'Berlin', 'Rome'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'choices': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    # Add more questions here
]

@app.route('/')
def index():
    return render_template('index.html', questions=quiz_questions)

if __name__ == '__main__':
    app.run(debug=True)