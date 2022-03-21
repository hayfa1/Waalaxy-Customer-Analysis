"""
this file contains different functions to add new features

 to the dataset that will be useful in the analysis. 


"""
from re import search

#Function to to categorize the origins i.e. Blog, default, link, prospectin...
def origin_categories(data):
    new_origin=[]
    origin=data['origin'].str.lower()
    # New origin 
    for i in range(0,len(data['origin'])):
        if(origin[i]=="unknown"):
            new_origin.append("unknown")
        elif (origin[i]=="default"):
            new_origin.append("default")
        elif search("ads", str(origin[i])):
            new_origin.append("ads")
        elif search("blog", str(origin[i])):
            new_origin.append("blog")
        elif search("prospectin", str(origin[i])):
            new_origin.append("prospectin")
        elif search("Lead Magnet", str(origin[i])):
            new_origin.append("Lead Magnet")
        elif search("Linkedin", str(origin[i])):
            new_origin.append("LinkedIn")
        elif search("link", str(origin[i])):
            new_origin.append("Link")
        elif search("marquefr", str(origin[i])):
            new_origin.append("marquefr")
        elif search("momo", str(origin[i])):
            new_origin.append("momo")
        elif search("duhirel", str(origin[i])):
            new_origin.append("duhirel")
        elif search("tgautron", str(origin[i])):
            new_origin.append("tgautron")
        elif search("leadmagneten", str(origin[i])):
            new_origin.append("leadmagneten")
        elif search("salesbytech", str(origin[i])):
            new_origin.append("salesbytech")
        else:
            new_origin.append("Others")
    return (new_origin)

#Function to extract Product type (Advanced,Pro, Business) from product column
def product_type(data):
    waalaxy_cat=[]
    origin=data['product'].str.lower()
    # New origin 
    for i in range(0,len(data['product'])):
        if search("pro", str(origin[i])):
            waalaxy_cat.append("Pro")
        elif search("advanced", str(origin[i])):
            waalaxy_cat.append("Advanced")
        elif search("business", str(origin[i])):
            waalaxy_cat.append("Business")
        else:
            print("error")
    return (waalaxy_cat)

#Function to create intervals for news staffCount:
def staff_intervals(data):
    new_staff_count=[]
    #New staffCount
    for i in range(0,len(data['staffCount'])):
        if data['staffCount'][i]<=10:
            new_staff_count.append("[0-10]")
        elif data['staffCount'][i]<=50:
            new_staff_count.append("[10-50]")
        elif data['staffCount'][i]<=100:
            new_staff_count.append("[50-100]")
        elif data['staffCount'][i]<=500:
            new_staff_count.append("[100-500]")
        elif data['staffCount'][i]<=1000:
            new_staff_count.append("[500-1000]")
        else:
            new_staff_count.append(">1000")
    return(new_staff_count)


