import streamlit as st
import openai

# 미리 입력된 OpenAI API 키 설정
openai_api_key = "your-api-key"  # 여기에 실제 API 키를 입력하세요.
openai.api_key = openai_api_key

# Show title and description
st.title("💬 피카츄 Chatbot")
st.write(
    #"This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses."
    "앗! 야생의 피카츄 가(이) 나타났다!"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages,
    )

    message_content = response['choices'][0]['message']['content']
    st.session_state.messages.append({"role": "assistant", "content": message_content})
    
    with st.chat_message("assistant"):
        st.markdown(message_content)
