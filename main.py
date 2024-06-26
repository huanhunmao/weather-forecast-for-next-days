import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecast days')
option = st.selectbox('Select data to view', ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} days in {place}')

def get_data(days):
    date = ['2024-25-6', '2024-26-6', '2024-27-6']
    temperature = [10, 11, 15]
    temperature = [days * i for i in temperature]
    return date,temperature

d, t = get_data(days)

figure = px.line(x = d,y = t,labels={'x': 'Date', 'y': 'Temperature'})
st.plotly_chart(figure)