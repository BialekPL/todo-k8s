from flask import Flask, jsonify, render_template, request, redirect, url_for
import socket
import pyodbc
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler, AzureEventHandler
from credentials import db_password, db_username, db_server, db_name, ai_connection_string


app = Flask(__name__)
driver= '{ODBC Driver 18 for SQL Server}'
connection_string = f'DRIVER={driver};SERVER={db_server};PORT=1433;DATABASE={db_name};UID={db_username};PWD={db_password};Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;'
logger = logging.getLogger(__name__)
logger.addHandler(AzureEventHandler(connection_string=ai_connection_string))


def fetch_host_details():
  hostname = socket.gethostname()
  host_ip = socket.gethostbyname(hostname)
  return str(hostname), str(host_ip)

@app.route("/")
def index():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM Tasks")
        tasks = cursor.fetchall()
        """Generate random log data."""
        for num in range(1,4):
            logger.warning(f"Log Entry - {num}")
    return render_template("todo.html", tasks=tasks)


@app.route("/create_task", methods = ['POST'])
def create_task():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Tasks (Name) VALUES ('{request.form['name']}');")
        cursor.execute("SELECT id, name FROM Tasks")
        tasks = cursor.fetchall()
    return render_template("todo.html", tasks=tasks)

@app.route("/delete_task", methods = ['POST'])
def delete_task():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Tasks WHERE Id = '{request.form['id']}';")
    return redirect(url_for('index'))

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    hostname, ip = fetch_host_details()
    return render_template("details.html", HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
