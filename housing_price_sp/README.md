# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## To excute the script
-  ``` conda env create -f env.yml ``` to create the environment from env.yml file
-	 ``` conda activate env.yml``` to activate the environment

This code has python files refactored as scripts and are able to install as a package.
All the python scripts are available at ```src/housing_price```.
This folder contains ```datasets``` which has the required datsets along with train and test datasets as csv files.

```housing_price``` folder is refactored to a package so it contains ```__init__.py```.

This package also contains ```tests``` folder which has some functional and unit tests for this project.
