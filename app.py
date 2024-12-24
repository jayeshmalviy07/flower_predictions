import os
from flask import Flask,request,render_template
import joblib
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import io
import base64
from sklearn.tree import DecisionTreeClassifier

app=Flask(__name__)

model=joblib.load('model.pkl')
iris=load_iris()

def generate_plot():
    data=pd.DataFrame(data=iris.data,columns=iris.feature_names)
    data['target']=iris.target
    
    fig,ax=plt.subplots()
    scatter=ax.scatter(data['sepal length (cm)'],data['sepal width (cm)'],c=data['target'],cmap='viridis')
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.set_title('Sepal Dimensions')
    
    fig.colorbar(scatter)
    
    img_io=io.BytesIO()
    plt.savefig(img_io,format='png')
    img_io.seek(0)
    img_str=base64.b64encode(img_io.getvalue()).decode('utf-8')
    plt.close(fig)
    
    return img_str

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
    
        features=pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],columns=iris.feature_names)

        prediction_index=model.predict(features)[0]
        prediction_name=load_iris().target_names[prediction_index]

        plot_img=generate_plot()
        return render_template('index.html',prediction=f"The predicted class is: {prediction_name}",plot_img=plot_img)

    except Exception as e:
        return render_template('index.html',error=f"Error:{str(e)}")
    
if __name__=='__main__':
    app.run(debug=True)    