from flask import Flask, request


app = Flask(__name__)
@app.route('/api')
def home():
    with open('data.json') as file:
        data = file.read()
    return data

@app.route('/submit_data', methods=['GET', 'POST'])
def query_form():
    if request.method == 'POST':
        # Handle form submission
        return "Data submitted successfully!"
    return "Please submit the form."

if __name__ == '__main__':
    app.run(debug=True)