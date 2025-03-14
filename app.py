import streamlit as st
import pickle


model = pickle.load(open('Spam detection model.pki','rb'))

st.title('SPAM EARLY DETECTION APP (S.E.D.A)')

message = st.text_input('Enter Message')

submit = st.button('Predict')


if submit:
    prediction = model.predict([message])[0] 
    
    if prediction == 1:
        st.write('This is a spam Message')
    else:
        st.write('Thia is a legitimate message')
st.balloons()