# Simple todo app
## Stack: Python (flask), Kubernetes, Azure SQL

The goal is to create a functioning todo app in a microservice manner so the front and back end can be scaled separatly.

Concept:
- Python app as front end (Flask probably)
- Python app as API between front and db (Flask, maybe switch to FastAPI later if Ill be able to test performance)
- Azure SQL database (columns: id of task, title, isDone)
### Chapter-1: Creating simple flask app and dockerizing it

### Chapter-2: Creating Kubernetes files

### Chapter-3: Connecting to database

You need to create a secret containing your database credentials like this:
