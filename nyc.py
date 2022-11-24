import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def data_load():
    df = pd.read_csv('citibike-tripdata.csv')
    df['started_at'] = pd.to_datetime(df['started_at'])
    df = df.rename(columns= {'start_lat':'lat', 'start_lng':'lon'})
    return df

st.set_page_config(page_title="Citibike NYC App")

df=data_load()

st.title('Cicle Rides in NYC')
st.subheader('Creado por Angel Cavazos')

sidebar = st.sidebar

raw = sidebar.checkbox('Show raw data')

if raw:
    st.subheader('Raw Data')
    st.dataframe(df)

hist_hora = sidebar.checkbox('Recorridos por hora')

if hist_hora:
    fig = px.histogram(df,df['started_at'].dt.hour,labels={'count':'Viajes','x':'Hora'},range_x=[0,23])
    fig.update_layout(xaxis = dict(tickmode = 'linear',),barmode='group',bargap=0.2)
    st.write(fig)

hora = sidebar.select_slider('Hora',{0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23})  

st.markdown(f'Mapa de recorridos iniciados a la(s) {hora}:00')
df_filtro = df[df['started_at'].dt.hour == hora]
st.map(df_filtro)