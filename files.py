import streamlit as st
import pandas as pd

st.subheader('Upoading the CSV file :')
df = st.file_uploader('Upload the CSV file :', type =['csv','xlsx'])

st.subheader('Loading the CSV file :')
df = pd.read_csv("Football.csv")
if df is not None:
    st.table(df.head())

st.subheader('Working with Images')
img_file = st.file_uploader('Upload the Image File', type =['png','jpg','jpeg'])
if img_file is not None:
    st.image(img_file)


st.subheader('Working with Videos')
video_file = st.file_uploader('Upload the Video file', type= ['mp4','mkv'])
if video_file is not None:
    st.video(video_file, start_time=2)

st.subheader('Working with Audios')
audio_file = st.file_uploader('Upload the Audio file', type= ['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file)
