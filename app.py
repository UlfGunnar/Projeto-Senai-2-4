from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('Login.html')

@app.route('/registrar')
def register_page():
    return render_template('Register.html')

if __name__ == '__main__':
    app.run(debug=True)