import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('sleep.csv')
# df['Sleep Disorder']=df['Sleep Disorder'].replace(np.nan,'Normal')
print(df.head())
st.sidebar.header("Sleep dashboard")
st.sidebar.image('R.jpg')
st.sidebar.write('the purpose of dashboard is to show the reasons of sleep disorder')
cat_filter=st.sidebar.selectbox('filters',['Gender','Occupation','BMI Category',None,'Sleep Disorder'])
a1, a2, a3, a4 =st.columns(4)
a1.metric("avg age",round(df['Age'].mean(),2))
a2.metric("Count oF ID",round(df['Person ID'].count(),2))
a3.metric("max daily steps",round(df['Daily Steps'].max(),2))
a4.metric("avg sleep duration",round(df['Sleep Duration'].mean(),2))
st.subheader('Sleep quality vs stress level',)
fig=px.scatter ( data_frame=df,x='Stress Level',y='Quality of Sleep',color=cat_filter,size='Quality of Sleep')
st.plotly_chart(fig,use_container_width=True)
c1,c2 = st.columns([4,3])
with c1:
    st.text('Occupation VS Avg Sleep Duration (Sorted)')
    avg_sleep_by_occ=df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False).reset_index()
    fig1=px.bar(data_frame=avg_sleep_by_occ,x='Occupation',y='Sleep Duration')
    st.plotly_chart(fig1,use_container_width=True)
with c2:
    st.text('Gender VS Quality of Sleep')
    gender_sleep=df.groupby('Gender')['Quality of Sleep'].mean().sort_values(ascending=False).reset_index()
    fig2=px.pie(gender_sleep,names='Gender',values='Quality of Sleep')
    st.plotly_chart(fig2,use_container_width=True)
st.subheader("pair plot & hotmap for nymerical features")
num_cols =['Physical Activity Level', 'Stress Level', 'Daily Steps', 'Quality of Sleep']
df_num= df[num_cols]
st.text("pair plot")
fig_pair=sns.pairplot(df_num)
st.pyplot(fig_pair)
st.text("Correlation heatmap (Selected numerical features)")

select_cols=['Sleep Duration','Physical Activity Level', 'Stress Level', 'Daily Steps', 'Quality of Sleep','Heart Rate']
df_selected=df[select_cols]
fig_heat, ax=plt.subplots(figsize=(10,6))
sns.heatmap(df_selected.corr(),annot=True,cmap='coolwarm',fmt="2f",ax=ax)
st.pyplot(fig_heat)