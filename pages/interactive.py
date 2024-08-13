import streamlit as st

st.title('🎶상호작용을 위한 앱 만들기')

st.write('https://www.youtube.com/playlist?list=PLSTJuHaq4hGVL0elWMRIuepBmKHq_QCpg')
st.link_button('유뷰브 영상 바로가기', 'https://www.youtube.com/playlist?list=PLSTJuHaq4hGVL0elWMRIuepBmKHq_QCpg')

st.image('https://cdn.wadiz.kr/ft/images/green001/2023/0502/20230502101219905_35.gif', width = 800)

col1, col2 = st.columns(2)
with col1:
    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExajZiMm4zOGJ0MzBnNjZhOHRnZ3Z2cnNheWdub25ucDJjM2xjMG5mcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TdfyKrN7HGTIY/giphy.webp")
with col2:
    st.success('제 캐릭터의 이름은 무엇일까요?')
    answer = st.text_input("이 캐릭터의 이름을 써주세요.")
    if answer == '스펀지밥':
        st.success("정답")
    else:
        st.error("다시 생각해주세요")

st.camera_input("사진을 찍어주세요")

st.latex("2x^2-1")
st.latex("cos(2x)+2")

st.expander('ddd')


tab1, tab2 =st.tabs(["봄",'여름'])
tab1.success("봄이에요")
tab2.info("여름이에요")

