from flask import Flask, render_template, request
import pymongo
from dotenv import load_dotenv
import os

# Setup MongoDB connection
load_dotenv()
mongo_uri = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_uri)
db = client.contactsdb
collection = db.contacts

# Initialize Flask app
app = Flask(__name__)

@app.route('/api')
def home():
    with open('data.json') as file:
        data = file.read()
    return data

@app.route('/')
def contact_form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        form_data = dict(request.form)
        collection.insert_one(form_data)
        return render_template('submit.html')
    except Exception as e:
        error_message = f"Could not submit form: {str(e)}"
        return render_template('form.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True)