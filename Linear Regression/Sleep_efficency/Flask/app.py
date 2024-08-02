import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, render_template
app = Flask(__name__)
model = pickle.load(open('best_model.pkl', 'rb'))

@app.route('/') # rendering the html template
def index():
    return render_template('index.html')
@app.route('/predict') # rendering the html template
def innerpage():
    return render_template('portfolio-details.html')



@app.route('/submit', methods=["POST"])
def submit():


    Age=int(request.form["Age"])
    Gender = int(request.form["Gender"])
    Sleep_Duration = int(request.form["Sleep Duration"])
    Rem_sleep_percentage = int(request.form["REM sleep percentage"])
    Deep_sleep_percentage = int(request.form["Deep sleep percentage"])
    Light_sleep_percentage = int(request.form["Light sleep percentage"])
    Awakenings = float(request.form["Awakenings"])
    Caffeine_consumption = float(request.form["Caffeine consumption"])
    Alcohol_consumption = float(request.form["Alcohol consumption"])
    Smoking_status = float(request.form["Smoking status"])
    Exercise_frequency = float(request.form["Exercise frequency"]) 






    X =np.array ([[Age,Gender,Sleep_Duration,Rem_sleep_percentage,Deep_sleep_percentage,Light_sleep_percentage,Awakenings,Caffeine_consumption,Alcohol_consumption,Smoking_status,Exercise_frequency]])
    prediction = model.predict(X)
    result = str(round (prediction[0] ,2))
    return render_template("blog.html", predict=result)



  
if __name__=="__main__":
     app.run( debug=True, port = 5000)    # running the app