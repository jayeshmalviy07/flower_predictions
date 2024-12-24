# Flower Prediction Flask App 🌸

This project is a simple machine learning-powered Flask application that predicts the species of an iris flower based on user-provided dimensions of sepal and petal. The application uses the Iris dataset and a pre-trained Decision Tree model to make predictions. Additionally, it visualizes the dataset using Matplotlib.

## Features ✨

- Predicts the flower species (Setosa, Versicolor, Virginica) based on sepal and petal dimensions.
- Interactive web interface for input.
- Visual representation of sepal dimensions and flower classification.
- Built with Flask, Scikit-learn, and Matplotlib.

## Installation 🛠️

### Prerequisites

- Python 3.8+
- Flask
- Scikit-learn
- Matplotlib
- Joblib
- Git (to clone the repository)

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:jayeshmalviy07/flower_predictions.git
   cd flower_predictions```
   
2. Create and activate a virtual environment (optional but recommended):
   ```bash
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate```

3. Install the required dependencies:
   ```
    bash
    pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```
    bash
    python app.py

4. Open the app in your browser:
   ```
    http://127.0.0.1:5000/
   ```
## Usage 📋
- Enter the dimensions of the sepal and petal (length and width) in the input form.
- Click the Predict button.
- View the predicted flower species and the visualized data.

##Project Structure 🗂️
```
flower_predictions/
│
├── app.py                 # Flask application
├── model.pkl              # Pre-trained Decision Tree model
├── Task1.ipynb            # Jupyter Notebook for model training and visualization
├── templates/
│   └── index.html         # HTML file for the web interface
├── static/                # (Optional) For static files like images, CSS
└── README.md              # Project documentation (this file)
```
## Visualization 🌐
The application generates a scatter plot to visualize sepal dimensions and classify the dataset. The plot is dynamically displayed on the web interface.

## Dataset 📊
The app uses the Iris dataset, which contains measurements for sepal length, sepal width, petal length, and petal width for three species of iris flowers:

- Setosa
- Versicolor
- Virginica

## Future Improvements 🚀
- Add support for other datasets or flower species.
- Enhance the UI with better styling.
- Deploy the application on a cloud platform like AWS, Heroku, or Render.
- Include more visualizations for petal dimensions.

## License 📜
- This project is licensed under the MIT License.

## Contributors 🤝
Jayesh Kumar Malviya (Project Owner)  
Feel free to contribute to this project by opening issues or submitting pull requests.

## Deployment 🌍
This app can be deployed to platforms like:

- Heroku
- AWS Elastic Beanstalk
- Render
