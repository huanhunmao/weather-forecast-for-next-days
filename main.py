import streamlit as st
import plotly.express as px

from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecast days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

# def get_data(days):
#     date = ['2024-25-6', '2024-26-6', '2024-27-6']
#     temperature = [10, 11, 15]
#     temperature = [days * i for i in temperature]
#     return date,temperature

if place:
    filter_data = get_data(place, days)

    if option == 'Temperature':
        temperature = [dict['main']['temp'] for dict in filter_data]
        dates = [dict['dt_txt'] for dict in filter_data]
        figure = px.line(x = dates,y = temperature,labels={'x': 'Dates', 'y': 'Temperature'})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {
            'Clear': 'images/clear.png',
            'Clouds': 'images/cloud.png',
            'Rain': 'images/rain.png',
            'Snow': 'images/snow.png'
        }
        sky_condition = [dict['weather'][0]['main'] for dict in filter_data]
        image_path = [images[condition] for condition in sky_condition]
        print(image_path)
        st.image(image_path, width=115)