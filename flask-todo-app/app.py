from flask import Flask, render_template, request, redirect
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')


@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        logging.info(f"Task added: {task}")
    return redirect('/')


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
