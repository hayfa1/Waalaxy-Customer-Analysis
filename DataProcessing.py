#Importing libraries
from googletrans import Translator, constants
from pprint import pprint
from langdetect import detect
from textblob import TextBlob
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
import string
from re import search
from googletrans import Translator, constants
from pprint import pprint
import re
from tqdm import tqdm
import argparse
from roles import role_words


#Function to to categorize the origins i.e. Blog, default, link, prospectin...
def OriginCategories(data):
    newOrigin=[]
    origin=data['origin'].str.lower()
    # New origin 
    for i in range(0,len(data['origin'])):
        if(origin[i]=="unknown"):
            newOrigin.append("unknown")
        elif (origin[i]=="default"):
            newOrigin.append("default")
        elif search("ads", str(origin[i])):
            newOrigin.append("ads")
        elif search("blog", str(origin[i])):
            newOrigin.append("blog")
        elif search("prospectin", str(origin[i])):
            newOrigin.append("prospectin")
        elif search("Lead Magnet", str(origin[i])):
            newOrigin.append("Lead Magnet")
        elif search("Linkedin", str(origin[i])):
            newOrigin.append("LinkedIn")
        elif search("link", str(origin[i])):
            newOrigin.append("Link")
        elif search("marquefr", str(origin[i])):
            newOrigin.append("marquefr")
        elif search("momo", str(origin[i])):
            newOrigin.append("momo")
        elif search("duhirel", str(origin[i])):
            newOrigin.append("duhirel")
        elif search("tgautron", str(origin[i])):
            newOrigin.append("tgautron")
        elif search("leadmagneten", str(origin[i])):
            newOrigin.append("leadmagneten")
        elif search("salesbytech", str(origin[i])):
            newOrigin.append("salesbytech")
        else:
            newOrigin.append("Others")
    return (newOrigin)

#Function to extract Product type (Advanced,Pro, Business) from product column
def ProductType(data):
    WaalaxyCat=[]
    origin=data['product'].str.lower()
    # New origin 
    for i in range(0,len(data['product'])):
        if search("pro", str(origin[i])):
            WaalaxyCat.append("Pro")
        elif search("advanced", str(origin[i])):
            WaalaxyCat.append("Advanced")
        elif search("business", str(origin[i])):
            WaalaxyCat.append("Business")
        else:
            print("error")
    return (WaalaxyCat)

#Function to create intervals for news staffCount:
def CreateIntervals(data):
    NewStaffCount=[]
    #New staffCount
    for i in range(0,len(data['staffCount'])):
        if data['staffCount'][i]<=10:
            NewStaffCount.append("[0-10]")
        elif data['staffCount'][i]<=50:
            NewStaffCount.append("[10-50]")
        elif data['staffCount'][i]<=100:
            NewStaffCount.append("[50-100]")
        elif data['staffCount'][i]<=500:
            NewStaffCount.append("[100-500]")
        elif data['staffCount'][i]<=1000:
            NewStaffCount.append("[500-1000]")
        else:
            NewStaffCount.append(">1000")
    return(NewStaffCount)


#Function to translate Occupation from the language in language column to english using text blob library
def translator1(data):
    occup=list(data['occupation'])
    OccupTrans=[]
    for i in range(0, len(occup)):
        lg=data['language'][i]
        try:
            blob= TextBlob(str(occup[i]))
            tra=blob.translate(from_lang=lg,to='en')
            OccupTrans.append(str(tra))
        except:
            OccupTrans.append(occup[i])
            #print(occup[i])
    return (OccupTrans)

#Function to translate Occupation from the language in language column to english using Googletrans library
def translator2(data):
    occup=list(data['occupation'])
    OccupTrans=[]
    print("The translation is in progress, please wait")
    for i in tqdm(range(0, len(occup))):
        lg=data['language'][i]
        try:
            translator = Translator()
            translation = translator.translate(occup[i], src=lg)
            OccupTrans.append(translation.text)
        except:
            OccupTrans.append(occup[i])
            #print(occup[i])
    return (OccupTrans)


#Functions to change occupations to general job titles 
def find_maximal_roles(title):
    role_word_re = r'\b(?:' + '|'.join(role_words) + r')\b'
    preceding_word = r'(?:\b[\w\d]+\s+)'
    role_term_re = re.compile(preceding_word + '{0,4}' + role_word_re)
    return role_term_re.findall(title)

def JobTitles(data):
    occup=list(data['Occupation EN'])
    JobTitle=[]
    for i in range(0, len(occup)):
        a=find_maximal_roles(str(occup[i]).lower())
        if a:
            JobTitle.append(a[0])
        else:
            JobTitle.append(occup[i])
            #print(occup[i])
    return JobTitle

#Function to group similar jobs but with different titles in the same job title
def GroupJobs(df):
    substring_list=['founder','fondatrice','ceoowner','cofounderowner','fondateur','owner']
    substring_list2=['human resources','talent hunter', 'recruitment','recrutement,' 'head of human resources', 'recruiter','hr ', 'talent scout','talent','recruting']
    substring_list3=['ceo','chief executive officer']
    substring_list4=['manager','management','managing','gérant','gerant']
    substring_list5=['director','directeur','directrice']
    substring_list6=['engineer','web developer','developer','ingénieur']
    substring_list7=['consultant','consulting']
    substring_list8=['business developer','business development']
    substring_list9=['master','student','alternant','studing','internship']
    substring_list10=['entrepreneur','contractor']
    substring_list11=['head of customer','head of client']

    for i in range(0, len(df['JobTitle'])):
        a=0
        try:
            if any(substring in df['JobTitle'][i].lower() for substring in substring_list):
                df['JobTitle'][i]="Founder"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list2):
                df['JobTitle'][i]="Recruiter"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list3):
                df['JobTitle'][i]="CEO"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list4):
                df['JobTitle'][i]="Manager"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list5):
                df['JobTitle'][i]="Director"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list6):
                df['JobTitle'][i]="Engineer"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list7):
                df['JobTitle'][i]="Consultant"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list8):
                df['JobTitle'][i]="Business Developer"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list9):
                df['JobTitle'][i]="Student"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list10):
                df['JobTitle'][i]="Contractor"
            elif any(substring in df['JobTitle'][i].lower() for substring in substring_list11):
                df['JobTitle'][i]="Head of Customer"
            elif 'marketing' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Marketing Specialist"
            elif 'coach' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Coach"
            elif 'coach' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Coach"
            elif 'independent' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Independent"   
            elif 'president' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="President"  
            elif 'lead' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Leader" 
            elif 'commercial' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Commercial"
            elif 'cmo' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="CMO"
            elif 'growth' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Growth Manager"
            elif 'train' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Trainer"
            elif 'designer' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="designer"
            elif 'copywriter' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Copywriter"
            elif 'head of sales' in df['JobTitle'][i].lower():
                df['JobTitle'][i]="Head of Sales"
        except:
            a=1

#Main
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
    newOrigin=OriginCategories(data)
    data['New origin']=newOrigin

    #Add new colum for product type
    productType=ProductType(data)
    data['Product Type']=productType

    #Add new column for staffCount Intervals
    NewStaffCount=CreateIntervals(data)
    data['New staffCount']=NewStaffCount

    #Translate Occupation To English
    OccupTrans=translator2(data)
    data['Occupation EN']=OccupTrans

    #Create a new Column for job titles 
    JobTitle=JobTitles(data)
    data['JobTitle']=JobTitle

    #Grouping similar jobs but with different titles in the same job title
    GroupJobs(data)

    #export the new data in a csv file
    data.to_csv(args.destination.name)

    




