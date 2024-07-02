import streamlit as st
import joblib

# # Load your pre-trained model
pipeline = joblib.load("svm_model.joblib")

# Function for prediction the answer
def predict_input_svm(pipeline, user_input):
    predicted_response = pipeline.predict([user_input])[0]
    return predicted_response

# Chatbot ui 
st.title("Mental Healthcare Chatbot")
st.markdown("Hello! I'm your friendly mental health care assistant.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Enter your input here"):
    
    st.chat_message("user").markdown(prompt)
   
    st.session_state.messages.append({"role": "user", "content": prompt})

    response =predict_input_svm(pipeline, prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})



