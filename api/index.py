from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, niggers!'


@app.route('/input')
def about():
    # render an html page
    return """
        <!DOCTYPE html>
<html>
<head>
    <title>Input Box Example</title>
</head>
<body>
    <input type="text" placeholder="Enter your text here">
</body>
</html>
    """