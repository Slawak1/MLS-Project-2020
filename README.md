# Machine Learning and Statistics Project, 2020.

### GMIT - Higher Diploma in Computing and Data Analytics.
### Author : Slawomir Sowa
### Email : G00376519@gmit.ie
---

This repository contains all the files for Machine Learning and Statistics Project, 2020. 

### Subject 

In this project you must create a web service that uses machine learning to make predictions based on the data set powerproduction.csv. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. You must then develop a web service that will respond with predicted power values based on speed values sent as HTTP requests. Your submission must be in the form of a git repository containing, at a minimum, the following items:

- Jupyter notebook that trains a model using the data set. In the notebook you should explain your model and give an analysis of its accuracy.
- Python script that runs a web service based on the model, as above.
- Dockerfile to build and run the web service in a container.
- Standard items in a git repository such as a README.

### The repository contains the following files:

* ML_server.py - Flask server application 
* requirements.txt - text file with python packages required to run the app
* static - folder contains html pages, CSS, img folder and .dockerignore file. 
* .gitignore - GitHub gitignore file
* MLS_Project_2020.ipynb - Jupyter Notebook file, contains that trains a models using in the dataset.
* powerproduction.csv - data set
* model - folder contains trained models as .pkl files
* dockerfile - file with instructions to create docker image

### Instruction

Follow these steps to run the application

1. Clone repository: https://github.com/Slawak1/MLS-Project-2020
2. Navigate to repository folder 
3. Create Docker image: <code> docker build -t ml_server . </code>
4. Run Docker image: <code> docker -d -p 5000:5000 ml_server </code>
5. Open http://127.0.0.1:5000/ in web browser
6. To stop server display list of containers: <code> docker container ls </code>
7. Copy <code>CONTAINER ID</code>
8. Use code: <code> docker kill CONTAINER ID </code> to stop server 



#### Alternatively
2. Create and activate blank virtual environment with a directory named <code>venv</code>
3. Run code <code> pip install -r requirements.txt</code> to install required Python packages
4. Run Flas server (On Windows):
* <code>SET FLASK_APP=ml_server</code>
* <code>SET FLASK_ENV=development</code>
* <code>flask run</code>
5. Open http://127.0.0.1:5000/ in web browser
6. To stop server return to console and press CTRL+C

### References

<em>[1].</em> Wind Turbine Power Calculations;  https://www.raeng.org.uk/publications/other/23-wind-turbine <br>
<em>[2].</em> The Missing Link Between Air Density And Wind Power Production; https://www.technologyreview.com/2011/03/15/196333/the-missing-link-between-air-density-and-wind-power-production/<br>
<em>[3].</em> Rooftop Wind Turbines: Are They Worthwhile? https://www.engineering.com/ElectronicsDesign/ElectronicsDesignArticles/ArticleID/9556/Rooftop-Wind-Turbines-Are-They-Worthwhile.aspx<br>
<em>[4].</em> Ways to Detect and Remove the Outliers; https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba; May 22, 2018<br>
<em>[5].</em> Understanding Q-Q Plots; https://data.library.virginia.edu/understanding-q-q-plots/<br>
<em>[6].</em> https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/<br>
<em>[7].</em> Machine Learning: Simple Linear Regression with Python; https://towardsdatascience.com/machine-learning-simple-linear-regression-with-python-f04ecfdadc13<br>
<em>[8].</em> https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/<br>
<em>[9].</em> Remove warnings from jupyter notebook; https://stackoverflow.com/a/46721064<br>
<em>[10].</em> Polynomial Regression in Python – Complete Implementation in Python;  https://www.askpython.com/python/examples/polynomial-regression-in-python<br>
<em>[11].</em> Linear Regression in Python; https://realpython.com/linear-regression-in-python/<br>
<em>[12].</em> Chapter 12 Polynomial Regression Models; http://home.iitk.ac.in/~shalab/regression/Chapter12-Regression-PolynomialRegression.pdf

