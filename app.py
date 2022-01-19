from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('crop.html', title=title)

@ app.route('/fertilizer')
def fertilizer_recommendation():
    title = 'Harvestify - Fertilizer Suggestion'
    return render_template('fertilizer.html', title=title)

@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Harvestify - Disease Detection'
    return render_template('disease.html', title=title)

if __name__ == "__main__":
    app.run(debug=True,port=8000)