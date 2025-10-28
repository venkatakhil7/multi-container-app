from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='root',
            password='password',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        result = cursor.fetchone()
        return result[0] if result else "No message found"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
