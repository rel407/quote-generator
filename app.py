import sqlite3
import random
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_quote():
    # Connect to database
    conn = sqlite3.connect('quotes-proj.db')
    c = conn.cursor()
    
    # Query or select a random quote and corresponding author
    c.execute('''
        SELECT q.quote, a.author
        FROM quotes q
        JOIN authors a ON q.author_id = a.author_id
        ORDER BY RANDOM()
        LIMIT 1          
    ''')
    
    quote = c.fetchone()
    conn.close()
    
    if quote:
        return {"quote": quote[0], "author": quote[1]}
    else:
        return {"quote": "No quotes available", "author": "Unknown"}
    
@app.route('/random_quote', methods=['GET'])
def random_quote():
    quote_data = get_quote()
    return jsonify(quote_data)

if __name__ == '__main__':
    app.run(debug=True)