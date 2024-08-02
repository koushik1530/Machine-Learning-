import numpy as np
import os
import tensorflow as tf
from PIL import Image
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
model =  tf.keras.models.load_model("model.h5")

@app. route( '/' )
def index():
    return render_template("index.html")


@app. route( '/predict', methods =['GET','POST'] )
def output():
    if request.method =='POST':
        f=request.files['pc_image']
        img_path = "static/uploads/" + f.filename
        f.save(img_path)
        img=load_img(img_path,target_size=(224,224))
        # Resize the image to the required size
        # Convert the image to an array and normalize it
        image_array = np.array(img)
        # Add a batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        # Use the pre-trained model to make a prediction
        pred=np.argmax(model.predict(image_array),axis=1)
        index=['Coccidiosis', 'Healthy' , 'New Castle Disease', 'Salmonella']
        prediction = index[int(pred)]
        print("prediction")
        #predict = prediction
        return render_template("contact.html", predict = prediction)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    