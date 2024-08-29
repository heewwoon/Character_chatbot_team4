import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "your-api-key"  # 여기에 실제 API 키를 입력하세요.

# Show title and description
st.title("💬 피카츄 Chatbot")
st.write(
    "앗! 야생의 피카츄 가(이) 나타났다!"
)

# 피카츄 말투로 대화하도록 설정
system_message = {
    "role": "system", 
    "content": "You are Pikachu. You only respond with 'Pika Pika!' or similar variations."
}

# Initialize chat history with the system message
if "messages" not in st.session_state:
    st.session_state.messages = [system_message]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("피카츄에게 말을 걸어보세요!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # 혹은 "gpt-3.5-turbo" 등
            prompt="\n".join(m["content"] for m in st.session_state.messages),
            max_tokens=150
        )

        # 응답 내용 처리
        message_content = response.choices[0].text.strip()
        st.session_state.messages.append({"role": "assistant", "content": message_content})
        
        with st.chat_message("assistant"):
            st.markdown(message_content)
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
