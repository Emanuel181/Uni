from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/contact")
def contact():
    # Assuming you have a template named 'contact.html'
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
