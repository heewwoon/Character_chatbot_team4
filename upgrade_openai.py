import os
import subprocess
import streamlit as st

# 오픈에이아이 라이브러리 업그레이드
def upgrade_openai():
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", "--upgrade", "openai"])
        st.success("OpenAI 라이브러리가 성공적으로 업그레이드되었습니다!")
    except Exception as e:
        st.error(f"라이브러리 업그레이드 중 오류가 발생했습니다: {str(e)}")

# 버튼을 클릭하면 라이브러리 업그레이드 실행
if st.button("Upgrade OpenAI Library"):
    upgrade_openai()
