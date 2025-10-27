import streamlit as st
import time

st.title('Welcome to Elegibility to Drive App!')
x= st.text_input('Please Enter Your Name: ').title()
y = st.text_input('Please Enter Your Age: ')
ch = st.button('Check Elegibility to Drive',type='primary')
if x and y :
    time.sleep(2)
    st.header(f"Welcome: {x} \n Because Your [{y}] Years old")
    if ch :
        st.toast('Checking Statue Now!')
        time.sleep(2)
        if int(y) >=18:
            st.header('You are Allowed to drive')
            st.balloons()
        else:
            st.header(f'Sorry You are not Allowed To drive Please come back after {18-int(y)} Years')
elif not x :
    st.write('Name Cant be Empty!')
elif  not y:
    st.write('Age Cant be Empty!')
else:
    st.write('Cant be empty Please Enter Data to Process!')
    

