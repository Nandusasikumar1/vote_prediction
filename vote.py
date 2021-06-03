import pickle
import streamlit as st
predictor1=pickle.load(open('model1.pickle','rb'))
predictor2=pickle.load(open('model2.pickle','rb'))
predictor3=pickle.load(open('model3.pickle','rb'))
def predict(x):
    n_votes1=predictor1.predict([[x]])
    n_votes2=predictor2.predict([[x]])
    n_votes3=predictor3.predict([[x]])
    return n_votes1,n_votes2,n_votes3
def app():
    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    Total_electors=st.number_input('Enter the number of total eligible voters in your assembly constituency(Kerala only)',value=150000)
    if st.button('Predict'):
        result1,result2,result3=predict(Total_electors)
        st.success('Total votes are more likely to be any number close to these three numbers-{},{},{}'.format(result1,result2,result3))
app()
