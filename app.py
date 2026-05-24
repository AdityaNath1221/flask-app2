from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
    <head>
        <title>DevOps Demo</title>

        <style>
            body {{
                background: #F6F4F3;
                color: #161925;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }}

            h1 {{
                font-size: 60px;
                color: #38bdf8;
            }}

            p {{
                font-size: 24px;
            }}

            button {{
                padding: 15px 30px;
                font-size: 20px;
                border: none;
                border-radius: 10px;
                background: #38bdf8;
                cursor: pointer;
            }}
        </style>
    </head>

    <body>
        <h1>🚀 Flask app CI/CD Pipeline</h1>

        <p>Deployment Successful</p>

        <p>Time: {datetime.now()}</p>

        <button onclick="sayHello()">Click Me</button>

        <script>
            function sayHello() {{
                alert("Hello World");
            }}
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)