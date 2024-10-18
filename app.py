from flask import Flask, render_template, request, redirect, url_for
import datetime
import random
import os
import json

app = Flask(__name__)

# Load saved module names
if os.path.exists('modules.json'):
    with open('modules.json', 'r') as f:
        modules = json.load(f)
else:
    modules = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        module_name = request.form['module_name']
        if module_name not in modules:
            modules.append(module_name)
            with open('modules.json', 'w') as f:
                json.dump(modules, f)

        date_today = datetime.date.today().strftime("%B %d, %Y")
        attendance_code = ''.join([str(random.randint(0, 9)) for _ in range(8)])

        return render_template('attendance.html',
                               module_name=module_name,
                               date_today=date_today,
                               attendance_code=attendance_code,
                               modules=modules)
    return render_template('index.html', modules=modules)

if __name__ == '__main__':
    app.run(debug=True)
