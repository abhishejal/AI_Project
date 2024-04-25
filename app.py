# #-----------------------------------Importing libraries

import streamlit as st
from models.utils import AI_Project

def main():
    '''
    this is the streamlit app function which will be called when the app is run
    '''

    st.title("Prediction Web Application")

    complaint = st.text_input("Enter the complaint")

    diagnosis = ""
    result = ""

    # creating the button~
    if st.button("Forward_the_complaint"):
        diagnosis = AI_Project(complaint)
        result = diagnosis.forward_complaint(complaint)

    st.success(result)
    return result

if __name__ == '__main__':
    main()