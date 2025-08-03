import streamlit as st
import joblib
import pandas as pd

model=joblib.load("food_review_sentiment.pkl")

st.set_page_config(page_title="Sentiment Analysis", layout="wide")

st.markdown("""
<div style="background-color:brown; padding: 10px; border-radius: 10px;">
    <h1 style="color:white; text-align:center;">🍽️ Food Sentiment Prediction</h1>
</div>
""", unsafe_allow_html=True)

st.sidebar.image("f:/images/flag.jpg")
st.sidebar.header("📞Contact us")
st.sidebar.text("99999999")

st.sidebar.header("🧑‍🤝‍🧑About us")
st.sidebar.text("we are a group of ML Engineers working on Sentiment Analysis")

st.text('')

msg = st.text_input("💬 Enter Your Message", placeholder="Enter your review")

if st.button("Predict"):
    resp=model.predict([msg])
    if resp[0]==0:
        st.title("👎 Dislike")
    else:
        st.title("👍 Like")
        st.balloons()

st.title("upload file for bulk prediction")
path=st.file_uploader("upload csv file",type=['csv','txt'])
if path is not None:
    df=pd.read_csv(path,names=['Msg'])
    st.dataframe(df,width=700)
if st.button("Predict",key='b2'):
    df['Sentiment']=model.predict(df.Msg)
    df['Sentiment']=df['Sentiment'].map({0:"👎 Dislike",1:"👍 Like"})
    st.dataframe(df,width=700)
