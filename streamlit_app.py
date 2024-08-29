import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "your-api-key"  # 여기에 실제 OpenAI API 키를 입력하세요.

# 앱 제목 및 설명
st.title("💬 피카츄 Chatbot")
st.write("앗! 야생의 피카츄가 나타났다! 피카츄와 대화해보세요!")

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
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 사용 가능한 모델을 지정하세요. 최신 모델 이름을 확인하세요.
            messages=st.session_state.messages,
            max_tokens=150  # 응답의 길이를 조절할 수 있습니다.
        )

        # 응답 내용 처리
        message_content = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": message_content})
        
        with st.chat_message("assistant"):
            st.markdown(message_content)
    except Exception as e:
        st.error(f"응답 생성 중 오류가 발생했습니다: {str(e)}")
