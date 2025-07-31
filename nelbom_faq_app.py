
import streamlit as st
import difflib

st.set_page_config(page_title="늘봄지원실 FAQ 자동응답", page_icon="🤖", layout="centered")

st.title("📚 늘봄지원실 FAQ 자동응답 챗봇")

st.markdown(
    """
    **사용 방법**  
    1. 상단에서 **질문 입력 방법**을 선택하세요.  
    2. *드롭다운*을 선택하면 준비된 질문 목록에서 고를 수 있고, *직접 질문 입력*을 선택하면 자유롭게 질문을 입력할 수 있습니다.  
    3. 질문에 맞는 답변이 화면에 표시됩니다.  

    ℹ️ 신규 질문은 GitHub 이슈로 남겨주세요!
    """
)

# 주요 FAQ 데이터 -----------------------------------------------------------
FAQ_DICT = {
    "늘봄학교 운영 과정은 무엇입니까": "늘봄학교 운영 과정은 도담도담(맞춤형 프로그램), 선택형 교육프로그램, 선택형 돌봄프로그램 세 가지로 이루어져 있습니다.",
    "도담도담 또는 맞춤형 프로그램이 무엇입니까": "도담도담(맞춤형 프로그램)은 초등학교 1~2학년을 대상으로 수업이 끝난 후 하루 최대 2시간까지 운영되는 무료 프로그램입니다.",
    "선택형교육 프로그램은 무엇입니까": "선택형 교육프로그램은 초등~고등학생까지 선택하여 수강할 수 있는 방과후 교육프로그램입니다.",
    "선택형돌봄프로그램은 무엇입니까": "선택형 돌봄프로그램은 방과후 돌봄이 필요한 초등~고등학생을 대상으로 이루어지는 돌봄 프로그램입니다.",
    "운영시간": "늘봄지원실 운영시간은 오후 3시부터 오후 6시까지입니다."
}

# ----------------------------------------------------------------------------
mode = st.radio("질문 입력 방법을 선택하세요:", ("드롭다운에서 선택", "직접 질문 입력"), horizontal=True)

if mode == "드롭다운에서 선택":
    selected_question = st.selectbox(
        "질문을 선택하세요:",
        list(FAQ_DICT.keys()),
        index=None,
        placeholder="질문을 골라주세요…"
    )
    if selected_question:
        st.success(FAQ_DICT[selected_question])
else:
    user_question = st.text_input("질문을 입력하세요:")
    if user_question:
        # 1차: 포함 검색
        match_key = next((q for q in FAQ_DICT if q in user_question), None)

        # 2차: 유사도 검색
        if not match_key:
            candidates = difflib.get_close_matches(user_question, FAQ_DICT.keys(), n=1, cutoff=0.6)
            match_key = candidates[0] if candidates else None

        if match_key:
            st.success(FAQ_DICT[match_key])
        else:
            st.info("죄송합니다. 해당 질문에 대한 답변을 아직 준비하지 못했습니다. 담당자에게 문의해주세요.")

# 푸터 ----------------------------------------------------------------------
st.divider()
st.caption("© 2025. 늘봄지원실 FAQ 챗봇 · Streamlit")
