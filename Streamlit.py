import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import streamlit as st

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp
     {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('bg_streamlit.jpg')


# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)



def prediction(input_data):
    x = np.array(input_data)
    prediction = model.predict(x.reshape(1,-1))
    return prediction

def main():
    st.markdown("<h1 style='color: Black;font_size : 3rem'>Scrabble Game</h1>", unsafe_allow_html=True)
    game_id = st.number_input("Game ID")
    user_score = st.number_input("User Score")
    bot_name = st.number_input("Bot name")
    bot_score = st.number_input("Bot Score")
    bot_rating = st.number_input("Bot Rating")
    user_freq = st.number_input("User Frequency")

    pred = ''
    if st.button('Predict'):
        try:
            pred = prediction([game_id, user_score,bot_name, bot_score, bot_rating, user_freq])
        except Exception as e:
            print(e)

    st.success(pred)
    

main()
