import streamlit as st

# st.write(3)
# st.write("어서오세요")
# st.write([
#     "도윤",
#     "하빈",
#     "유하"
# ])
# st.write({
#     "아이스 커피": 4500,
#     "카페 모카": 5000,
#     "녹차": 5000
# })
# st.write([
#     { "name": "아이스 커피", "price": 4500 },
#     { "name": "카페모카", "price": 5000 },
#     { "name": "녹차", "price": 5000 }
# ])


# st.title("제목")
# st.header("머릿말1")
# st.subheader("작은 머릿말1")
# st.text("본문1")
# st.divider()
# st.header("머릿말2")
# st.subheader("작은 머릿말2")
# st.text("본문2")

# st.success("성공")
# st.info("정보 전달")
# st.warning("경고")
# st.error("오류")

#st.metric("오늘 날씨", "10°C", help="강원도 기준", delta=-2, border=True)

# st.image("/workspaces/code_practice/codeit_streamlit/meerkat.jpg")
# #st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Meerkat_%28Suricata_suricatta%29_Tswalu.jpg/728px-Meerkat_%28Suricata_suricatta%29_Tswalu.jpg")

# st.image("/workspaces/code_practice/codeit_streamlit/meerkat.jpg", width=200)  #width-> 너비조절

# name = st.text_input("이름")
# st.write(f"안녕하세요, {name}님!")

# st.title("과목 설문 조사")

# date = st.date_input("수강 날짜")
# name = st.text_input("이름")
# description = st.text_area("전체 소감")
# student_type = st.selectbox("교육과정", options=["중학생", "고등학생", "대학생"])
# level = st.number_input("학년", 1, step=1)
# preference = st.slider("과목 선호도", min_value=1, max_value=10)
# difficulty = st.radio(
#     "난이도",
#     options=["쉬웠다", "보통", "어려웠다"],
# )
# is_retaking = st.checkbox("재수강 여부")

# clicked = st.button("확인")
# if clicked:
#     st.write("클릭함!")


# name = st.text_input("이름")
# clicked = st.button("확인")
# if clicked:
#     st.write(f"{name}님 안녕하세요!")

# st.table([
#     "도윤",
#     "하빈",
#     "유하"
# ])
# st.table({
#     "아이스 커피": 4500,
#     "카페 모카": 5000,
#     "녹차": 5000
# })
# st.table([
#     {"메뉴": "아이스커피", "가격": 4500},
#     {"메뉴": "카페 모카", "가격": 5000},
#     {"메뉴": "녹차", "가격": 5000},
# ])

# value1 = st.data_editor([
#     "도윤",
#     "하빈",
#     "유하"
# ])
# st.write(value1)

# value2 = st.data_editor([
#   { "메뉴": "아이스커피", "가격": 4500 },
#   { "메뉴": "카페 모카", "가격": 5000 },
#   { "메뉴": "녹차", "가격": 5000 },
# ])
# st.write(value2)

# st.header("2024년 서울 날씨")
# data = [
#     {
#         "날짜": "2024-01",
#         "평균 기온": -0.5,
#         "평균 최저 기온": -3.9,
#         "평균 최고 기온": 3.6
#     },
#     {
#         "날짜": "2024-02",
#         "평균 기온": 3.8,
#         "평균 최저 기온": 0.2,
#         "평균 최고 기온": 8.2
#     },
#     {
#         "날짜": "2024-03",
#         "평균 기온": 7,
#         "평균 최저 기온": 2.4,
#         "평균 최고 기온": 12
#     },
#     {
#         "날짜": "2024-04",
#         "평균 기온": 16.3,
#         "평균 최저 기온": 11.5,
#         "평균 최고 기온": 22.4
#     },
#     {
#         "날짜": "2024-05",
#         "평균 기온": 18.5,
#         "평균 최저 기온": 13.8,
#         "평균 최고 기온": 23.7
#     },
#     {
#         "날짜": "2024-06",
#         "평균 기온": 24.6,
#         "평균 최저 기온": 19.9,
#         "평균 최고 기온": 30.1
#     },
#     {
#         "날짜": "2024-07",
#         "평균 기온": 26.6,
#         "평균 최저 기온": 24.1,
#         "평균 최고 기온": 29.6
#     },
#     {
#         "날짜": "2024-08",
#         "평균 기온": 29.3,
#         "평균 최저 기온": 26.3,
#         "평균 최고 기온": 33.3
#     },
#     {
#         "날짜": "2024-09",
#         "평균 기온": 25.5,
#         "평균 최저 기온": 22,
#         "평균 최고 기온": 29.8
#     },
#     {
#         "날짜": "2024-10",
#         "평균 기온": 16.7,
#         "평균 최저 기온": 12.7,
#         "평균 최고 기온": 21.4
#     },
#     {
#         "날짜": "2024-11",
#         "평균 기온": 9.7,
#         "평균 최저 기온": 5.5,
#         "평균 최고 기온": 14.9
#     },
#     {
#         "날짜": "2024-12",
#         "평균 기온": 0.8,
#         "평균 최저 기온": -2.9,
#         "평균 최고 기온": 5.3
#     }
# ]

# st.line_chart(data, x="날짜", y=["평균 기온", "평균 최저 기온", "평균 최고 기온"], x_label="날짜", y_label="기온")

# if "number" not in st.session_state:
#     st.session_state["number"] = 1
# st.text(st.session_state["number"])

# clicked = st.button("더하기")
# if clicked:
#     st.session_state["number"] += 1
#     st.rerun()


# if "value" not in st.session_state:
#     st.session_state["value"] = []

# todo = st.text_input("할 일")
# data = st.date_input("마감 기한")
# clicked = st.button("추가하기")

# if clicked:
#     st.session_state["value"].append({"할 일":todo, "마감 기한":data})
#     st.rerun()

# st.data_editor(st.session_state["value"])

# data = {}

# with st.form("과목 설문 조사"):
#   data["date"] = st.date_input("수강 날짜")
#   data["name"] = st.text_input("이름")
#   data["description"] = st.text_area("전체 소감")
#   data["level"] = st.number_input(label="학년", value=1, step=1)
#   data["preference"] = st.slider(label="과목 선호도", min_value=1, max_value=10)
#   data["difficulty"] = st.radio(
#       label="난이도",
#       options=["쉬웠다", "보통", "어려웠다"],
#   )
#   data["is_retaking"] = st.checkbox(label="재수강 여부")
#   st.form_submit_button("적용")

# st.table(data)

def calculate_grade(score):
    if score >= 70:
        return "A"
    if score >= 60:
        return "B"
    if score >= 50:
        return "C"
    return "F"

with st.form("학생 정보"):
  name = st.text_input("이름")
  score = st.number_input("점수")
  st.form_submit_button("제출")

st.table({
    "name": name,
    "score": score,
    "grade": calculate_grade(score),
})