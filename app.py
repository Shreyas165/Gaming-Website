        
from flask import Flask,request,render_template
import subprocess
import pandas as pd
import os

app = Flask(__name__)
data_dir = 'static/data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    country = request.form.get('country')
    message = request.form.get('message')

    # Define the path to the Excel file
    excel_path = os.path.join(data_dir, 'Book1.xlsx')

    # Load existing data or create a new DataFrame
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path,engine='openpyxl')
    else:
        df = pd.DataFrame(columns=['Name', 'Email', 'Country', 'Message'])

    # Append new data
    new_row = {'Name': name, 'Email': email, 'Country': country, 'Message': message}
    df = df.append(new_row, ignore_index=True)

    # Save the DataFrame to the Excel file
    df.to_excel(excel_path, index=False, engine='openpyxl')

    return 'Form submitted successfully!'

@app.route('/run-script')
def run_script():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game3.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result
#New function to call new python script
@app.route('/run-script2')
def run_script2():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game4.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result

@app.route('/run-script3')
def run_script3():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game5.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script8')
def run_script8():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game8.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script9')
def run_script9():
    # Call your Python script here
    process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script7')
def run_script7():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game7.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result
@app.route('/run-script77')
def run_script77():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game7,1.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result

@app.route('/run-script10')
def run_script10():
    # Call your Python script here
    process = subprocess.Popen(['python', 'ggame10.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


if __name__ == '__main__':
    app.run(debug=True)