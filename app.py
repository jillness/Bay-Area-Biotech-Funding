from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template('index.html') #"Render Dashboard!"

@app.route("/")
def presentation():
    return render_template('presentation.html') #"Render Presentation page!"

@app.route("/")
def tables():
    return render_template('tables.html') #"Render Tables page!"

if __name__ == "__main__":
    app.run(debug=True)