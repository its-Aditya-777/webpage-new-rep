#flask
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import os

app = Flask(__name__)
DATA_FILE = 'students.csv'

# Ensure the CSV file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Roll Number', 'Phone Number', 'Cumulative GPA'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        phone_number = request.form['phone_number']
        gpa = request.form['gpa']
        with open(DATA_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, roll_number, phone_number, gpa])
        return redirect(url_for('home'))
    return render_template('add_student.html')

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    students = []
    if request.method == 'POST':
        query = request.form['query']
        with open(DATA_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if query.lower() in row['Name'].lower() or query == row['Roll Number']:
                    students.append(row)
    return render_template('search_student.html', students=students)

#changing port from (5000 to 8000).
if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

#create two directories static and template.

#final-> Deployment of app(webpage) on Heroku.