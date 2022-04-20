from flask import Flask
app = Flask('first-app')

@app.route('/')
def index():
   return 'Hello World!'


app.run()