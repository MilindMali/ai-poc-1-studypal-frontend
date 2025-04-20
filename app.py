import streamlit as st 
import requests 

#-----page configuration----- 


st.set_page_config(
    page_title="StudyPal", 
    page_icon="🤖",
    layout="centered", 
)   

st.title("🤖 StudyPlan Application") 

#-----api details-----
API_URL="http://127.0.0.1:8000/ask"
PROVIDERS=["Groq","Ollama"]
MODELS=["llama 3.3","Deepseek R1"] 


st.session_state.setdefault("show_settings",False)
st.session_state.setdefault("provider",PROVIDERS[0]) 
st.session_state.setdefault("model",MODELS[0]) 


#-----layout----- 
col1, col2 = st.columns([8,1]) 
question = col1.text_input(label="Ask your question here", placeholder="What is AI?")  

if col2.button("⚙️", help="select the model setting"): 
    st.session_state.show_settings = not st.session_state.show_settings

# -----model setting-----
if st.session_state.show_settings: 
    with st.expander("Model Setting", expanded=True): 
        st.session_state.provider=st.selectbox(label="Provider", options=PROVIDERS, index=PROVIDERS.index(st.session_state.provider)) 
        st.session_state.model=st.selectbox(label="Model", options=MODELS, index=MODELS.index(st.session_state.model)) 
        st.success(f"Using {st.session_state.provider} with {st.session_state.model}") 


#-----get answer from api-----

if st.button("get answer"):
    response=requests.post(url=API_URL, json={"question": question}) 
    result = response.json()
    answer=result['answer']
    st.success(answer)