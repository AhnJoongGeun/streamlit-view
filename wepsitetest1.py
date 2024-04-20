import streamlit as st
st.write('# 강원과학고 대신전해드립니다')
st.write('## 어떤 도움이 필요하신가요?')

import streamlit as st

genre = st.radio(
    "도움 종류",
    ["상담", "고민", "속마음"])

import streamlit as st
options = st.multiselect(
    '학생',
    ['익명',
'1101 곽호영',
'1102 김담휘',
'1103 김민건',
'1104 김범준',
'1105 김영균',
'1106 김영조',
'1107 김지원',
'1108 김창규',
'1109 노윤철',
'1110 유성재',
'1111 유승원',
'1112 유초비',
'1113 윤상원',
'1114 이정호',
'1115 이현우',
'1116 정우석',
'1117 정효림',
'1118 천현서',
'1119 최하영',
'1120 홍진기',
'1201 강승원',
'1202 권하늬',
'1203 김윤하',
'1204 김한중',
'1205 남규민',
'1206 민지현',
'1207 박서진',
'1208 박재현',
'1209 박찬웅',
'1210 서민성',
'1211 원재인',
'1212 원하담',
'1213 이강현',
'1214 이건희',
'1215 이민찬',
'1216 이주섭',
'1217 이주혁',
'1218 이지호',
'1219 임지승',
'1220 최원섭',
'1221 홍서현',
'1301 권민기',
'1302 김나람',
'1303 김민준',
'1304 김소희',
'1305 김승호',
'1306 김진우',
'1307 노아현',
'1308 박기동',
'1309 송유찬',
'1310 심민섭',
'1311 심예성',
'1312 이동률',
'1313 이아림',
'1314 이원희',
'1315 임승준',
'1316 임휘수',
'1317 정단비',
'1318 정하민',
'1319 허강현',
'1320 허정원'])


import streamlit as st
options = st.multiselect(
    '전하고 싶은 대상',
    ['관리자',
'1101 곽호영',
'1102 김담휘',
'1103 김민건',
'1104 김범준',
'1105 김영균',
'1106 김영조',
'1107 김지원',
'1108 김창규',
'1109 노윤철',
'1110 유성재',
'1111 유승원',
'1112 유초비',
'1113 윤상원',
'1114 이정호',
'1115 이현우',
'1116 정우석',
'1117 정효림',
'1118 천현서',
'1119 최하영',
'1120 홍진기',
'1201 강승원',
'1202 권하늬',
'1203 김윤하',
'1204 김한중',
'1205 남규민',
'1206 민지현',
'1207 박서진',
'1208 박재현',
'1209 박찬웅',
'1210 서민성',
'1211 원재인',
'1212 원하담',
'1213 이강현',
'1214 이건희',
'1215 이민찬',
'1216 이주섭',
'1217 이주혁',
'1218 이지호',
'1219 임지승',
'1220 최원섭',
'1221 홍서현',
'1301 권민기',
'1302 김나람',
'1303 김민준',
'1304 김소희',
'1305 김승호',
'1306 김진우',
'1307 노아현',
'1308 박기동',
'1309 송유찬',
'1310 심민섭',
'1311 심예성',
'1312 이동률',
'1313 이아림',
'1314 이원희',
'1315 임승준',
'1316 임휘수',
'1317 정단비',
'1318 정하민',
'1319 허강현',
'1320 허정원',
     '원은미',
     '강청묵',
     '김명진',
     '김수현',
     '이지영',
     '유혜림',
     '김정동',
     '지혜미',
     '오일석',
     '지은영',
     '최진우',
     '신승원',
     '박다혜',
     '성혜진',
     '이정미',
     '이상찬',
     '고보배',
     '권용표',
     '이소라',
     '김재헌',
     '이경애',
     '신승환',
     '유선륜',
     '박소현',
     '김주영',
     '김경하',
     '이진한',
     '최혁',
     '홍예림',
     '이지영',
     '김화성',
     '김상욱',
     '김시내',
     '김윤지',
     '유정',
     '정리나',
     '조운재',
     '임종원',
     '홍상희'])

import streamlit as st
options = st.multiselect(
    '전달 장소',
    ['집',
     '병원',
     '양현재1',
     '양현재2',
     '양현재3',
     '1-1반',
     '1-2반',
     '1-3반'
     '2-1반',
     '2-2반',
     '2-3반',
     '3-1반',
     '3-2반',
     '3-3반',
     '1층교무실',
     'STEAM실',
     '급식실',
     '농구장',
     '대회의실',
     '소회의실',
     '무한상상실',
     '멀티미디어실',
     '물리세미나실',
     '물리실험실',
     '상담실',
     '생물세미나실',
     '생물실험실',
     '선각재',
     '수학탐구실',
     '시청각실',
     '음악실',
     '지구과학세미나실',
     '지구과학실험실',
     '천문대',
     '체육관',
     '폴라리스실'
     '풋살장',
     '학생부',
     '화학세미나실',
     '화학실험실',
     '휴게실',
     '화장실'])
import streamlit as st

txt = st.text_area(
    "사유",
    )
         
st.button("신청하기", type="primary")
