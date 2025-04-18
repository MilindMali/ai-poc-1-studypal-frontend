import streamlit as st 
import requests 

st.set_page_config(
    page_title="StudyPal", 
    page_icon="🤖",
    layout="centered", 
)

st.title("🤖 StudyPlan Application")


api_url = "http://127.0.0.1:8000/ask"  

#get user input 
user_question = st.text_input(label="Ask your question here", placeholder="What is the best way to study for an exam?") 

#button to trigger the api 
if st.button("get answer"): 
    response=requests.post( 
        url=api_url, 
        json={"question": user_question}
    ) 
    result = response.json() 
    answer=result['answer'] 

    st.success(answer)