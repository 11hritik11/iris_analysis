# Iris Analysis Project

## Overview
This project is focused on analyzing the Iris dataset, a popular dataset in machine learning and statistics. It includes data visualization, model training, and prediction functionalities.

## Features
- **Data Preprocessing**: The dataset is preprocessed using `pandas` and `LabelEncoder`.
- **Model Training**: A logistic regression model is trained using `scikit-learn`.
- **Prediction**: The trained model predicts the species of Iris flowers based on user input.
- **Visualization**: Interactive visualization using `streamlit`.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run appsss.py
   ```
2. Adjust the sliders for Sepal Length, Sepal Width, Petal Length, and Petal Width.
3. Click the "Predict" button to get the predicted species.

## Dependencies
- Python >= 3.13
- `matplotlib`
- `numpy`
- `pandas`
- `scikit-learn`
- `streamlit`

## Files
- `appsss.py`: Streamlit application for visualization and prediction.
- `main.py`: Entry point for the project.
- `irisdataset.pkl`: Serialized logistic regression model.
- `irisdatset.ipynb`: Jupyter notebook for data analysis and model training.

## License
This project is licensed under the MIT License.