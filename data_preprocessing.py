"""
this is the main file for the data preparation and preprocessing

"""

from transforming_columns import *
from occupation import *
import argparse
import pandas as pd



if __name__== "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("-source", type=argparse.FileType('r'))
    parser.add_argument('-destination', type=argparse.FileType('w', encoding='latin-1'))
    args = parser.parse_args()
    print(args.source.name)
    print(args.destination.name)
    #Import the dataset
    data= pd.read_csv(args.source.name,delimiter=";")
    print("Sum of null values per column:")
    print(data.isnull().sum())

    #Supprimer les ponctuations et les emojis de la colonne occupation
    data['occupation'] = data['occupation'].str.replace('[^\w\s]','')
   
    #Add new column for origins categories
    new_origin=origin_categories(data)
    data['New origin']=new_origin

    #Add new colum for product type
    product_t=product_type(data)
    data['Product Type']=product_t

    #Add new column for staffCount Intervals
    new_staff_count=staff_intervals(data)
    data['New staffCount']=new_staff_count


    #Translate Occupation To English
    occupT=translator_two(data)
    data['Occupation EN']=occupT

    #Create a new Column for job titles 
    jobT=job_titles(data)
    data['JobTitle']=jobT

    #Grouping similar jobs but with different titles in the same job title
    group_jobs(data)

    #export the new data in a csv file
    data.to_csv(args.destination.name)

    

