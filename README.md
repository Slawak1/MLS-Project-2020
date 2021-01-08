# Data Representation Project

### GMIT - Higher Diploma in Computing and Data Analytics.
### Author : Slawomir Sowa
### Email : G00376519@gmit.ie
---

This repository contains all the files for Machine Learning and Statistics Project, 2020. 

### The repository contains the following files:

* ML_server.py - Flask server application 
* requirements.txt - text file with python packages required to run the app
* static - folder contains html pages, CSS, img folder and .dockerignore file. 
* .gitignore - GitHub gitignore file
* MLS_Project_2020.ipynb - Jupyter Notebook file, contains that trains a models using in the dataset.
* powerproduction.csv - data set
* model - folder contains trained models and exported to .pkl files

### Instruction

1. Clone repository: https://github.com/Slawak1/Data-Representation-Project
2. Create and activate blank virtual environment with a directory named <code>venv</code>
3. Run code <code> pip install -r requirements.txt</code> to install required Python packages
4. Run Flas server (On Windows):
* <code>SET FLASK_APP=server</code>
* <code>SET FLASK_ENV=development</code>
* <code>flask run</code>
5. Open http://127.0.0.1:5000/ in web browser

### Errors:
1. Docker Error - 
> [4/5] RUN pip install --no-cache-dir -r requirements.txt:<br>
#8 4.333 ERROR: Could not find a version that satisfies the requirement pywin32==227<br>
#8 4.333 ERROR: No matching distribution found for pywin32==227<br>
------<br>
executor failed running [/bin/sh -c pip install --no-cache-dir -r requirements.txt]: exit code: 1<br>
