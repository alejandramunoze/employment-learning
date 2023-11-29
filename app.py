

from flask import Flask

# Create a flask application
app = Flask(__name__) # must give it a name

# Registrating a route

@app.route("/") # empty page
def home():
    return render_template('home.html') #In the function we render the formatting from html


# With the following we can use "python app.py" to get it running without having to use the "export FLASK_APP=app, flask run" command
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

