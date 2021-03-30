import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
import pandas as pd

app=Flask(__name__)

df=pd.read_csv('sehat.csv')
df.set_index('DESCRIPTION',inplace=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    initial_features=request.form['bc'].lower()
    
    a=df.loc[initial_features].Minimum
    b=df.loc[initial_features].Maximum
    c=df.loc[initial_features].Mean
    return render_template('index.html',prediction_text='Your range wil be from {}$ to {}$'.format(a,b))
        
if __name__=='__main__':
    app.run(debug=True)
    