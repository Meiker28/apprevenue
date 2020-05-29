import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
df = pd.read_csv('Prediccsiones.csv')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = round(np.random.rand(), 2)*100
    output = round(df.loc[df.CALUMNO ==int_features[0],'PREDICHO'].values[0],3)

    return render_template('index.html', prediction_text='Descuento del estudiante es {}%'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)

#int_features = 1369260

#output = round(df.loc[df.CALUMNO ==int_features,'PREDICHO'].values[0],3)
