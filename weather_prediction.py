import  streamlit as st
import pickle

st.subheader("Weather Prediction")
pn=st.number_input("Enter Precipitation:")
maxt=st.number_input("Enter Max Tempreture:")
mint=st.number_input("Enter Min Tempreture:")
ws=st.number_input("Enter Wind Speed:")

btn=st.button("Predict!")

if btn:
    model=pickle.load(open("wp.pkl","rb"))
    res=model.predict([[pn,maxt,mint,ws]])[0]

    st.markdown(f"""weather condition: {res}""")

else:
    print("Invalid Input")