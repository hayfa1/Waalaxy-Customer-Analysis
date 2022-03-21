"""
This file contains functions to translate the values of occupations 

from different languages into English and to extract the job titles.


"""
from roles import role_words
from tqdm import tqdm
import re
import pandas as pd
from textblob import TextBlob
from googletrans import Translator, constants
import string
from re import search




#Function to translate Occupation from the language in language column to english using text blob library
def translator_one(data):
    occup=list(data['occupation'])
    occup_trans=[]
    for i in range(0, len(occup)):
        lg=data['language'][i]
        try:
            blob= TextBlob(str(occup[i]))
            tra=blob.translate(from_lang=lg,to='en')
            occup_trans.append(str(tra))
        except:
            occup_trans.append(occup[i])
            #print(occup[i])
    return (occup_trans)

#Function to translate Occupation from the language in language column to english using Googletrans library
def translator_two(data):
    occup=list(data['occupation'])
    occup_trans=[]
    print("The translation is in progress, please wait")
    for i in tqdm(range(0, len(occup))):
        lg=data['language'][i]
        try:
            translator = Translator()
            translation = translator.translate(occup[i], src=lg)
            occup_trans.append(translation.text)
        except:
            occup_trans.append(occup[i])
            #print(occup[i])
    return (occup_trans)


#Functions to change occupations to general job titles 
def find_maximal_roles(title):
    role_word_re = r'\b(?:' + '|'.join(role_words) + r')\b'
    preceding_word = r'(?:\b[\w\d]+\s+)'
    role_term_re = re.compile(preceding_word + '{0,4}' + role_word_re)
    return role_term_re.findall(title)

def job_titles(data):
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
def group_jobs(df):
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
