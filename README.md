# Waalaxy-Customer-Analysis
The goal of this repository  is to prepare Waalaxy's historical customer data to create dashboards to exploit
this data and extract useful information and insights. This will help Waalaxy to have a global view on customer
behavior and subsequently target their customers and improve the customer journey.

This repository contains two main files:
data_preprocessing.py This file contains a python script for data cleaning and processing. 
The input of this script is the historical customer data collected by Waalaxy and the
output will be a file that contains the cleaned data with new columns that will be useful for analysis.

Clustering.py  contains a python script for clustering data. The file will take the output of
the DataProcessing.py as an input and returns a new dataset for the analysis later.
This will allow Waalaxy to divide their customers into groups or 'clusters' that reflect similarity amongst customers.


system info:

- python 3.8.3

- windows 10

## Installing
use virtual environment python: 
```bash
python -m venv yourvenv
```
Activate virtual environment:
```bash
yourvenv\Scripts\activate
```
update pip:
```bash
pip install --upgrade pip
```
install requirements:
```bash
pip install -r requirements.txt
```



## usage

```bash
python DataProcessing.py -source inputfile - destination outputfile
```

```bash
python Clustering.py -source inputfile -destination outputfile
```