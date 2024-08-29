import streamlit as st
import openai

# 미리 입력된 OpenAI API 키 설정
openai_api_key = "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"  # 여기에 실제 API 키를 입력하세요.
openai.api_key = openai_api_key

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
print(response.choices[0].message["content"])
