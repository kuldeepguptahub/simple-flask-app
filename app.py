from flask import Flask, render_template
import pymongo
from dotenv import load_dotenv
import os

# Setup MongoDB connection
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")
client = pymongo.MongoClient(mongo_uri)
db = client.get_database('mydatabase')
collection = db.get_collection('mycollection')

# Initialize Flask app
app = Flask(__name__)
@app.route('/api')
def home():
    with open('data.json') as file:
        data = file.read()
    return data

@app.route('/', methods=['GET', 'POST'])
def query_form():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)