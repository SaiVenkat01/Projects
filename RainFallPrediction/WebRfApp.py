# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:38:08 2022

@author: saive
"""

import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

loaded_model=pickle.load(open('‪D:\Mini Project\train_model_rf.sav','rb'))

#creating a function for prediction

def rainfall_predict(input_data):
    input_data=np.asarray(input_data)
    input_data=input_data.reshape(1,-1)
    #sc1 = StandardScaler()
    #input_data = sc1.fit_transform(input_data)

    y_pred = (np.array(loaded_model.predict(input_data),dtype=int))
    if(y_pred[0]==0):
        return 'Tomorrow there will be rainfall'
    else:
        return 'Tomorrow there is no rainfall'
    



def main():
    
    #Giving a title
    st.title('Rainfall Prediction Web App')
    
    area=['Albury', 'BadgerysCreek' ,'Cobar', 'CoffsHarbour', 'Moree' ,'Newcastle',
 'NorahHead' ,'NorfolkIsland' ,'Penrith' ,'Richmond' ,'Sydney', 'SydneyAirport',
 'WaggaWagga' ,'Williamtown' ,'Wollongong', 'Canberra' ,'Tuggeranong',
 'MountGinini', 'Ballarat', 'Bendigo', 'Sale' ,'MelbourneAirport' ,'Melbourne',
 'Mildura' ,'Nhil' ,'Portland', 'Watsonia', 'Dartmoor' ,'Brisbane' ,'Cairns',
 'GoldCoast' ,'Townsville' ,'Adelaide', 'MountGambier', 'Nuriootpa' ,'Woomera',
 'Albany', 'Witchcliffe' ,'PearceRAAF' ,'PerthAirport' ,'Perth' ,'SalmonGums',
 'Walpole' ,'Hobart' ,'Launceston' ,'AliceSprings' ,'Darwin' ,'Katherine',
 'Uluru']
    
    direction=['nan','W', 'WNW' ,'WSW', 'NE' ,'NNW', 'N' ,'NNE', 'SW','ENE' ,'SSE', 'S', 
               'NW' ,'SE','ESE', 'E' ,'SSW']
    #Location=st.selectbox('Select a location',options=area)
    MinTemp=st.text_input('Enter minimum temperature of the day in celcius')
    MaxTemp=st.text_input('Enter maximum temperature of the day in celcius')
    Rainfall=st.text_input('Enter rainfall in cms')
    #WindGustDir=st.selectbox('Select wind gust direction ',options=direction)
    WindGustSpeed=st.text_input('Enter the gust speed in meter/sec')
    #WindDir9am=st.selectbox('Select wind direction at 9am',options=direction)
    #WindDir3pm=st.selectbox('Select wind direction at 3pm',options=direction)
    WindSpeed9am=st.text_input('Enter wind speed at 9am in m/sec')
    WindSpeed3pm=st.text_input('Enter wind speed at 3pm in m/sec')
    Humidity9am=st.text_input('Enter humidity at 9am in gm/kg')
    Humidity3pm=st.text_input('Enter humidity at 3pm in gm/kg')
    Pressure9am=st.text_input('Enter pressure at 9am in atm')
    Pressure3pm=st.text_input('Enter pressure at 3pm in atm')
    Temp9am=st.text_input('Enter the temperature at 9am in celcius')
    Temp3pm=st.text_input('Enter the temperature at 3pm in celcuis')
    #RainToday=st.text_input('Enter rain today,if yes 1 else 0')
    
    #code for prediction
    
    diagonsis=''
    
    
    #creating a button for prediction
    if(st.button('Predict')):
        diagonsis=rainfall_predict([MinTemp,MaxTemp,Rainfall,WindGustSpeed,WindSpeed9am,WindSpeed3pm,Humidity9am,Humidity3pm,Pressure9am,Pressure3pm,Temp9am,Temp3pm])
    
    
    st.success(diagonsis)
    
if __name__ =='__main__':
    main()
    
    