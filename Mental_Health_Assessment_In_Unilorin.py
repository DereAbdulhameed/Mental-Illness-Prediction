#!/usr/bin/env python
# coding: utf-8

# Import the necessary libraries
# 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.impute import SimpleImputer
import streamlit as st


import pickle
from PIL import Image

model = pickle.load(open('finalized_model.sav', 'rb'))

image = Image.open('index.png')
st.image(image, '')

st.write("""

#   Mental Health Diagnostic App
    """)
    
    
st.sidebar.header('Biodata')



Year_List = [100,200,300,400,500,600]
age_list = [16-20, 21-24, 25-30, 30]
sleep_hours = [4,5,6,7,8,9,10]
a = 'rarely'
b = 'always'

def user_input_features():
    
    level_class = st.sidebar.selectbox('Kindly select your level', Year_List, 0)
    age = st.sidebar.text_input('Please fill in your age appropriately', 16)
    family = st.sidebar.selectbox('Are your parents separated?', [0, 1], 0)
    experience = st.sidebar.selectbox('Which level have you had the toughest experience of your medical training?', Year_List, 0)
    financial = st.sidebar.selectbox('Do you have a good support system that you can fall back on during financial crisis?', [0, 1])
    emotional = st.sidebar.selectbox('Do you have a good support system that you can fall back on during emotional crisis?', [0, 1])
    sleep = st.slider('On an average, how many hours do you sleep daily??',4,10)
    esteem = st.slider('In a range of 1-5, how much has medical training negatively affected your self esteem?', 0,5)
    isolation = st.slider('Do you experience social isolation, withdrawal from friends and loneliness often?',0,5)
    concentration = st.slider('Do you have reduced ability to concentrate for over a short period?', 0,5)
    assessment = st.slider('How do you describe your assessment in medical school?',0,5)
    burnout = st.slider('Do you frequently experience burnout, anxiety and depression especially when exams are getting closer?', 0,5)
    history = st.selectbox('Is there a history of mental illness in a blood relative, such as a parent or sibling?',[0,1],0)
    extracurricular = st.selectbox('Medicine apart, do you have any extracurricular activities you engage in?',[0,1],0)
    suicide = st.selectbox('Have you ever had suicidal thoughts before?',[0,1],0)

    
    
    data = {'level_class': level_class,
            'Age': age,
            'family': family,
            'experience':experience,
            'financial': financial,
            'emotional': emotional,
            'sleep': sleep,
            'esteem': esteem,
            'isolation': isolation,
            'concentration': concentration,
            'assessment': assessment,
            'burnout': burnout,
            'extracurricular': extracurricular,
            'suicide': suicide
        
        }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
    
st.subheader('Tell me about yourself, let us make a diagnosis!' )




st.subheader('Diagnosis')
diagnosis = model.predict(df)
#Note, you need to include all the features in df to be able to use the pickled nodek to predict.





