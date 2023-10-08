import pickle
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = tf.keras.models.load_model(r'C:\Users\Guide Info\Downloads\DSTI\training\model.skl')

@app.route('/')
def home():
    return render_template('template_1.html')

@app.route(r'/predict',methods=['POST'])
def predict():

    """int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)"""

    # Retrieve input values from the form
    language_code = request.form['language_code']
    num_pages = float(request.form['num_pages'])
    ratings_count = float(request.form['ratings_count'])
    text_reviews_count = float(request.form['text_reviews_count'])
    publication_day = float(request.form['publication_day'])
    publication_month = float(request.form['publication_month'])
    publication_year = float(request.form['publication_year'])
    publisher = request.form['publisher']

    # Convert and preprocess the inputs as needed (e.g., encoding, scaling)
    # Load the saved label encoders
    with open('language_encoder.pkl', 'rb') as le_file:
        language_encoder = pickle.load(le_file)

    with open('publisher_encoder.pkl', 'rb') as le_file:
        publisher_encoder = pickle.load(le_file)

    language_code =  language_encoder.fit_transform([language_code])
    publisher =  publisher_encoder.fit_transform([publisher])

    #Normalize and standardize data
    stand_scaler = StandardScaler()
    norm_scaler = MinMaxScaler()
    """
    language_code = norm_scaler.fit_transform(language_code)
    language_code = stand_scaler.fit_transform(language_code)

    num_pages = norm_scaler.fit_transform(num_pages)
    num_pages = stand_scaler.fit_transform(num_pages)

    ratings_count = norm_scaler.fit_transform(ratings_count)
    ratings_count = stand_scaler.fit_transform(ratings_count)

    text_reviews_count = norm_scaler.fit_transform(text_reviews_count)
    text_reviews_count = stand_scaler.fit_transform(text_reviews_count)

    publication_day = norm_scaler.fit_transform(publication_day)
    publication_day = stand_scaler.fit_transform(publication_day)

    publication_month = norm_scaler.fit_transform(publication_month)
    publication_month = stand_scaler.fit_transform(publication_month)
    
    publication_year = norm_scaler.fit_transform(publication_year)
    publication_year = stand_scaler.fit_transform(publication_year)

    publisher = norm_scaler.fit_transform(publisher)
    publisher = stand_scaler.fit_transform(publisher)
    """

    # Create a feature vector using the input values
    features = [language_code, [num_pages], [ratings_count], [text_reviews_count], [publication_day], [publication_month], [publication_year], publisher]
    features = np.array(features)
    features = features.reshape([-1,8])
    print(features.shape)
    features = norm_scaler.fit_transform(features)
    features = stand_scaler.fit_transform(features)
    # Make predictions using your model
    prediction = model.predict([features])  # Assuming "model" is your trained ML model


    output = prediction[0]

    return render_template('template_1.html', prediction_text='Average Rate = {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)