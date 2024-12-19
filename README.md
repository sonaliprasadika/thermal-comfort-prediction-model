# IoT 2024
# Thermal Comfort Prediction Model for a Bio Sauna
# Group information
* Student 1: [Sonali Prasadika](https://github.com/sonaliprasadika)
* Student 2: [Alexis Chambers](https://github.com/apchamb2)
* Student 3: [Piyumi Weebadu Arachchige](https://github.com/PiyumiUoR)
* Student 4: Emilia Pyyny-Polat

For this project, humidity, temperature, and pressure data were collected, processed, and visualized to predict the comfort of a bio sauna. A traditional Finnish sauna has temperatures from 80-100◦C and humidity of 10-20%. A bio sauna differs from a traditional Finnish sauna in its lower temperature range of 50-60◦C and higher humidity levels of up to 50%. 

## 🔗 Dependencies and Setup

The following tools and libraries are required for setting up the project. 
### 1. Install Python version 3.x

- [x]  Install latest python version from [here.](https://www.python.org) 3.10.12 is recommended 
- [x]  Install pip from [here.](https://pip.pypa.io/en/stable/installation/) 24.3.1 is recommended.
Note: pip will be available as a part of your python installation. you can check the pip version for verifying.
```bash
pip --version
```
### 2. Install the follwoing libs to run Machine Learning Model
- ☑️ everywhereml==0.1.4
- ☑️ numpy==1.22.0
- ☑️ pandas==1.5.3
- ☑️ scikit-learn==1.2.0
- ☑️ matplotlib==3.6.0
- ☑️ joblib==1.2.0

## 🔗 Run the Machine Learning Model and Evaluation
### 1. Run ML Model inside the model directory
```bash
cd models
```
```bash
python ml_model.py 
```
### 2. Run files for each evaluation inside the evaluation directory
Ex: Get the Classification Report
```bash
cd evaluation
```
```bash
python classification-report.py 
```

## 🔗 Connection to the MQTT broker

Adding the properties to the [config.py](pico-code/config.py) should establish connectivity between clients and the broker. In HiveMQ broker, the broker details are under the `OVERVIEW` tab. The `MQTT_USER` and the `MQTT_PWD` are the web client details entered under the `WEB CLIENT` to connect the clients to the server. 

´´´python
MQTT_BROKER = '' # broker/server URL
MQTT_PORT= 8883
MQTT_USER = ''  # access username
MQTT_PWD = '' # access password
´´´






