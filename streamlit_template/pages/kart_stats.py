import pandas as pd
import streamlit as st

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')
df_kart = df_kart[['Body','Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed']]
st.dataframe(df_kart.style
                .highlight_max(color='lightgreen', axis=0, subset=['Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed'])
                .highlight_min(color='pink', axis=0, subset=['Weight','Acceleration','On-Road traction','Mini-Turbo','Ground Speed'])
)

st.header('Correlation of Weight and Other Statistics:')
st.line_chart(df_kart, x='Weight', y=['Acceleration','On-Road traction','Mini-Turbo','Ground Speed'])

st.header('Kart Weights Plotted Against Ground Speed and Accelerations:')
st.scatter_chart(df_kart, x='Ground Speed' , y='Acceleration' , size='Weight')

st.header('View Kart Stats:')
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')